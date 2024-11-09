import pathlib
from typing import Generator

import pytest
import frontmatter
from xprocess import ProcessStarter
from playwright.sync_api import Page, expect, sync_playwright


@pytest.fixture(scope="module")
def page_url(xprocess, url_port):
    """Returns the url of the live server"""

    url, port = url_port

    class Starter(ProcessStarter):
        timeout = 20
        # Start the process
        args = [
            "bundle",
            "exec",
            "jekyll",
            "serve",
            "--source",
            pathlib.Path().cwd().absolute(),
            "--port",
            port,
        ]
        terminate_on_interrupt = True
        pattern = "Server running... press ctrl-c to stop."

    xprocess.ensure("page_url", Starter)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Return the URL of the live server
        yield page, url

        # Clean up the process
        xprocess.getinfo("page_url").terminate()


def test_destination(
    loaded_route: str,
    page_url: tuple[Page, str],
) -> None:
    """Test that the destinations page loads with seeded data"""
    # Create a destination
    page, live_server_url = page_url
    response = page.goto(f"{live_server_url}/{loaded_route}")

    assert response.status == 200  # Check that the page loaded successfully


LANG_ROUTES = (
    "/es/",
    "/es/about/",
    "/es/events/",
    "/es/community/",
    "/sw/",
    "/sw/about/",
    "/sw/events/",
    "/sw/community/",
)


@pytest.mark.parametrize("route", LANG_ROUTES)
def test_headers_in_language(page_url: tuple[Page, str], route: str) -> None:
    """checks the route and the language of each route"""
    page, live_server_url = page_url
    response = page.goto(f"{live_server_url}{route}")
    assert response.status == 200
    doc_lang = page.evaluate("document.documentElement.lang")
    lang = route.lstrip("/").split("/", maxsplit=1)[
        0
    ]  # urls start with the language if not en
    assert doc_lang == lang


@pytest.mark.parametrize(
    "title, url",
    (
        ("Home", "/"),
        ("Blog", "/blog"),
        ("About Us", "/about/"),
        ("Events", "/events/"),
        ("Community", "/community/"),
    ),
)
def test_bpdevs_title_en(page_url: tuple[Page, str], title: str, url: str) -> None:
    page, live_server_url = page_url
    page.goto(f"{live_server_url}{url}")
    expect(page).to_have_title(f"Black Python Devs | {title}")


def test_mailto_bpdevs(page_url: tuple[Page, str]) -> None:
    page, live_server_url = page_url
    page.goto(live_server_url)
    mailto = page.get_by_role("link", name="email")
    expect(mailto).to_have_attribute("href", "mailto:contact@blackpythondevs.com")


def test_carousel_displayed(page_url: tuple[Page, str]) -> None:
    page, live_server_url = page_url
    page.goto(live_server_url)

    carousel = page.locator(".carousel")
    expect(carousel).to_be_visible()

    next_button = page.locator(".carousel-control-next")
    prev_button = page.locator(".carousel-control-prev")
    expect(next_button).to_be_visible()
    expect(prev_button).to_be_visible()


@pytest.mark.parametrize(
    "url",
    (
        "/",
        "/blog",
    ),
)
def test_page_description_in_index_and_blog(page_url: tuple[Page, str], url: str):
    """Checks for the descriptions data in the blog posts. There should be some objects with the class `post-description`"""
    page, live_server_url = page_url
    page.goto(f"{live_server_url}{url}")
    expect(page.locator("p.post-description").first).to_be_visible()
    expect(page.locator("p.post-description").first).not_to_be_empty()


def stem_description(
    path: pathlib.Path,
) -> Generator[tuple[str, frontmatter.Post], None, None]:
    """iterate throug a list returning the stem of the file and the contents"""

    for entry in path.glob("*.md"):
        yield (entry.stem, frontmatter.loads(entry.read_text()))


blog_posts = stem_description(pathlib.Path("_posts"))


@pytest.mark.parametrize("post", list(blog_posts))
def test_page_blog_posts(
    page_url: tuple[Page, str], post: tuple[str, frontmatter.Post]
):
    """Checks that the meta page description matches the description of the post"""
    page, live_server_url = page_url
    entry_stem, frontmatter = post
    url = f"{live_server_url}/{entry_stem}/"
    page.goto(url)
    page.wait_for_selector(
        'meta[name="description"]',
        timeout=5000,
        state="attached",
    )
    assert (
        page.locator('meta[name="description"]').get_attribute("content")
        == frontmatter["description"]
    )

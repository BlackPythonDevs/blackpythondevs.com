import pathlib

import pytest
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
    page.goto(f"{live_server_url}/{url}")
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

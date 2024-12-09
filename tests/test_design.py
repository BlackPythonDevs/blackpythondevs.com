import pathlib

import pytest
from playwright.sync_api import Page, sync_playwright
from xprocess import ProcessStarter


@pytest.fixture(scope="module")
def per_device_page_url(xprocess, loaded_profile, url_port):
    """Returns the url of the live server"""

    url, port = url_port

    class Starter(ProcessStarter):
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

    xprocess.ensure("per_device_page_url", Starter)

    with sync_playwright() as p:
        device = p.devices[loaded_profile]
        browser = p.chromium.launch()
        context = browser.new_context(**device)
        page = context.new_page()

        # Return the URL of the live server
        yield page, url

        # Clean up the process
        xprocess.getinfo("per_device_page_url").terminate()


@pytest.fixture(scope="session")
def create_test_image():
    image_path = pathlib.Path("./").joinpath("test_images")

    if not image_path.is_dir():
        image_path.mkdir()
    return image_path


@pytest.mark.design
def test_route_designs(
    loaded_route: str,
    per_device_page_url: tuple[Page, str],
    create_test_image,
    request,
) -> None:
    """Test that the destinations page loads with seeded data"""
    # Create a destination
    page, live_server_url = per_device_page_url
    response = page.goto(f"{live_server_url}/{loaded_route}")
    page.screenshot(
        path=create_test_image.joinpath(request.node.name).with_suffix(".jpg"),
        full_page=True,
    )
    assert response.status == 200

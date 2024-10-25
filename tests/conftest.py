import pytest
import ephemeral_port_reserve


@pytest.fixture(scope="module")
def url_port() -> tuple[str, int]:
    """returns the localhost and port"""
    hostname = ephemeral_port_reserve.LOCALHOST
    free_port = ephemeral_port_reserve.reserve(hostname)
    url = f"http://{hostname}:{free_port}"
    return url, free_port


ROUTES = [
    "",
    "blog",
    "about",
    "events",
    "community",
    "leadership",
    "book-club",
    "support",
]


@pytest.fixture(params=ROUTES)
def loaded_route(request):
    return request.param


PROFILES = [
    "iPhone 15",
    "iPhone 15 landscape",
    "iPhone 15 Plus",
    "iPhone 15 Plus landscape",
]


@pytest.fixture(scope="session", params=PROFILES)
def loaded_profile(request):
    return request.param

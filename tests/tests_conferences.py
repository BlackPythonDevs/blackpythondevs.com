import pytest
import datetime
from gh_issues import Repo, Issue
import _conferences.__main__ as conferences

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
yesterday = datetime.date.today() + datetime.timedelta(days=-1)

TEST_ISSUE_TEXT = f"""
## conference_name

New Conference

## url

https://pycon.us

## Conference Start Date

{yesterday.isoformat()}


## Conference End Date

{tomorrow.isoformat()}

## Conference Type

online

## Summary

This is a test

## Speaking

## Ignore This

This is bad
"""

TEST_ISSUE = Issue(
    repo=Repo("blackpythondevs", "blackpythondevs.github.io"),
    issue={"body": TEST_ISSUE_TEXT},
)


@pytest.mark.parametrize("test_url", ["pycon.us", "https://pycon.us", "ftp://pycon.us"])
def test_normalize_url(test_url: str):
    """
    Tests that urls are valid URLs with https:// protocols
    """

    assert conferences.normalize_url(test_url) == "https://pycon.us"


def tests___to_conference_date_converts_to_datetime():
    assert conferences.__to_conference_date("2024-01-01") == datetime.date(2024, 1, 1)


def tests_parse_conference():
    """
    Tests when given an Issue it is converted to the only have the keys requested
    """
    test_dictionary = {
        "conference_name": "New Conference",
        "url": "https://pycon.us",
        "conference_start_date": yesterday.isoformat(),
        "conference_end_date": tomorrow.isoformat(),
        "conference_type": "online",
        "conference_location": None,  # This was omitted from the value
        "summary": "This is a test",
        "speaking": None,
    }

    assert conferences.parse_conference(TEST_ISSUE) == test_dictionary


@pytest.mark.parametrize(
    "check_value, asserted_value",
    [
        ("conference_start_date", False),
        ("conference_end_date", True),
        ("missing_value", False),
    ],
)
def tests_validate_issue(check_value, asserted_value):
    """tests the date validator againse yesterday value (fail) and tomorrow value (pass)"""

    assert conferences._validate_issue(TEST_ISSUE, check_value) == asserted_value

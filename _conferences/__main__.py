import datetime
import json
import pathlib
from typing import Iterator
from urllib.parse import urlparse

import gh_issues

QUERY = "repo:blackpythondevs/blackpythondevs.github.io type:issue label:conference"


def get_conference_issues(
    query: str = QUERY,
) -> Iterator[gh_issues.Issue]:  # pragma no cover
    issues = gh_issues.issues_by_query(query)
    return issues


def normalize_url(url_match: str | None) -> str | None:
    """
    Parse the url and see if a scheme (`https`) is included in it.
    If not, then prepend `https` to the url from the issue body

    This guards against the website thinking the passed in url is another page on https://blackpythondevs.com/
    """
    if url_match:
        parsed_url = urlparse(url_match)
        url_scheme = parsed_url.scheme

        # If "https" is already the scheme, then we're good and don't need to do anything else
        if url_scheme == "https":
            return url_match

        # If the scheme is not "https", then we need to prepend "https" to the url
        if url_scheme.strip() == "":
            return f"https://{url_match}"
        else:
            # If the scheme is a valid protocol (ftp, http, etc.),
            # but not "https", then we need to replace it with "https"
            return url_match.replace(parsed_url.scheme, "https")


def write_conferences_to_file(confs: list[dict]):
    # Write the conferences to the _data/conferences.yml file
    conferences_path.write_text(json.dumps(confs))


def __to_conference_date(conference_date: str) -> datetime.date:
    return datetime.date.fromisoformat(conference_date)


def parse_conference(issue: gh_issues.Issue) -> dict[str, str | None]:
    """convert an issue to a dictionary of parsed data"""

    KEYS = [
        "conference_name",
        "url",
        "conference_start_date",
        "conference_end_date",
        "conference_type",
        "conference_location",
        "summary",
        "speaking",
    ]

    _issue = {k: getattr(issue, k, None) for k in KEYS}
    _issue["url"] = normalize_url(_issue.get("url", None))
    return _issue


def _validate_issue(issue: gh_issues.Issue, date_to_check: str) -> bool:
    """Validate an issue based on its `date_to_check`"""
    if not (valid_date := getattr(issue, date_to_check, False)):
        return False
    else:
        return __to_conference_date(valid_date) >= datetime.date.today()


def build_conferences() -> list[dict[str, str | None]]:  # pragma: no cover
    return [
        parse_conference(issue)
        for issue in get_conference_issues()
        if _validate_issue(issue, "conference_end_date")
    ]


if __name__ == "__main__":  # pragma: no cover
    ROOT = pathlib.Path(__file__).parent.parent
    conferences_path = ROOT.joinpath("_data/conferences.json")
    conferences = build_conferences()
    j_conferences = json.dumps(
        list(
            sorted(
                conferences,
                key=lambda x: __to_conference_date(x["conference_start_date"]),
            )
        ),
        indent=2,
    )
    conferences_path.write_text(f"{j_conferences}\n")

from github import Github

from popr import __version__
from popr.construct_base_url import construct_base_url
from popr.extract_branches import extract_branches

origin: str = "katrinleinweber/poPR"
repo: object = Github().get_repo(origin)


def test_version():
    assert __version__ == "0.1.0"


def test_extract_branches():
    assert extract_branches(repo, from_pulls=True) == {
        "branch-in-pr-1",
        "branch-in-pr-2",
    }
    assert extract_branches(repo) == {"master"}


def test_construct_base_url():
    base_url = construct_base_url(repo)
    assert base_url == "https://github.com/katrinleinweber/poPR/compare/master...{head}"

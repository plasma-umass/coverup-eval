# file semantic_release/errors.py:26-27
# lines [26, 27]
# branches []

import pytest
from semantic_release.errors import HvcsRepoParseError

def test_hvcs_repo_parse_error():
    with pytest.raises(HvcsRepoParseError) as excinfo:
        raise HvcsRepoParseError("An error occurred while parsing the repository information")

    assert str(excinfo.value) == "An error occurred while parsing the repository information"

# file cookiecutter/repository.py:21-23
# lines [21, 23]
# branches []

import pytest
import re
from cookiecutter.repository import is_repo_url

# Assuming REPO_REGEX is defined somewhere in the cookiecutter.repository module
# If not, we need to define it here for the test to work
# For example, a simple regex that matches URLs could be:
# REPO_REGEX = re.compile(r'https?://\S+')

def test_is_repo_url():
    # Test with a valid repository URL
    valid_repo_url = "https://github.com/audreyr/cookiecutter-pypackage.git"
    assert is_repo_url(valid_repo_url) is True

    # Test with an invalid repository URL
    invalid_repo_url = "not_a_valid_url"
    assert is_repo_url(invalid_repo_url) is False

    # Test with an empty string
    empty_string = ""
    assert is_repo_url(empty_string) is False

    # Test with a non-string object, converting it to string first
    non_string = 12345
    assert is_repo_url(str(non_string)) is False

# file string_utils/validation.py:177-201
# lines [194]
# branches ['193->194']

import pytest
from string_utils.validation import is_url

@pytest.fixture
def cleanup():
    # No cleanup is necessary for this test, but the fixture is here in case future cleanup is needed.
    yield
    # Any potential cleanup code would go here.

def test_is_url_with_non_string_input(cleanup):
    assert not is_url(None), "None should not be considered a valid URL"
    assert not is_url(123), "Integer should not be considered a valid URL"
    assert not is_url([]), "List should not be considered a valid URL"
    assert not is_url({}), "Dictionary should not be considered a valid URL"

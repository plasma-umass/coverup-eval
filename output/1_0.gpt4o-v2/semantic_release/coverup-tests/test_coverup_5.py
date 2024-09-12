# file: semantic_release/errors.py:10-11
# asked: {"lines": [10, 11], "branches": []}
# gained: {"lines": [10, 11], "branches": []}

import pytest
from semantic_release.errors import ImproperConfigurationError, SemanticReleaseBaseError

def test_improper_configuration_error():
    with pytest.raises(ImproperConfigurationError) as exc_info:
        raise ImproperConfigurationError("This is a test error")
    assert str(exc_info.value) == "This is a test error"
    assert isinstance(exc_info.value, ImproperConfigurationError)
    assert isinstance(exc_info.value, SemanticReleaseBaseError)

# file semantic_release/errors.py:10-11
# lines [10, 11]
# branches []

import pytest
from semantic_release.errors import ImproperConfigurationError

def test_improper_configuration_error():
    with pytest.raises(ImproperConfigurationError) as exc_info:
        raise ImproperConfigurationError("An error occurred due to improper configuration")

    assert str(exc_info.value) == "An error occurred due to improper configuration"

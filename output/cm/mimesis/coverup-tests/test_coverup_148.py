# file mimesis/providers/internet.py:255-263
# lines [262, 263]
# branches []

import pytest
from mimesis.enums import TLDType
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.internet import Internet

def test_top_level_domain_with_invalid_tld_type(mocker):
    internet_provider = Internet()
    invalid_tld_type = "invalid_tld_type"

    with pytest.raises(NonEnumerableError):
        internet_provider.top_level_domain(tld_type=invalid_tld_type)

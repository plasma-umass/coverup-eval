# file mimesis/providers/internet.py:238-253
# lines [238, 247, 248, 249, 252, 253]
# branches []

import pytest
from mimesis.providers.internet import Internet
from mimesis.enums import TLDType

@pytest.fixture
def internet():
    return Internet()

def test_home_page_default_tld(internet):
    result = internet.home_page()
    assert result.startswith('https://')
    assert '.' in result.split('//')[1]

def test_home_page_specific_tld(internet, mocker):
    mocker.patch('mimesis.providers.internet.Internet.top_level_domain', return_value='.com')
    result = internet.home_page(tld_type=TLDType.CCTLD)
    assert result.startswith('https://')
    assert result.endswith('.com')
    assert '.' in result.split('//')[1]

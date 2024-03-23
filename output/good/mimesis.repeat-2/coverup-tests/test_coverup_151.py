# file mimesis/providers/internet.py:69-77
# lines [69, 77]
# branches []

import pytest
from mimesis.providers.internet import Internet

@pytest.fixture
def internet_provider(mocker):
    provider = Internet()
    mocker.patch.object(provider.random, 'choice', side_effect=lambda x: x[0])
    return provider

def test_http_status_code(internet_provider):
    # We need to ensure that the first element of the mocked HTTP_STATUS_CODES is returned
    # since we mocked random.choice to return the first element of its input list.
    # Since the actual HTTP_STATUS_CODES list is not accessible, we will mock it as well.
    mocked_status_codes = [100, 200, 300, 400, 500]
    internet_provider.HTTP_STATUS_CODES = mocked_status_codes
    status_code = internet_provider.http_status_code()
    assert status_code == mocked_status_codes[0]

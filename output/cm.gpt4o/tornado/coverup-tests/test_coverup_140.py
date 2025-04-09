# file tornado/locale.py:219-221
# lines [219, 221]
# branches []

import pytest
from unittest import mock
from tornado.locale import get_supported_locales

@pytest.fixture
def mock_supported_locales():
    with mock.patch('tornado.locale._supported_locales', new=['en_US', 'es_ES', 'fr_FR']):
        yield

def test_get_supported_locales(mock_supported_locales):
    supported_locales = get_supported_locales()
    assert supported_locales == ['en_US', 'es_ES', 'fr_FR']

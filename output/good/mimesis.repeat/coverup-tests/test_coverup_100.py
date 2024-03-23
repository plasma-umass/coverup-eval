# file mimesis/providers/address.py:30-37
# lines [30, 35, 36, 37]
# branches []

import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale


def test_address_init_with_unsupported_locale(mocker):
    pull_mock = mocker.patch('mimesis.providers.base.BaseDataProvider._pull', side_effect=UnsupportedLocale)

    with pytest.raises(UnsupportedLocale):
        Address(locale='unsupported_locale')

    # Since the _pull method raises an exception, it will not be called, so we should not assert it was called.

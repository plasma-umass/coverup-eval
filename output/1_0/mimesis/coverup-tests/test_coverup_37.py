# file mimesis/providers/transport.py:85-94
# lines [85, 91, 92, 94]
# branches ['91->92', '91->94']

import pytest
from mimesis.providers.transport import Transport
from mimesis.exceptions import NonEnumerableError

# Assuming VRC_BY_LOCALES and VR_CODES are defined somewhere in the module
# If not, they should be defined for the test to work

def test_vehicle_registration_code_with_locale(mocker):
    # Mock the VRC_BY_LOCALES dictionary to control the test environment
    mocker.patch(
        'mimesis.providers.transport.VRC_BY_LOCALES',
        {'US': 'USA', 'UK': 'GB'}
    )

    transport = Transport()

    # Test with a known locale
    code = transport.vehicle_registration_code(locale='US')
    assert code == 'USA'

    # Test with a locale that does not exist in the dictionary
    with pytest.raises(KeyError):
        transport.vehicle_registration_code(locale='XX')

def test_vehicle_registration_code_without_locale(mocker):
    # Mock the VR_CODES list to control the test environment
    mocker.patch(
        'mimesis.providers.transport.VR_CODES',
        ['USA', 'GB']
    )

    transport = Transport()

    # Test without specifying a locale
    code = transport.vehicle_registration_code()
    assert code in ['USA', 'GB']

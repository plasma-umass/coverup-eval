# file string_utils/validation.py:247-283
# lines [281]
# branches ['280->281']

import pytest
from string_utils.validation import is_credit_card

def test_is_credit_card_any_type(mocker):
    # Mocking the CREDIT_CARDS dictionary and is_full_string function
    mocker.patch('string_utils.validation.CREDIT_CARDS', {
        'VISA': mocker.Mock(match=mocker.Mock(return_value=None)),
        'MASTERCARD': mocker.Mock(match=mocker.Mock(return_value=None)),
        'AMERICAN_EXPRESS': mocker.Mock(match=mocker.Mock(return_value=None)),
        'DISCOVER': mocker.Mock(match=mocker.Mock(return_value=None)),
        'DINERS_CLUB': mocker.Mock(match=mocker.Mock(return_value=None)),
        'JCB': mocker.Mock(match=mocker.Mock(return_value=None)),
    })
    mocker.patch('string_utils.validation.is_full_string', return_value=True)

    # Test input that should not match any card type
    input_string = '1234567890123456'
    assert is_credit_card(input_string) is False

    # Modify the mock to match AMERICAN_EXPRESS for the next test
    mocker.patch('string_utils.validation.CREDIT_CARDS', {
        'VISA': mocker.Mock(match=mocker.Mock(return_value=None)),
        'MASTERCARD': mocker.Mock(match=mocker.Mock(return_value=None)),
        'AMERICAN_EXPRESS': mocker.Mock(match=mocker.Mock(return_value=True)),
        'DISCOVER': mocker.Mock(match=mocker.Mock(return_value=None)),
        'DINERS_CLUB': mocker.Mock(match=mocker.Mock(return_value=None)),
        'JCB': mocker.Mock(match=mocker.Mock(return_value=None)),
    })

    # Test input that should match AMERICAN_EXPRESS
    input_string = '378282246310005'
    assert is_credit_card(input_string) is True

# file string_utils/validation.py:434-448
# lines [434, 448]
# branches []

import pytest
from string_utils.validation import is_ip

def test_is_ip_v4(mocker):
    mock_is_ip_v4 = mocker.patch('string_utils.validation.is_ip_v4', return_value=True)
    mock_is_ip_v6 = mocker.patch('string_utils.validation.is_ip_v6', return_value=False)
    
    assert is_ip('255.200.100.75') == True
    
    mock_is_ip_v4.assert_called_once_with('255.200.100.75')
    mock_is_ip_v6.assert_called_once_with('255.200.100.75')

def test_is_ip_v6(mocker):
    mock_is_ip_v4 = mocker.patch('string_utils.validation.is_ip_v4', return_value=False)
    mock_is_ip_v6 = mocker.patch('string_utils.validation.is_ip_v6', return_value=True)
    
    assert is_ip('2001:db8:85a3:0000:0000:8a2e:370:7334') == True
    
    mock_is_ip_v4.assert_not_called()
    mock_is_ip_v6.assert_called_once_with('2001:db8:85a3:0000:0000:8a2e:370:7334')

def test_is_ip_invalid(mocker):
    mock_is_ip_v4 = mocker.patch('string_utils.validation.is_ip_v4', return_value=False)
    mock_is_ip_v6 = mocker.patch('string_utils.validation.is_ip_v6', return_value=False)
    
    assert is_ip('1.2.3') == False
    
    mock_is_ip_v4.assert_called_once_with('1.2.3')
    mock_is_ip_v6.assert_called_once_with('1.2.3')

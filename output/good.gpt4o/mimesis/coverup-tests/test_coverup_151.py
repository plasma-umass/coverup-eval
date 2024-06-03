# file mimesis/providers/internet.py:134-142
# lines [134, 142]
# branches []

import pytest
from mimesis.providers.internet import Internet

def test_ip_v6(mocker):
    internet = Internet()
    
    # Mock the ip_v6_object method to ensure it gets called
    mock_ip_v6_object = mocker.patch.object(internet, 'ip_v6_object', return_value='2001:c244:cf9d:1fb1:c56d:f52c:8a04:94f3')
    
    # Call the ip_v6 method
    result = internet.ip_v6()
    
    # Assert that the ip_v6_object method was called
    mock_ip_v6_object.assert_called_once()
    
    # Assert that the result is as expected
    assert result == '2001:c244:cf9d:1fb1:c56d:f52c:8a04:94f3'

# file mimesis/providers/internet.py:59-67
# lines [67]
# branches []

import pytest
from mimesis.providers.internet import Internet

def test_http_status_message(mocker):
    internet = Internet()
    mocker.patch.object(internet.random, 'choice', return_value='200 OK')
    
    result = internet.http_status_message()
    
    assert result == '200 OK'

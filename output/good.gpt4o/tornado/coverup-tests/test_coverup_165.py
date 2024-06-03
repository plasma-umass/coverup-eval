# file tornado/tcpclient.py:198-204
# lines [198, 199]
# branches []

import pytest
from tornado.tcpclient import TCPClient

@pytest.fixture
def mock_tcpclient(mocker):
    mocker.patch('tornado.tcpclient.TCPClient.__init__', return_value=None)
    return TCPClient()

def test_tcpclient_initialization(mock_tcpclient):
    assert isinstance(mock_tcpclient, TCPClient)

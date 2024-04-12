# file tornado/simple_httpclient.py:165-190
# lines [165, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 179, 180, 181, 182, 184, 185, 186, 187, 188, 189]
# branches ['173->174', '173->184', '179->180', '179->184', '186->exit', '186->187']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from unittest.mock import Mock
from tornado.ioloop import IOLoop
from tornado.log import gen_log

@pytest.fixture
def mock_ioloop(mocker):
    loop = mocker.Mock(spec=IOLoop)
    loop.time.return_value = 123.456
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=loop)
    return loop

@pytest.fixture
def mock_logger(mocker):
    mocker.patch.object(gen_log, 'debug')

def test_fetch_impl_queueing(mock_ioloop, mock_logger):
    client = SimpleAsyncHTTPClient(max_clients=1)
    client.active = {object(): None}  # Simulate an active client to trigger queuing

    request = HTTPRequest(url='http://example.com', connect_timeout=10, request_timeout=20)
    callback = Mock()

    client.fetch_impl(request, callback)

    assert len(client.queue) == 1
    assert client.queue[0][1] == request
    assert client.queue[0][2] == callback
    assert mock_ioloop.add_timeout.called
    assert gen_log.debug.called
    assert gen_log.debug.call_args[0][0].startswith("max_clients limit reached")

    # Clean up
    client.close()

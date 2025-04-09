# file: tornado/tcpclient.py:293-328
# asked: {"lines": [303, 304, 305, 308, 312, 313, 315, 316, 317, 318, 320, 321, 322, 323, 324, 325, 326, 328], "branches": [[305, 308], [305, 312], [313, 315], [313, 321]]}
# gained: {"lines": [303, 304, 305, 308, 312, 313, 315, 316, 317, 318, 320, 321, 322, 328], "branches": [[305, 308], [305, 312], [313, 315], [313, 321]]}

import pytest
import socket
from tornado.iostream import IOStream
from tornado.concurrent import Future
from tornado.tcpclient import TCPClient

@pytest.fixture
def tcp_client():
    return TCPClient()

def test_create_stream_no_source_ip_no_source_port(tcp_client, mocker):
    af = socket.AF_INET
    addr = ('127.0.0.1', 8888)
    max_buffer_size = 1024

    mock_connect = mocker.patch.object(IOStream, 'connect', return_value=Future())
    stream, future = tcp_client._create_stream(max_buffer_size, af, addr)
    assert isinstance(stream, IOStream)
    assert future is mock_connect.return_value

def test_create_stream_with_source_port_no_source_ip(tcp_client, mocker):
    af = socket.AF_INET
    addr = ('127.0.0.1', 8888)
    max_buffer_size = 1024
    source_port = 9999

    mock_connect = mocker.patch.object(IOStream, 'connect', return_value=Future())
    stream, future = tcp_client._create_stream(max_buffer_size, af, addr, source_port=source_port)
    assert isinstance(stream, IOStream)
    assert future is mock_connect.return_value

def test_create_stream_with_source_ip_and_port(tcp_client, mocker):
    af = socket.AF_INET
    addr = ('127.0.0.1', 8888)
    max_buffer_size = 1024
    source_ip = '127.0.0.1'
    source_port = 9999

    mock_connect = mocker.patch.object(IOStream, 'connect', return_value=Future())
    stream, future = tcp_client._create_stream(max_buffer_size, af, addr, source_ip=source_ip, source_port=source_port)
    assert isinstance(stream, IOStream)
    assert future is mock_connect.return_value

def test_create_stream_with_ipv6(tcp_client, mocker):
    af = socket.AF_INET6
    addr = ('::1', 8888)
    max_buffer_size = 1024

    mock_connect = mocker.patch.object(IOStream, 'connect', return_value=Future())
    stream, future = tcp_client._create_stream(max_buffer_size, af, addr)
    assert isinstance(stream, IOStream)
    assert future is mock_connect.return_value

def test_create_stream_bind_error(tcp_client, mocker):
    af = socket.AF_INET
    addr = ('127.0.0.1', 8888)
    max_buffer_size = 1024
    source_ip = '127.0.0.1'
    source_port = 9999

    mock_socket = mocker.patch('socket.socket')
    mock_socket.return_value.bind.side_effect = socket.error

    with pytest.raises(socket.error):
        tcp_client._create_stream(max_buffer_size, af, addr, source_ip=source_ip, source_port=source_port)

def test_create_stream_iostream_error(tcp_client, mocker):
    af = socket.AF_INET
    addr = ('127.0.0.1', 8888)
    max_buffer_size = 1024

    mock_iostream = mocker.patch('tornado.iostream.IOStream')
    mock_iostream.side_effect = socket.error

    stream, future = tcp_client._create_stream(max_buffer_size, af, addr)
    assert isinstance(future, Future)
    future.set_exception(socket.error("Test exception"))
    assert future.exception() is not None

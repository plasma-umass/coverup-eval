# file: lib/ansible/module_utils/connection.py:75-90
# asked: {"lines": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[78, 79], [78, 83], [80, 81], [80, 82], [85, 86], [85, 90], [87, 88], [87, 89]]}
# gained: {"lines": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[78, 79], [78, 83], [80, 81], [80, 82], [85, 86], [85, 90], [87, 88], [87, 89]]}

import pytest
import socket
import struct
from unittest import mock

# Assuming the function recv_data is part of a module named connection
from ansible.module_utils.connection import recv_data

def test_recv_data_complete(monkeypatch):
    # Mock socket to return a complete header and data
    mock_socket = mock.Mock()
    header = struct.pack('!Q', 4)  # data length is 4 bytes
    data = b'test'
    mock_socket.recv = mock.Mock(side_effect=[header, data])

    result = recv_data(mock_socket)
    assert result == data

def test_recv_data_incomplete_header(monkeypatch):
    # Mock socket to return an incomplete header
    mock_socket = mock.Mock()
    mock_socket.recv = mock.Mock(side_effect=[b'\x00\x00\x00\x00', b''])

    result = recv_data(mock_socket)
    assert result is None

def test_recv_data_incomplete_data(monkeypatch):
    # Mock socket to return a complete header but incomplete data
    mock_socket = mock.Mock()
    header = struct.pack('!Q', 4)  # data length is 4 bytes
    mock_socket.recv = mock.Mock(side_effect=[header, b'te', b''])

    result = recv_data(mock_socket)
    assert result is None

def test_recv_data_partial_reads(monkeypatch):
    # Mock socket to return data in multiple small reads
    mock_socket = mock.Mock()
    header = struct.pack('!Q', 4)  # data length is 4 bytes
    data = b'test'
    mock_socket.recv = mock.Mock(side_effect=[header[:4], header[4:], data[:2], data[2:]])

    result = recv_data(mock_socket)
    assert result == data

def test_recv_data_empty_socket(monkeypatch):
    # Mock socket to return nothing
    mock_socket = mock.Mock()
    mock_socket.recv = mock.Mock(return_value=b'')

    result = recv_data(mock_socket)
    assert result is None

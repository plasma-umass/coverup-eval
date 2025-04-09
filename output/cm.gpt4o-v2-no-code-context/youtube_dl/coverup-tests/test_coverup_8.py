# file: youtube_dl/downloader/ism.py:39-40
# asked: {"lines": [39, 40], "branches": []}
# gained: {"lines": [39, 40], "branches": []}

import pytest
from youtube_dl.downloader.ism import full_box
import struct

def test_full_box(monkeypatch):
    # Mocking the box function to verify it is called with the correct parameters
    def mock_box(box_type, data):
        return (box_type, data)
    
    monkeypatch.setattr('youtube_dl.downloader.ism.box', mock_box)
    
    box_type = 'test'
    version = 1
    flags = 0x123456
    payload = b'payload_data'
    
    result = full_box(box_type, version, flags, payload)
    
    expected_data = struct.pack('>B', version) + struct.pack('>I', flags)[1:] + payload
    assert result == (box_type, expected_data)

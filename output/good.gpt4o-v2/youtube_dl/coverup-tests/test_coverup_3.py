# file: youtube_dl/downloader/ism.py:39-40
# asked: {"lines": [39, 40], "branches": []}
# gained: {"lines": [39, 40], "branches": []}

import pytest
from youtube_dl.downloader.ism import full_box, box
from struct import pack

def test_full_box(monkeypatch):
    def mock_box(box_type, payload):
        return b'\x00\x00\x00\x10' + box_type + payload

    monkeypatch.setattr('youtube_dl.downloader.ism.box', mock_box)

    box_type = b'test'
    version = 1
    flags = 0
    payload = b'data'

    result = full_box(box_type, version, flags, payload)
    expected_payload = pack('>B', version) + pack('>I', flags)[1:] + payload
    expected_result = b'\x00\x00\x00\x10' + box_type + expected_payload

    assert result == expected_result

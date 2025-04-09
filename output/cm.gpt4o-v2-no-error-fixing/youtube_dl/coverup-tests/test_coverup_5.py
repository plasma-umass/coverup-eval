# file: youtube_dl/downloader/ism.py:39-40
# asked: {"lines": [39, 40], "branches": []}
# gained: {"lines": [39, 40], "branches": []}

import pytest
from youtube_dl.downloader.ism import full_box

def test_full_box(monkeypatch):
    class MockU8:
        @staticmethod
        def pack(value):
            return bytes([value])

    class MockU32:
        @staticmethod
        def pack(value):
            return value.to_bytes(4, byteorder='big')

    def mock_box(box_type, payload):
        return MockU32.pack(8 + len(payload)) + box_type + payload

    monkeypatch.setattr('youtube_dl.downloader.ism.u8', MockU8)
    monkeypatch.setattr('youtube_dl.downloader.ism.u32', MockU32)
    monkeypatch.setattr('youtube_dl.downloader.ism.box', mock_box)

    box_type = b'test'
    version = 1
    flags = 0x123456
    payload = b'data'

    result = full_box(box_type, version, flags, payload)
    expected_payload = MockU8.pack(version) + MockU32.pack(flags)[1:] + payload
    expected_result = mock_box(box_type, expected_payload)

    assert result == expected_result

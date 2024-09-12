# file: youtube_dl/downloader/ism.py:43-190
# asked: {"lines": [44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 101, 102, 103, 104, 106, 107, 108, 109, 111, 112, 113, 114, 116, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 160, 162, 163, 165, 166, 168, 169, 171, 173, 175, 177, 179, 180, 182, 183, 184, 185, 186, 187, 189, 190], "branches": [[101, 102], [101, 106], [120, 121], [120, 131], [128, 129], [128, 158], [145, 146], [145, 158]]}
# gained: {"lines": [44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 101, 102, 103, 104, 106, 107, 108, 109, 111, 112, 113, 114, 116, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 160, 162, 163, 165, 166, 168, 169, 171, 173, 175, 177, 179, 180, 182, 183, 184, 185, 186, 187, 189, 190], "branches": [[101, 102], [101, 106], [120, 121], [120, 131], [128, 129], [145, 146]]}

import pytest
import io
import time
import binascii

# Mocking the required functions and constants
u32 = u64 = s1616 = s88 = u16 = u8 = u1616 = lambda x: x
unity_matrix = b'\x00' * 36
TRACK_ENABLED = 1
TRACK_IN_MOVIE = 2
TRACK_IN_PREVIEW = 4
SELF_CONTAINED = 1

def box(type, payload):
    return type + payload

def full_box(type, version, flags, payload):
    return type + payload

from youtube_dl.downloader.ism import write_piff_header

@pytest.fixture
def mock_time(monkeypatch):
    mock_time = 1609459200  # Fixed timestamp for testing
    monkeypatch.setattr(time, 'time', lambda: mock_time)
    yield mock_time

def test_write_piff_header_audio(mock_time):
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'AACL',
        'duration': 1000,
        'timescale': 1000,
        'language': 'eng',
        'height': 0,
        'width': 0,
        'channels': 2,
        'bits_per_sample': 16,
        'sampling_rate': 44100
    }
    write_piff_header(stream, params)
    result = stream.getvalue()
    assert b'ftyp' in result
    assert b'moov' in result

def test_write_piff_header_video(mock_time):
    stream = io.BytesIO()
    params = {
        'track_id': 1,
        'fourcc': 'H264',
        'duration': 1000,
        'timescale': 1000,
        'language': 'eng',
        'height': 1080,
        'width': 1920,
        'codec_private_data': binascii.hexlify(b'\x00\x00\x00\x01sps\x00\x00\x00\x01pps').decode('utf-8'),
        'nal_unit_length_field': 4
    }
    write_piff_header(stream, params)
    result = stream.getvalue()
    assert b'ftyp' in result
    assert b'moov' in result
    assert b'avc1' in result

# file: youtube_dl/downloader/f4m.py:184-185
# asked: {"lines": [185], "branches": []}
# gained: {"lines": [185], "branches": []}

import pytest
from youtube_dl.downloader.f4m import read_bootstrap_info, FlvReader

class MockFlvReader(FlvReader):
    def read_box_info(self):
        return (1, b'abst', b'data')

    def read_abst(self):
        return 'bootstrap_info'

def test_read_bootstrap_info(monkeypatch):
    def mock_flv_reader_init(self, bootstrap_bytes):
        pass

    monkeypatch.setattr(FlvReader, '__init__', mock_flv_reader_init)
    monkeypatch.setattr(FlvReader, 'read_box_info', MockFlvReader.read_box_info)
    monkeypatch.setattr(FlvReader, 'read_abst', MockFlvReader.read_abst)

    bootstrap_bytes = b'some_bytes'
    result = read_bootstrap_info(bootstrap_bytes)
    assert result == 'bootstrap_info'

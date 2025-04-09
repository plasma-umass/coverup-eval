# file: youtube_dl/extractor/linuxacademy.py:69-70
# asked: {"lines": [69, 70], "branches": []}
# gained: {"lines": [69, 70], "branches": []}

import pytest
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE
from youtube_dl.utils import ExtractorError

class MockInfoExtractor:
    def _get_login_info(self):
        return 'username', 'password'
    
    def _download_webpage_handle(self, *args, **kwargs):
        return '<html></html>', MockUrlHandle()
    
    def _parse_json(self, *args, **kwargs):
        return {'extraParams': {}}
    
    def _search_regex(self, *args, **kwargs):
        return 'eyJleHRyYVBhcmFtcyI6eyJjbGllbnRfaWQiOiJjbGllbnQtaWQifX0='
    
    def _download_webpage(self, *args, **kwargs):
        return '<html></html>'
    
    def _hidden_inputs(self, *args, **kwargs):
        return {}
    
    def _search_regex(self, *args, **kwargs):
        return 'access_token=mock_access_token'
    
class MockUrlHandle:
    def geturl(self):
        return 'https://login.linuxacademy.com/callback?access_token=mock_access_token'

@pytest.fixture
def mock_linuxacademy_ie(monkeypatch):
    ie = LinuxAcademyIE()
    monkeypatch.setattr(ie, '_get_login_info', MockInfoExtractor()._get_login_info)
    monkeypatch.setattr(ie, '_download_webpage_handle', MockInfoExtractor()._download_webpage_handle)
    monkeypatch.setattr(ie, '_parse_json', MockInfoExtractor()._parse_json)
    monkeypatch.setattr(ie, '_search_regex', MockInfoExtractor()._search_regex)
    monkeypatch.setattr(ie, '_download_webpage', MockInfoExtractor()._download_webpage)
    monkeypatch.setattr(ie, '_hidden_inputs', MockInfoExtractor()._hidden_inputs)
    return ie

def test_real_initialize(mock_linuxacademy_ie):
    mock_linuxacademy_ie._real_initialize()
    assert True  # If no exception is raised, the test passes

def test_login(mock_linuxacademy_ie):
    mock_linuxacademy_ie._login()
    assert True  # If no exception is raised, the test passes

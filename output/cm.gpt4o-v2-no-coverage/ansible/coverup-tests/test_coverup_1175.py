# file: lib/ansible/modules/apt_repository.py:249-278
# asked: {"lines": [263, 264, 276], "branches": [[262, 263], [269, 275], [271, 275], [275, 276]]}
# gained: {"lines": [263, 264, 276], "branches": [[262, 263], [271, 275], [275, 276]]}

import pytest
from ansible.modules.apt_repository import SourcesList, InvalidSource

VALID_SOURCE_TYPES = ['deb', 'deb-src']

class MockModule:
    def __init__(self):
        pass

@pytest.fixture
def sources_list(monkeypatch):
    def mock_apt_cfg_file(filespec):
        return "/dev/null"
    
    def mock_apt_cfg_dir(dirspec):
        return "/dev/null"
    
    monkeypatch.setattr(SourcesList, "_apt_cfg_file", staticmethod(mock_apt_cfg_file))
    monkeypatch.setattr(SourcesList, "_apt_cfg_dir", staticmethod(mock_apt_cfg_dir))
    
    return SourcesList(MockModule())

def test_parse_valid_source(sources_list):
    line = "deb http://archive.ubuntu.com/ubuntu/ focal main restricted"
    valid, enabled, source, comment = sources_list._parse(line)
    assert valid is True
    assert enabled is True
    assert source == "deb http://archive.ubuntu.com/ubuntu/ focal main restricted"
    assert comment == ""

def test_parse_commented_source(sources_list):
    line = "#deb http://archive.ubuntu.com/ubuntu/ focal main restricted"
    valid, enabled, source, comment = sources_list._parse(line)
    assert valid is True
    assert enabled is False
    assert source == "deb http://archive.ubuntu.com/ubuntu/ focal main restricted"
    assert comment == ""

def test_parse_source_with_inline_comment(sources_list):
    line = "deb http://archive.ubuntu.com/ubuntu/ focal main restricted # main repository"
    valid, enabled, source, comment = sources_list._parse(line)
    assert valid is True
    assert enabled is True
    assert source == "deb http://archive.ubuntu.com/ubuntu/ focal main restricted"
    assert comment == "main repository"

def test_parse_invalid_source(sources_list):
    line = "invalid http://archive.ubuntu.com/ubuntu/ focal main restricted"
    valid, enabled, source, comment = sources_list._parse(line)
    assert valid is False
    assert enabled is True
    assert source == "invalid http://archive.ubuntu.com/ubuntu/ focal main restricted"
    assert comment == ""

def test_parse_invalid_source_with_exception(sources_list):
    line = "invalid http://archive.ubuntu.com/ubuntu/ focal main restricted"
    with pytest.raises(InvalidSource):
        sources_list._parse(line, raise_if_invalid_or_disabled=True)

def test_parse_commented_invalid_source_with_exception(sources_list):
    line = "#invalid http://archive.ubuntu.com/ubuntu/ focal main restricted"
    with pytest.raises(InvalidSource):
        sources_list._parse(line, raise_if_invalid_or_disabled=True)

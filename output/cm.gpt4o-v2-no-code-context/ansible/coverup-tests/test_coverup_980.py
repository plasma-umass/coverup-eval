# file: lib/ansible/utils/color.py:104-112
# asked: {"lines": [105, 106, 107, 108, 109, 111, 112], "branches": [[105, 106], [105, 112], [106, 107], [106, 108], [108, 109], [108, 111]]}
# gained: {"lines": [105, 106, 107, 108, 109, 111, 112], "branches": [[105, 106], [105, 112], [106, 107], [106, 108], [108, 109], [108, 111]]}

import pytest
from ansible.utils.color import hostcolor
from ansible import constants as C
from ansible.utils.color import stringc

@pytest.fixture
def mock_constants(monkeypatch):
    class MockConstants:
        COLOR_ERROR = 'red'
        COLOR_CHANGED = 'yellow'
        COLOR_OK = 'green'
    
    monkeypatch.setattr(C, 'COLOR_ERROR', MockConstants.COLOR_ERROR)
    monkeypatch.setattr(C, 'COLOR_CHANGED', MockConstants.COLOR_CHANGED)
    monkeypatch.setattr(C, 'COLOR_OK', MockConstants.COLOR_OK)

def test_hostcolor_failures(mock_constants, monkeypatch):
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)
    host = "test_host"
    stats = {'failures': 1, 'unreachable': 0, 'changed': 0}
    result = hostcolor(host, stats, color=True)
    expected = u"%-37s" % stringc(host, C.COLOR_ERROR)
    assert result == expected

def test_hostcolor_unreachable(mock_constants, monkeypatch):
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)
    host = "test_host"
    stats = {'failures': 0, 'unreachable': 1, 'changed': 0}
    result = hostcolor(host, stats, color=True)
    expected = u"%-37s" % stringc(host, C.COLOR_ERROR)
    assert result == expected

def test_hostcolor_changed(mock_constants, monkeypatch):
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)
    host = "test_host"
    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    result = hostcolor(host, stats, color=True)
    expected = u"%-37s" % stringc(host, C.COLOR_CHANGED)
    assert result == expected

def test_hostcolor_ok(mock_constants, monkeypatch):
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', True)
    host = "test_host"
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    result = hostcolor(host, stats, color=True)
    expected = u"%-37s" % stringc(host, C.COLOR_OK)
    assert result == expected

def test_hostcolor_no_color(mock_constants, monkeypatch):
    monkeypatch.setattr('ansible.utils.color.ANSIBLE_COLOR', False)
    host = "test_host"
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    result = hostcolor(host, stats, color=True)
    expected = u"%-26s" % host
    assert result == expected

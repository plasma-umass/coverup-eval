# file: lib/ansible/playbook/playbook_include.py:47-49
# asked: {"lines": [47, 48, 49], "branches": []}
# gained: {"lines": [47, 48, 49], "branches": []}

import pytest
from ansible.playbook.playbook_include import PlaybookInclude
from unittest.mock import Mock

@pytest.fixture
def mock_base_class(monkeypatch):
    mock_base = Mock()
    monkeypatch.setattr('ansible.playbook.playbook_include.Base', mock_base)
    return mock_base

@pytest.fixture
def mock_conditional_class(monkeypatch):
    mock_conditional = Mock()
    monkeypatch.setattr('ansible.playbook.playbook_include.Conditional', mock_conditional)
    return mock_conditional

@pytest.fixture
def mock_taggable_class(monkeypatch):
    mock_taggable = Mock()
    monkeypatch.setattr('ansible.playbook.playbook_include.Taggable', mock_taggable)
    return mock_taggable

@pytest.fixture
def playbook_include(mock_base_class, mock_conditional_class, mock_taggable_class):
    return PlaybookInclude()

def test_load_method(playbook_include, mocker):
    data = {'key': 'value'}
    basedir = '/some/path'
    variable_manager = mocker.Mock()
    loader = mocker.Mock()

    mock_load_data = mocker.patch.object(PlaybookInclude, 'load_data', return_value='loaded_data')

    result = PlaybookInclude.load(data, basedir, variable_manager, loader)

    mock_load_data.assert_called_once_with(ds=data, basedir=basedir, variable_manager=variable_manager, loader=loader)
    assert result == 'loaded_data'

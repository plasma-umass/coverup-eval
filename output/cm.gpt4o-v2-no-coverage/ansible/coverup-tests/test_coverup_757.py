# file: lib/ansible/cli/doc.py:515-517
# asked: {"lines": [515, 516, 517], "branches": []}
# gained: {"lines": [515, 516, 517], "branches": []}

import pytest
from unittest.mock import patch, mock_open
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_pkgutil(monkeypatch):
    mock_data = b"keywords: ['keyword1', 'keyword2']"
    monkeypatch.setattr('pkgutil.get_data', lambda *args, **kwargs: mock_data)

def test_list_keywords(mock_pkgutil):
    result = DocCLI._list_keywords()
    assert result == {'keywords': ['keyword1', 'keyword2']}

# file: lib/ansible/playbook/block.py:105-117
# asked: {"lines": [105, 111, 112, 113, 115, 117], "branches": [[111, 112], [111, 117], [112, 113], [112, 115]]}
# gained: {"lines": [105, 111, 112, 113, 115, 117], "branches": [[111, 112], [111, 117], [112, 113], [112, 115]]}

import pytest
from ansible.playbook.block import Block

class MockBase:
    def preprocess_data(self, ds):
        return ds

@pytest.fixture
def mock_base(monkeypatch):
    monkeypatch.setattr("ansible.playbook.block.Base", MockBase)

def test_preprocess_data_with_non_block_dict(mock_base):
    block = Block()
    ds = {"key": "value"}
    result = block.preprocess_data(ds)
    assert result == {"block": [{"key": "value"}]}

def test_preprocess_data_with_list(mock_base):
    block = Block()
    ds = [{"key": "value"}]
    result = block.preprocess_data(ds)
    assert result == {"block": [{"key": "value"}]}

def test_preprocess_data_with_non_list(mock_base):
    block = Block()
    ds = {"key": "value"}
    result = block.preprocess_data(ds)
    assert result == {"block": [{"key": "value"}]}

def test_preprocess_data_with_block(mock_base):
    block = Block()
    ds = {"block": [{"key": "value"}]}
    result = block.preprocess_data(ds)
    assert result == {"block": [{"key": "value"}]}

# file: src/blib2to3/pytree.py:800-809
# asked: {"lines": [800, 802, 803, 804, 805, 806, 807, 808, 809], "branches": [[802, 803], [802, 809], [803, 802], [803, 804], [804, 805], [804, 808], [806, 807], [806, 808]]}
# gained: {"lines": [800, 802, 803, 804, 805, 806, 807, 808, 809], "branches": [[802, 803], [802, 809], [803, 802], [803, 804], [804, 805], [804, 808], [806, 807]]}

import pytest
from blib2to3.pytree import WildcardPattern

class MockNode:
    pass

@pytest.fixture
def mock_nodes():
    return [MockNode(), MockNode()]

@pytest.fixture
def wildcard_pattern():
    content = [['a'], ['b']]
    return WildcardPattern(content=content, min=1, max=2, name="test")

def test_match_seq_no_results(mock_nodes, wildcard_pattern, mocker):
    mocker.patch.object(wildcard_pattern, 'generate_matches', return_value=[(2, {})])
    assert wildcard_pattern.match_seq(mock_nodes) is True

def test_match_seq_with_results(mock_nodes, wildcard_pattern, mocker):
    mocker.patch.object(wildcard_pattern, 'generate_matches', return_value=[(2, {'key': 'value'})])
    results = {}
    assert wildcard_pattern.match_seq(mock_nodes, results) is True
    assert results == {'key': 'value', 'test': mock_nodes}

def test_match_seq_no_match(mock_nodes, wildcard_pattern, mocker):
    mocker.patch.object(wildcard_pattern, 'generate_matches', return_value=[(1, {})])
    assert wildcard_pattern.match_seq(mock_nodes) is False

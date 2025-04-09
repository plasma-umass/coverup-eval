# file src/blib2to3/pytree.py:902-914
# lines [904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914]
# branches ['905->906', '905->907', '907->exit', '907->908', '908->exit', '908->909', '909->908', '909->910', '910->909', '910->911']

import pytest
from blib2to3.pytree import BasePattern, WildcardPattern
from typing import Iterator, Tuple

class MockPattern(BasePattern):
    def generate_matches(self, alt, nodes):
        yield 1, {}

@pytest.fixture
def mock_generate_matches(mocker):
    return mocker.patch('blib2to3.pytree.generate_matches', side_effect=MockPattern().generate_matches)

def test_wildcard_pattern_recursive_matches(mock_generate_matches):
    class TestWildcardPattern(WildcardPattern):
        def __init__(self, content, min, max):
            self.content = content
            self.min = min
            self.max = max

    pattern = TestWildcardPattern(content=[1], min=0, max=2)
    nodes = [1, 2, 3]
    count = 0

    matches = list(pattern._recursive_matches(nodes, count))

    assert matches == [(0, {}), (1, {}), (2, {})]

    mock_generate_matches.assert_called()

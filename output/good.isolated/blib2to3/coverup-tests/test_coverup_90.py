# file src/blib2to3/pytree.py:582-590
# lines []
# branches ['589->exit']

import pytest
from blib2to3.pytree import BasePattern
from typing import List, Tuple, Iterator

class DummyPattern(BasePattern):
    def match(self, node, results):
        return False

@pytest.fixture
def cleanup():
    # Setup if necessary
    yield
    # Cleanup if necessary

def test_base_pattern_generate_matches_no_match(cleanup):
    pattern = DummyPattern()
    nodes = ['node1']
    matches = list(pattern.generate_matches(nodes))
    assert matches == []


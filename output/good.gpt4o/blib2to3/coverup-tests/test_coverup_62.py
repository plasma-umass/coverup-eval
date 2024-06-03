# file src/blib2to3/pytree.py:641-644
# lines [641, 643]
# branches []

import pytest
from blib2to3.pytree import BasePattern

def test_nodepattern_wildcards():
    class NodePattern(BasePattern):
        wildcards: bool = False

    # Create an instance of NodePattern
    node_pattern_instance = NodePattern()

    # Assert that the wildcards attribute is set to False
    assert node_pattern_instance.wildcards == False

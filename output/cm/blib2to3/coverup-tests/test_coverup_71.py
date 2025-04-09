# file src/blib2to3/pytree.py:641-644
# lines [641, 643]
# branches []

import pytest
from blib2to3.pytree import NodePattern

# Corrected test function that provides the required arguments to NodePattern
def test_node_pattern_wildcards():
    # Instantiate NodePattern with a type argument and an empty content list
    node_pattern = NodePattern(type=256, content=[])
    
    # Check if the wildcards attribute is set to False by default
    assert not node_pattern.wildcards, "The wildcards attribute should be False by default"

    # Now set the wildcards attribute to True and check
    node_pattern.wildcards = True
    assert node_pattern.wildcards, "The wildcards attribute should be able to be set to True"

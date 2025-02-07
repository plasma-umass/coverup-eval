# file: src/blib2to3/pytree.py:885-900
# asked: {"lines": [885, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900], "branches": [[891, 892], [891, 898], [893, 891], [893, 894], [894, 893], [894, 895]]}
# gained: {"lines": [885, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900], "branches": [[891, 892], [891, 898], [893, 891], [893, 894], [894, 893], [894, 895]]}

import pytest
from blib2to3.pytree import WildcardPattern, LeafPattern

class MockLeafPattern:
    def match(self, node, results):
        return node == "match"

def test_bare_name_matches():
    # Setup
    content = [[MockLeafPattern()]]
    pattern = WildcardPattern(content=content, name="test")
    nodes = ["match", "no_match", "match"]

    # Execute
    count, results = pattern._bare_name_matches(nodes)

    # Verify
    assert count == 1
    assert results == {"test": ["match"]}

    # Cleanup
    del pattern
    del nodes
    del content

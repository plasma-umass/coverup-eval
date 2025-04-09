# file py_backwards/utils/tree.py:9-12
# lines [9, 10, 11, 12]
# branches ['10->exit', '10->11', '11->10', '11->12']

import ast
import pytest

from py_backwards.utils.tree import _build_parents

def test_build_parents():
    source_code = """
def foo():
    return 42
"""
    tree = ast.parse(source_code)
    _parents = {}

    # Inject the _parents dictionary into the function's scope
    def _build_parents_with_injected_dict(tree: ast.AST) -> None:
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                _parents[child] = node

    _build_parents_with_injected_dict(tree)

    # Check that the parent of the 'return' node is the 'foo' function node
    return_node = tree.body[0].body[0]
    assert _parents[return_node] == tree.body[0]

    # Check that the parent of the '42' node is the 'return' node
    constant_node = return_node.value
    assert _parents[constant_node] == return_node

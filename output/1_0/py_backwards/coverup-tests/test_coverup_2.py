# file py_backwards/transformers/functions_annotations.py:5-24
# lines [17, 18, 19, 22, 23, 24]
# branches []

import ast
from py_backwards.transformers.functions_annotations import FunctionsAnnotationsTransformer

def test_functions_annotations_transformer(mocker):
    # Create a dummy ast tree
    dummy_tree = ast.parse("")

    # Initialize the transformer with the dummy tree
    transformer = FunctionsAnnotationsTransformer(tree=dummy_tree)

    # Mock the _tree_changed attribute to track changes
    mocker.spy(transformer, '_tree_changed')

    # Create a function definition with annotations
    func_def = ast.FunctionDef(
        name='test_func',
        args=ast.arguments(
            args=[ast.arg(arg='x', annotation=ast.Name(id='int', ctx=ast.Load()))],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[ast.Pass()],
        decorator_list=[],
        returns=ast.Name(id='int', ctx=ast.Load())
    )

    # Visit the function definition
    transformer.visit_FunctionDef(func_def)

    # Check if the transformer marked the tree as changed
    assert transformer._tree_changed

    # Check if the return annotation was removed
    assert func_def.returns is None

    # Visit the argument
    transformer.visit_arg(func_def.args.args[0])

    # Check if the transformer marked the tree as changed
    assert transformer._tree_changed

    # Check if the argument annotation was removed
    assert func_def.args.args[0].annotation is None

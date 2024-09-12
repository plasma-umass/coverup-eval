# file: py_backwards/compiler.py:15-51
# asked: {"lines": [32, 33, 34, 40, 41, 42, 44, 45, 46, 47, 48, 49], "branches": [[36, 40]]}
# gained: {"lines": [32, 33, 34, 40, 41, 42, 44, 45, 46, 47, 48, 49], "branches": [[36, 40]]}

import pytest
from py_backwards.compiler import _transform
from py_backwards.exceptions import TransformationError
from unittest.mock import patch, MagicMock

def test_transformer_raises_transformation_error():
    path = "test.py"
    code = "print('Hello, world!')"
    target = (3, 6)  # CompilationTarget is a tuple

    mock_transformer = MagicMock()
    mock_transformer.target = (3, 7)
    mock_transformer.transform.side_effect = Exception("Transformation failed")

    with patch('py_backwards.compiler.transformers', [mock_transformer]):
        with pytest.raises(TransformationError) as excinfo:
            _transform(path, code, target)
        assert excinfo.value.filename == path
        assert excinfo.value.transformer == mock_transformer
        assert "Transformation failed" in excinfo.value.traceback

def test_unparse_raises_transformation_error():
    path = "test.py"
    code = "print('Hello, world!')"
    target = (3, 6)  # CompilationTarget is a tuple

    mock_transformer = MagicMock()
    mock_transformer.target = (3, 7)
    mock_transformer.transform.return_value.tree_changed = True
    mock_transformer.transform.return_value.dependencies = []

    with patch('py_backwards.compiler.transformers', [mock_transformer]):
        with patch('py_backwards.compiler.unparse', side_effect=Exception("Unparsing failed")):
            with pytest.raises(TransformationError) as excinfo:
                _transform(path, code, target)
            assert excinfo.value.filename == path
            assert excinfo.value.transformer == mock_transformer
            assert "Unparsing failed" in excinfo.value.traceback

def test_transformer_tree_not_changed():
    path = "test.py"
    code = "print('Hello, world!')"
    target = (3, 6)  # CompilationTarget is a tuple

    mock_transformer = MagicMock()
    mock_transformer.target = (3, 7)
    mock_transformer.transform.return_value.tree_changed = False

    with patch('py_backwards.compiler.transformers', [mock_transformer]):
        result_code, dependencies = _transform(path, code, target)
        assert result_code.strip() == code.strip()  # Strip to ignore trailing newlines
        assert dependencies == []

def test_transformer_tree_changed():
    path = "test.py"
    code = "print('Hello, world!')"
    target = (3, 6)  # CompilationTarget is a tuple

    mock_transformer = MagicMock()
    mock_transformer.target = (3, 7)
    mock_transformer.transform.return_value.tree_changed = True
    mock_transformer.transform.return_value.dependencies = ["dependency"]

    with patch('py_backwards.compiler.transformers', [mock_transformer]):
        result_code, dependencies = _transform(path, code, target)
        assert "print('Hello, world!')" in result_code
        assert dependencies == ["dependency"]

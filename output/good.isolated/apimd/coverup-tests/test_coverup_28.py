# file apimd/loader.py:63-76
# lines [63, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]
# branches ['71->72', '71->76']

import pytest
from unittest.mock import MagicMock, patch
from importlib.util import spec_from_file_location, module_from_spec
from importlib.abc import Loader
from apimd.loader import _load_module

class MockLoader(Loader):
    def exec_module(self, module):
        pass

@pytest.fixture
def parser_mock(mocker):
    parser = mocker.MagicMock()
    parser.load_docstring = MagicMock()
    return parser

def test_load_module_success(parser_mock, tmp_path):
    module_name = "test_module"
    module_path = tmp_path / "test_module.py"
    module_path.write_text("# Test module content")

    with patch('apimd.loader.spec_from_file_location') as mock_spec, \
         patch('apimd.loader.module_from_spec') as mock_module_from_spec, \
         patch('builtins.__import__', MagicMock()):
        mock_spec.return_value = MagicMock(loader=MockLoader())
        mock_module_from_spec.return_value = MagicMock()
        assert _load_module(module_name, str(module_path), parser_mock)
        parser_mock.load_docstring.assert_called_once_with(module_name, mock_module_from_spec.return_value)

def test_load_module_import_error(parser_mock, tmp_path):
    module_name = "test_module"
    module_path = tmp_path / "test_module.py"
    module_path.write_text("# Test module content")

    with patch('builtins.__import__', side_effect=ImportError):
        assert not _load_module(module_name, str(module_path), parser_mock)

def test_load_module_spec_none(parser_mock, tmp_path):
    module_name = "test_module"
    module_path = tmp_path / "test_module.py"
    module_path.write_text("# Test module content")

    with patch('apimd.loader.spec_from_file_location') as mock_spec:
        mock_spec.return_value = None
        assert not _load_module(module_name, str(module_path), parser_mock)

def test_load_module_loader_not_instance_of_loader(parser_mock, tmp_path):
    module_name = "test_module"
    module_path = tmp_path / "test_module.py"
    module_path.write_text("# Test module content")

    with patch('apimd.loader.spec_from_file_location') as mock_spec:
        mock_spec.return_value = MagicMock(loader=object())
        assert not _load_module(module_name, str(module_path), parser_mock)

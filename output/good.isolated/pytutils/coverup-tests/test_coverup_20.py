# file pytutils/lazy/lazy_import.py:320-324
# lines [320, 322, 323, 324]
# branches ['322->exit', '322->323']

import pytest
from unittest.mock import MagicMock

# Assuming pytutils.lazy.lazy_import.ImportProcessor exists and is the class we are testing
from pytutils.lazy.lazy_import import ImportProcessor

@pytest.fixture
def import_processor():
    return ImportProcessor()

@pytest.fixture
def scope():
    return {}

def test_convert_imports(import_processor, scope, mocker):
    # Mock iteritems to return a dictionary that will be used in the loop
    mock_imports = {
        'name1': ('module.path1', 'member1', 'children1'),
        'name2': ('module.path2', 'member2', 'children2'),
    }
    import_processor.imports = MagicMock()
    import_processor.imports.iteritems.return_value = mock_imports.items()

    # Mock _lazy_import_class to verify it is called with correct arguments
    import_processor._lazy_import_class = MagicMock()

    # Call the method under test
    import_processor._convert_imports(scope)

    # Assert _lazy_import_class was called for each item in mock_imports
    assert import_processor._lazy_import_class.call_count == len(mock_imports)
    import_processor._lazy_import_class.assert_any_call(scope, name='name1', module_path='module.path1', member='member1', children='children1')
    import_processor._lazy_import_class.assert_any_call(scope, name='name2', module_path='module.path2', member='member2', children='children2')

    # Clean up by removing the mocks
    del import_processor.imports
    del import_processor._lazy_import_class

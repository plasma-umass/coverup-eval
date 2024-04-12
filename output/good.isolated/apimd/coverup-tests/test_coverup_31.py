# file apimd/parser.py:326-339
# lines [328, 329, 330, 331, 332, 333, 334, 336, 337, 338, 339]
# branches ['328->329', '328->332', '329->exit', '329->330', '332->exit', '332->333', '333->334', '333->336', '337->exit', '337->338']

import pytest
from apimd.parser import Parser
from ast import Import, alias

@pytest.fixture
def parser():
    return Parser()

@pytest.fixture
def cleanup_aliases(parser):
    # Fixture to clean up aliases after the test
    yield
    parser.alias.clear()

def test_imports_with_import_node(parser, cleanup_aliases, mocker):
    # Mock the _m function to just concatenate the arguments with a dot
    mock_m = mocker.patch('apimd.parser._m', side_effect=lambda *args: '.'.join(args))
    # Mock the parent function to return a fixed string
    mock_parent = mocker.patch('apimd.parser.parent', return_value='parent_module')

    # Create an Import node with aliases
    import_node = Import(names=[alias(name='module1', asname=None), alias(name='module2', asname='alias2')])

    # Call the imports method with the Import node
    parser.imports('root', import_node)

    # Assert that the aliases are correctly set
    assert parser.alias['root.module1'] == 'module1'
    assert parser.alias['root.alias2'] == 'module2'

    # Assert that the _m function was called with the correct arguments
    mock_m.assert_has_calls([mocker.call('root', 'module1'), mocker.call('root', 'alias2')])

    # Assert that the parent function was not called
    mock_parent.assert_not_called()

# file lib/ansible/cli/doc.py:439-471
# lines [442, 443, 444, 447, 449, 450, 451, 454, 455, 456, 458, 459, 461, 462, 464, 466, 467, 468, 471]
# branches ['447->449', '447->454', '449->450', '449->471', '455->456', '455->471', '458->459', '458->461', '461->462', '461->464', '466->455', '466->467']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_display_columns(mocker):
    mocker.patch('shutil.get_terminal_size', return_value=(80, 24))

@pytest.fixture
def mock_context(mocker):
    context = mocker.patch('ansible.cli.doc.context')
    context.CLIARGS = {'list_files': False}
    return context

def test_display_plugin_list(mock_display_columns, mock_context):
    args = MagicMock()
    cli = DocCLI(args)
    cli.plugin_list = ['plugin1', 'plugin2', '_deprecated_plugin']
    results = {
        'plugin1': 'This is a description for plugin1.',
        'plugin2': 'This is a description for plugin2.',
        '_deprecated_plugin': 'This is a deprecated plugin.'
    }

    with patch.object(DocCLI, 'tty_ify', side_effect=lambda x: x), \
         patch.object(DocCLI, 'pager') as mock_pager:
        cli.display_plugin_list(results)

        expected_output = [
            "plugin1            This is a description for plugin1.                      ",
            "plugin2            This is a description for plugin2.                      ",
            "\nDEPRECATED:",
            "deprecated_plugin  This is a deprecated plugin.                            "
        ]
        mock_pager.assert_called_once_with("\n".join(expected_output))

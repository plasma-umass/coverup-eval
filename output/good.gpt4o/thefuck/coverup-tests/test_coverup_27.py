# file thefuck/logs.py:93-114
# lines [93, 94, 95, 96, 98, 99, 100, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 114]
# branches ['98->99', '98->114', '107->108', '107->114']

import pytest
from unittest import mock
from thefuck.logs import how_to_configure_alias

@pytest.fixture
def mock_colorama(mocker):
    mocker.patch('thefuck.logs.colorama.Style.BRIGHT', 'BRIGHT')
    mocker.patch('thefuck.logs.colorama.Style.RESET_ALL', 'RESET_ALL')

@pytest.fixture
def mock_color(mocker):
    return mocker.patch('thefuck.logs.color', side_effect=lambda x: x)

def test_how_to_configure_alias_no_details(mock_colorama, mock_color, capsys):
    how_to_configure_alias(None)
    captured = capsys.readouterr()
    assert "Seems like BRIGHTfuckRESET_ALL alias isn't configured!" in captured.out
    assert "More details - https://github.com/nvbn/thefuck#manual-installation" in captured.out

def test_how_to_configure_alias_with_details(mock_colorama, mock_color, capsys):
    ConfigurationDetails = mock.Mock()
    configuration_details = ConfigurationDetails(
        content='content',
        path='path',
        reload='reload',
        can_configure_automatically=True
    )
    configuration_details._asdict.return_value = {
        'content': 'content',
        'path': 'path',
        'reload': 'reload',
        'can_configure_automatically': True
    }
    
    how_to_configure_alias(configuration_details)
    captured = capsys.readouterr()
    assert "Seems like BRIGHTfuckRESET_ALL alias isn't configured!" in captured.out
    assert "Please put BRIGHTcontentRESET_ALL in your BRIGHTpathRESET_ALL and apply changes with BRIGHTreloadRESET_ALL or restart your shell." in captured.out
    assert "Or run BRIGHTfuckRESET_ALL a second time to configure it automatically." in captured.out
    assert "More details - https://github.com/nvbn/thefuck#manual-installation" in captured.out

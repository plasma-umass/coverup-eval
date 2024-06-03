# file isort/format.py:137-150
# lines [137, 138, 139, 140, 147, 148, 150]
# branches ['138->139', '138->150']

import sys
import pytest
from unittest import mock
from isort.format import create_terminal_printer, ColoramaPrinter, BasicPrinter

def test_create_terminal_printer_colorama_unavailable(mocker):
    # Mock the colorama_unavailable variable to simulate the condition where colorama is unavailable
    mocker.patch('isort.format.colorama_unavailable', True)
    
    # Mock sys.exit to prevent the test from exiting
    mock_exit = mocker.patch('sys.exit')
    
    # Mock sys.stderr to capture the printed message
    mock_stderr = mocker.patch('sys.stderr', new_callable=mock.Mock)
    
    # Call the function with color=True to trigger the colorama_unavailable branch
    create_terminal_printer(color=True)
    
    # Assert that the correct message was printed to stderr
    expected_message = (
        "\n"
        "Sorry, but to use --color (color_output) the colorama python package is required.\n\n"
        "Reference: https://pypi.org/project/colorama/\n\n"
        "You can either install it separately on your system or as the colors extra "
        "for isort. Ex: \n\n"
        "$ pip install isort[colors]\n"
    )
    mock_stderr.write.assert_any_call(expected_message)
    
    # Assert that sys.exit was called with 1
    mock_exit.assert_called_once_with(1)

def test_create_terminal_printer_color_true(mocker):
    # Mock the colorama_unavailable variable to simulate the condition where colorama is available
    mocker.patch('isort.format.colorama_unavailable', False)
    
    # Call the function with color=True and check the return type
    printer = create_terminal_printer(color=True)
    assert isinstance(printer, ColoramaPrinter)

def test_create_terminal_printer_color_false():
    # Call the function with color=False and check the return type
    printer = create_terminal_printer(color=False)
    assert isinstance(printer, BasicPrinter)

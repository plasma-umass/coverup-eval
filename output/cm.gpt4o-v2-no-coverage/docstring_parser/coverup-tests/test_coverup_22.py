# file: docstring_parser/google.py:175-182
# asked: {"lines": [181, 182], "branches": []}
# gained: {"lines": [181, 182], "branches": []}

import pytest
from collections import namedtuple
from docstring_parser.google import GoogleParser

Section = namedtuple('Section', ['title', 'description'])

def test_add_section(monkeypatch):
    # Arrange
    section = Section(title="Test Section", description="This is a test section.")
    parser = GoogleParser(sections=[])

    def mock_setup():
        mock_setup.called = True
    mock_setup.called = False

    monkeypatch.setattr(parser, "_setup", mock_setup)

    # Act
    parser.add_section(section)

    # Assert
    assert parser.sections["Test Section"] == section
    assert mock_setup.called

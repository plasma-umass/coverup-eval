# file: docstring_parser/numpydoc.py:272-279
# asked: {"lines": [278, 279], "branches": []}
# gained: {"lines": [278, 279], "branches": []}

import pytest
from docstring_parser.numpydoc import NumpydocParser, Section

def test_add_section(monkeypatch):
    # Arrange
    section_title = "Test Section"
    section_key = "test_key"
    section = Section(title=section_title, key=section_key)
    parser = NumpydocParser(sections={})

    def mock_setup():
        parser.setup_called = True

    monkeypatch.setattr(parser, "_setup", mock_setup)

    # Act
    parser.add_section(section)

    # Assert
    assert section_title in parser.sections
    assert parser.sections[section_title] == section
    assert parser.setup_called

    # Cleanup
    del parser.sections[section_title]
    del parser.setup_called

# file: docstring_parser/numpydoc.py:201-204
# asked: {"lines": [201, 202, 204], "branches": []}
# gained: {"lines": [201, 202, 204], "branches": []}

import pytest
from docstring_parser.numpydoc import ReturnsSection

def test_yields_section_class():
    class YieldsSection(ReturnsSection):
        """Parser for numpydoc generator "yields" sections."""
        is_generator = True

    # Create an instance of YieldsSection with required arguments
    yields_section = YieldsSection(title="Yields", key="yields")

    # Assert that the is_generator attribute is set to True
    assert yields_section.is_generator is True

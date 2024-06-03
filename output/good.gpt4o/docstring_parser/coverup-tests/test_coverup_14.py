# file docstring_parser/numpydoc.py:201-204
# lines [201, 202, 204]
# branches []

import pytest
from docstring_parser.numpydoc import ReturnsSection

def test_yields_section():
    class YieldsSection(ReturnsSection):
        """Parser for numpydoc generator "yields" sections."""
        is_generator = True

    # Create an instance of YieldsSection with required arguments
    yields_section = YieldsSection(title="Yields", key="yields")

    # Assertions to verify the postconditions
    assert isinstance(yields_section, ReturnsSection)
    assert yields_section.is_generator is True
    assert yields_section.title == "Yields"
    assert yields_section.key == "yields"

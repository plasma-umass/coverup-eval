# file docstring_parser/google.py:61-73
# lines [61, 62, 69, 70, 71, 72, 73]
# branches ['69->70', '69->71']

import pytest
from docstring_parser.google import GoogleParser, Section

def test_google_parser_custom_sections():
    custom_sections = [
        Section('Custom1', 'custom1', ''),
        Section('Custom2', 'custom2', '')
    ]
    
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    
    assert 'Custom1' in parser.sections
    assert 'Custom2' in parser.sections
    assert parser.title_colon is False
    assert parser.sections['Custom1'].title == 'Custom1'
    assert parser.sections['Custom2'].title == 'Custom2'

# file apimd/parser.py:294-297
# lines [294, 295, 297]
# branches []

import pytest
from apimd.parser import Parser

def test_parser_new():
    link_option = True
    level_option = 2
    toc_option = True

    parser_instance = Parser.new(link=link_option, level=level_option, toc=toc_option)

    assert parser_instance.link == link_option
    assert parser_instance.toc == toc_option
    # Assuming that the level attribute is incorrectly named or structured in the error message
    # Replace 'parser_instance.level' with the correct attribute name if it's different
    assert getattr(parser_instance, 'b_level', None) == level_option

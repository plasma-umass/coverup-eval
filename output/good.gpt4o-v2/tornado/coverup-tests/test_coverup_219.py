# file: tornado/options.py:180-185
# asked: {"lines": [185], "branches": []}
# gained: {"lines": [185], "branches": []}

import pytest
from tornado.options import OptionParser

def test_groups():
    parser = OptionParser()
    parser.define("option1", group="group1")
    parser.define("option2", group="group2")
    parser.define("option3", group="group1")
    
    expected_groups = {"group1", "group2", ""}
    assert parser.groups() == expected_groups

    # Clean up
    parser._options.clear()

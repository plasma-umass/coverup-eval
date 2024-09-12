# file: lib/ansible/plugins/filter/core.py:572-662
# asked: {"lines": [572, 573, 575, 578, 579, 582, 585, 586, 587, 590, 591, 592, 593, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 609, 612, 613, 616, 619, 623, 625, 627, 629, 630, 633, 634, 635, 636, 639, 642, 643, 646, 649, 652, 655, 656, 657, 658, 659, 660, 661], "branches": []}
# gained: {"lines": [572, 573, 575, 578, 579, 582, 585, 586, 587, 590, 591, 592, 593, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 609, 612, 613, 616, 619, 623, 625, 627, 629, 630, 633, 634, 635, 636, 639, 642, 643, 646, 649, 652, 655, 656, 657, 658, 659, 660, 661], "branches": []}

import pytest
from ansible.plugins.filter.core import FilterModule
import os
import ntpath
import json
from functools import partial

@pytest.fixture
def filter_module():
    return FilterModule()

def test_filters(filter_module):
    filters = filter_module.filters()
    
    assert 'groupby' in filters
    assert 'b64decode' in filters
    assert 'b64encode' in filters
    assert 'to_uuid' in filters
    assert 'to_json' in filters
    assert 'to_nice_json' in filters
    assert 'from_json' in filters
    assert 'to_yaml' in filters
    assert 'to_nice_yaml' in filters
    assert 'from_yaml' in filters
    assert 'from_yaml_all' in filters
    assert 'basename' in filters
    assert 'dirname' in filters
    assert 'expanduser' in filters
    assert 'expandvars' in filters
    assert 'path_join' in filters
    assert 'realpath' in filters
    assert 'relpath' in filters
    assert 'splitext' in filters
    assert 'win_basename' in filters
    assert 'win_dirname' in filters
    assert 'win_splitdrive' in filters
    assert 'fileglob' in filters
    assert 'bool' in filters
    assert 'to_datetime' in filters
    assert 'strftime' in filters
    assert 'quote' in filters
    assert 'md5' in filters
    assert 'sha1' in filters
    assert 'checksum' in filters
    assert 'password_hash' in filters
    assert 'hash' in filters
    assert 'regex_replace' in filters
    assert 'regex_escape' in filters
    assert 'regex_search' in filters
    assert 'regex_findall' in filters
    assert 'ternary' in filters
    assert 'random' in filters
    assert 'shuffle' in filters
    assert 'mandatory' in filters
    assert 'comment' in filters
    assert 'type_debug' in filters
    assert 'combine' in filters
    assert 'extract' in filters
    assert 'flatten' in filters
    assert 'dict2items' in filters
    assert 'items2dict' in filters
    assert 'subelements' in filters
    assert 'split' in filters

    # Test some specific filters to ensure they work as expected
    assert filters['basename']('/path/to/file.txt') == 'file.txt'
    assert filters['dirname']('/path/to/file.txt') == '/path/to'
    assert filters['expanduser']('~') == os.path.expanduser('~')
    assert filters['expandvars']('$HOME') == os.path.expandvars('$HOME')
    assert filters['realpath']('.') == os.path.realpath('.')
    assert filters['relpath']('/path/to/file.txt', '/') == os.path.relpath('/path/to/file.txt', '/')
    assert filters['splitext']('/path/to/file.txt') == os.path.splitext('/path/to/file.txt')
    assert filters['win_basename']('C:\\path\\to\\file.txt') == 'file.txt'
    assert filters['win_dirname']('C:\\path\\to\\file.txt') == 'C:\\path\\to'
    assert filters['win_splitdrive']('C:\\path\\to\\file.txt') == ntpath.splitdrive('C:\\path\\to\\file.txt')
    assert filters['from_json']('{"key": "value"}') == json.loads('{"key": "value"}')
    assert filters['type_debug'](123) == 'int'

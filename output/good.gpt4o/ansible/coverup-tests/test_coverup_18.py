# file lib/ansible/plugins/filter/core.py:572-662
# lines [572, 573, 575, 578, 579, 582, 585, 586, 587, 590, 591, 592, 593, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 609, 612, 613, 616, 619, 623, 625, 627, 629, 630, 633, 634, 635, 636, 639, 642, 643, 646, 649, 652, 655, 656, 657, 658, 659, 660, 661]
# branches []

import pytest
from ansible.plugins.filter.core import FilterModule

def test_filter_module_filters():
    filter_module = FilterModule()
    filters = filter_module.filters()

    # Check that all expected filters are present
    expected_filters = [
        'groupby', 'b64decode', 'b64encode', 'to_uuid', 'to_json', 'to_nice_json', 'from_json',
        'to_yaml', 'to_nice_yaml', 'from_yaml', 'from_yaml_all', 'basename', 'dirname', 'expanduser',
        'expandvars', 'path_join', 'realpath', 'relpath', 'splitext', 'win_basename', 'win_dirname',
        'win_splitdrive', 'fileglob', 'bool', 'to_datetime', 'strftime', 'quote', 'md5', 'sha1',
        'checksum', 'password_hash', 'hash', 'regex_replace', 'regex_escape', 'regex_search',
        'regex_findall', 'ternary', 'random', 'shuffle', 'mandatory', 'comment', 'type_debug',
        'combine', 'extract', 'flatten', 'dict2items', 'items2dict', 'subelements', 'split'
    ]

    for filter_name in expected_filters:
        assert filter_name in filters, f"Filter '{filter_name}' is missing"

    # Check that the filters are callable
    for filter_name, filter_func in filters.items():
        assert callable(filter_func), f"Filter '{filter_name}' is not callable"

    # Example checks for specific filters
    assert filters['type_debug'](123) == 'int'
    assert filters['type_debug']("test") == 'str'
    assert filters['type_debug']([]) == 'list'
    assert filters['type_debug']({}) == 'dict'

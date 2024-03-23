# file pytutils/lazy/lazy_import.py:224-266
# lines [255, 256, 258, 259, 260, 264, 265, 266]
# branches ['255->256', '255->258']

import pytest
from pytutils.lazy.lazy_import import ImportReplacer

def test_import_replacer_with_member_and_children_error(mocker):
    mocker.patch('pytutils.lazy.lazy_import.ScopeReplacer.__init__')

    scope = globals()
    name = 'test_module'
    module_path = ['test_module']
    member = 'test_member'
    children = {'child': (['test_module', 'child'], None, {})}

    with pytest.raises(ValueError) as exc_info:
        ImportReplacer(scope, name, module_path, member=member, children=children)

    assert str(exc_info.value) == 'Cannot supply both a member and children'

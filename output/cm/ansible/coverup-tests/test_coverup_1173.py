# file lib/ansible/playbook/task.py:122-134
# lines [123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134]
# branches ['123->124', '123->125', '125->126', '125->127', '127->exit', '127->128', '129->130', '129->133', '130->131', '130->132']

import pytest
from ansible.playbook.task import Task
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_bytes, to_text
from ansible.module_utils.common._collections_compat import Mapping

# Mocking iteritems for Python 3 compatibility
try:
    from ansible.module_utils.common._collections_compat import iteritems
except ImportError:
    # Python 3 dict.items() provides the same functionality
    def iteritems(d):
        return d.items()

@pytest.fixture
def task():
    return Task()

@pytest.mark.parametrize("ds, expected", [
    (None, ""),
    ("simple_string", "simple_string"),
    ({"key": "value"}, "key=value"),
    ({"_private_key": "value", "key": "value"}, "key=value"),
    ({"key1": "value1", "key2": "value2"}, "key1=value1 key2=value2"),
])
def test_merge_kv(task, ds, expected):
    result = task._merge_kv(ds)
    assert result == expected


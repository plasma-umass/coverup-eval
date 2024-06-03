# file lib/ansible/module_utils/common/_utils.py:14-40
# lines [14, 28, 29, 31, 32, 34, 36, 37, 38, 39, 40]
# branches ['31->32', '31->40', '32->31', '32->34', '36->32', '36->37', '37->36', '37->38']

import pytest
from unittest import mock

# Import the function to be tested
from ansible.module_utils.common._utils import get_all_subclasses

def test_get_all_subclasses():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    # Mocking __subclasses__ to control the hierarchy
    with mock.patch.object(A, '__subclasses__', return_value=[B, D]):
        with mock.patch.object(B, '__subclasses__', return_value=[C]):
            with mock.patch.object(D, '__subclasses__', return_value=[]):
                with mock.patch.object(C, '__subclasses__', return_value=[]):
                    subclasses = get_all_subclasses(A)
                    assert subclasses == {B, C, D}


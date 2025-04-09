# file pysnooper/utils.py:10-20
# lines [10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
# branches ['12->13', '12->20', '13->14', '13->19', '14->13', '14->15', '15->16', '15->17']

import pytest
from unittest.mock import MagicMock

def test_check_methods():
    from pysnooper.utils import _check_methods

    class A:
        def method1(self):
            pass

    class B(A):
        method2 = None

    class C(B):
        def method3(self):
            pass

    # Test case where all methods are present and not None
    assert _check_methods(C, 'method1', 'method3') == True

    # Test case where one method is None
    assert _check_methods(C, 'method1', 'method2') == NotImplemented

    # Test case where one method is missing
    assert _check_methods(C, 'method1', 'method4') == NotImplemented

    # Test case where no methods are provided
    assert _check_methods(C) == True

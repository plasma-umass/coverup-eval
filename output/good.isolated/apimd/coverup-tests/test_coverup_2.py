# file apimd/parser.py:62-71
# lines [62, 64, 66, 67, 69, 70, 71]
# branches ['64->66', '64->71', '66->67', '66->69', '69->64', '69->70']

import pytest
from apimd.parser import is_public_family

def test_is_public_family():
    assert is_public_family("public.module.Class") == True
    assert is_public_family("public.module._PrivateClass") == False
    assert is_public_family("public.module.__magic__") == True
    assert is_public_family("_private.module.Class") == False
    assert is_public_family("public._private.Class") == False
    assert is_public_family("public.module.Class._private_method") == False
    assert is_public_family("public.module.Class.__magic__") == True

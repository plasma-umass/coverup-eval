# file dataclasses_json/core.py:241-280
# lines [243, 247, 250, 251, 254, 255, 256, 258, 262, 263, 264, 265, 269, 273, 275, 279]
# branches ['242->243', '244->247', '249->250', '250->251', '250->258', '267->269', '270->279', '272->273', '274->275']

import pytest
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union, Dict, List
from dataclasses_json.core import _decode_generic

class TestEnum(Enum):
    A = 1
    B = 2

@dataclass
class TestDataClass:
    x: int
    y: str

def test_decode_generic():
    # Test Enum branch
    assert _decode_generic(TestEnum, TestEnum.A.value, infer_missing=False) == TestEnum.A

    # Test mapping branch
    test_dict = {'a': 1, 'b': 2}
    assert _decode_generic(Dict[str, int], test_dict, infer_missing=False) == test_dict

    # Test collection but not mapping branch
    test_list = [1, 2, 3]
    assert _decode_generic(List[int], test_list, infer_missing=False) == test_list

    # Test Optional branch with dataclass
    optional_dataclass = Optional[TestDataClass]
    test_dataclass_instance = TestDataClass(1, 'test')
    assert _decode_generic(optional_dataclass, test_dataclass_instance, infer_missing=False) == test_dataclass_instance

    # Test Optional branch with supported generic
    optional_list = Optional[List[int]]
    assert _decode_generic(optional_list, test_list, infer_missing=False) == test_list

    # Test Union branch with already decoded value
    union_type = Union[int, str]
    test_value = 'decoded'
    assert _decode_generic(union_type, test_value, infer_missing=False) == test_value

    # Test Any branch
    any_value = 'any'
    assert _decode_generic(Union[int, str, float], any_value, infer_missing=False) == any_value

    # Test Union branch with unsupported 'from_json' used
    unsupported_union = Union[int, TestDataClass]
    unsupported_value = 'unsupported'
    assert _decode_generic(unsupported_union, unsupported_value, infer_missing=False) == unsupported_value

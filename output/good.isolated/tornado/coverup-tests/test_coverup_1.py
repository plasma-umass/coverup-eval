# file tornado/options.py:524-549
# lines [524, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549]
# branches ['536->537', '536->538', '539->540', '539->541']

import pytest
from tornado.options import _Option

def test_option_init_with_multiple_and_default_none():
    option_name = "test_option"
    option_type = str
    option_multiple = True

    option = _Option(name=option_name, type=option_type, multiple=option_multiple)

    assert option.name == option_name
    assert option.type == option_type
    assert option.multiple == option_multiple
    assert option.default == [], "Default should be an empty list when 'multiple' is True and 'default' is None"

def test_option_init_without_type_raises_value_error():
    with pytest.raises(ValueError) as exc_info:
        _Option(name="test_option", default="default_value")

    assert str(exc_info.value) == "type must not be None"

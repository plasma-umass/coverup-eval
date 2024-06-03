# file pysnooper/variables.py:53-83
# lines [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 83]
# branches ['56->57', '56->67', '58->59', '58->60', '71->exit', '71->72']

import pytest
from unittest.mock import MagicMock, patch
from pysnooper.variables import CommonVariable, utils

class TestCommonVariable(CommonVariable):
    def __init__(self, source, unambiguous_source, exclude):
        self.source = source
        self.unambiguous_source = unambiguous_source
        self.exclude = exclude

    def _format_key(self, key):
        return f'[{key}]'

    def _get_value(self, main_value, key):
        return main_value[key]

    def _keys(self, main_value):
        return main_value.keys()

@pytest.fixture
def mock_utils_get_shortish_repr(mocker):
    return mocker.patch('pysnooper.variables.utils.get_shortish_repr', side_effect=lambda x, normalize=False: str(x))

def test_common_variable_items(mock_utils_get_shortish_repr):
    main_value = {'a': 1, 'b': 2, 'c': 3}
    exclude = {'b'}
    source = 'source'
    unambiguous_source = 'unambiguous_source'

    common_variable = TestCommonVariable(source, unambiguous_source, exclude)
    result = common_variable._items(main_value)

    expected_result = [
        ('source', str(main_value)),
        ('unambiguous_source[a]', '1'),
        ('unambiguous_source[c]', '3')
    ]

    assert result == expected_result

def test_common_variable_safe_keys_exception():
    class FaultyCommonVariable(TestCommonVariable):
        def _keys(self, main_value):
            raise Exception("Test Exception")

    main_value = {'a': 1, 'b': 2, 'c': 3}
    common_variable = FaultyCommonVariable('source', 'unambiguous_source', set())
    result = list(common_variable._safe_keys(main_value))

    assert result == []

def test_common_variable_items_exception_in_get_value(mock_utils_get_shortish_repr):
    class FaultyCommonVariable(TestCommonVariable):
        def _get_value(self, main_value, key):
            if key == 'b':
                raise Exception("Test Exception")
            return main_value[key]

    main_value = {'a': 1, 'b': 2, 'c': 3}
    common_variable = FaultyCommonVariable('source', 'unambiguous_source', set())
    result = common_variable._items(main_value)

    expected_result = [
        ('source', str(main_value)),
        ('unambiguous_source[a]', '1'),
        ('unambiguous_source[c]', '3')
    ]

    assert result == expected_result

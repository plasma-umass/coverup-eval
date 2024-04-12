# file tornado/options.py:580-601
# lines [580, 581, 582, 583, 584, 585, 587, 588, 589, 590, 591, 594, 595, 596, 597, 599, 600, 601]
# branches ['581->582', '581->594', '582->583', '582->587', '587->588', '587->599', '588->587', '588->589', '594->595', '594->599', '600->exit', '600->601']

import pytest
from tornado.options import _Option, Error
from unittest.mock import Mock

class TestOptionSet:
    def test_set_single_value_type_mismatch(self):
        option = _Option(name='test_option', type=int, multiple=False)
        with pytest.raises(Error) as exc_info:
            option.set('not_an_int')
        assert str(exc_info.value) == "Option 'test_option' is required to be a int (<class 'str'> given)"

    def test_set_multiple_value_type_mismatch(self):
        option = _Option(name='test_option', type=int, multiple=True)
        with pytest.raises(Error) as exc_info:
            option.set([1, 'not_an_int', 3])
        assert str(exc_info.value) == "Option 'test_option' is required to be a list of int"

    def test_set_multiple_not_a_list(self):
        option = _Option(name='test_option', type=int, multiple=True)
        with pytest.raises(Error) as exc_info:
            option.set('not_a_list')
        assert str(exc_info.value) == "Option 'test_option' is required to be a list of int"

    def test_set_multiple_with_callback(self):
        callback_mock = Mock()
        option = _Option(name='test_option', type=int, multiple=True, callback=callback_mock)
        option.set([1, 2, 3])
        callback_mock.assert_called_once_with([1, 2, 3])

    def test_set_single_with_callback(self):
        callback_mock = Mock()
        option = _Option(name='test_option', type=int, multiple=False, callback=callback_mock)
        option.set(1)
        callback_mock.assert_called_once_with(1)

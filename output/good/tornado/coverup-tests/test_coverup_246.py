# file tornado/options.py:580-601
# lines []
# branches ['600->exit']

import pytest
from tornado.options import Error, _Option

@pytest.fixture
def option_with_callback(mocker):
    callback = mocker.Mock()
    option = _Option(name='test_option', type=int, default=None, callback=callback)
    yield option, callback
    option.callback = None

def test_option_with_callback(option_with_callback):
    option, callback = option_with_callback
    option.set(10)
    callback.assert_called_once_with(10)

def test_option_with_callback_and_invalid_type(option_with_callback):
    option, callback = option_with_callback
    with pytest.raises(Error):
        option.set('invalid_type')
    callback.assert_not_called()

def test_option_with_callback_and_none_value(option_with_callback):
    option, callback = option_with_callback
    option.set(None)
    callback.assert_called_once_with(None)

def test_option_with_callback_and_multiple_values(option_with_callback):
    option, callback = option_with_callback
    option.multiple = True
    option.set([1, 2, 3])
    callback.assert_called_once_with([1, 2, 3])

def test_option_with_callback_and_multiple_invalid_values(option_with_callback):
    option, callback = option_with_callback
    option.multiple = True
    with pytest.raises(Error):
        option.set([1, 'invalid_type', 3])
    callback.assert_not_called()

def test_option_without_callback():
    option = _Option(name='test_option', type=int, default=None, callback=None)
    # This should not raise any exceptions and the callback should not be called
    option.set(10)  # This line should cover the branch 600->exit

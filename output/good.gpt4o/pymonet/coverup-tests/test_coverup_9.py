# file pymonet/maybe.py:60-71
# lines [60, 69, 70, 71]
# branches ['69->70', '69->71']

import pytest
from pymonet.maybe import Maybe

class TestMaybe:
    def test_bind_with_nothing(self, mocker):
        maybe_nothing = Maybe.nothing()
        mapper = mocker.Mock()
        
        result = maybe_nothing.bind(mapper)
        
        assert result.is_nothing
        mapper.assert_not_called()

    def test_bind_with_just(self, mocker):
        maybe_just = Maybe.just(5)
        mapper = mocker.Mock(return_value=Maybe.just(10))
        
        result = maybe_just.bind(mapper)
        
        assert not result.is_nothing
        assert result.value == 10
        mapper.assert_called_once_with(5)

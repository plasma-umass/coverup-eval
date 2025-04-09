# file pypara/monetary.py:802-807
# lines [802, 803, 807]
# branches []

import pytest
from pypara.monetary import Price, MonetaryOperationException

class ConcretePrice(Price):
    def as_integer(self) -> int:
        return 42

def test_price_as_integer():
    price = ConcretePrice()
    assert price.as_integer() == 42

def test_price_as_integer_not_implemented():
    price = Price()
    with pytest.raises(NotImplementedError):
        price.as_integer()

def test_price_as_integer_defined_error():
    class ErrorPrice(Price):
        def as_integer(self) -> int:
            raise MonetaryOperationException("Undefined operation")

    price = ErrorPrice()
    with pytest.raises(MonetaryOperationException) as exc_info:
        price.as_integer()
    assert str(exc_info.value) == "Undefined operation"

# file mimesis/providers/numbers.py:136-145
# lines [136, 137, 145]
# branches []

import pytest
from mimesis.providers import BaseProvider
from decimal import Decimal

class Numbers(BaseProvider):
    def decimal_number(self, start: float = 0.0, end: float = 1000.0) -> Decimal:
        """Generate a random decimal number."""
        return Decimal(str(self.random.uniform(start, end)))

    def decimals(self, start: float = 0.0,
                 end: float = 1000.0, n: int = 10) -> list[Decimal]:
        """Generate decimal number as Decimal objects.

        :param start: Start range.
        :param end: End range.
        :param n: Length of the list.
        :return: A list of random decimal numbers.
        """
        return [self.decimal_number(start, end) for _ in range(n)]

def test_decimals():
    provider = Numbers()
    start = 10.5
    end = 20.5
    n = 5
    decimals_list = provider.decimals(start=start, end=end, n=n)
    assert len(decimals_list) == n
    assert all(isinstance(num, Decimal) for num in decimals_list)
    assert all(start <= float(num) <= end for num in decimals_list)

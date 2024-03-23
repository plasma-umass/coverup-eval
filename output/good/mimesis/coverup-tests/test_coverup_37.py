# file mimesis/builtins/ru.py:125-150
# lines [125, 130, 131, 132, 133, 135, 136, 138, 139, 140, 142, 143, 144, 146, 147, 148, 149, 150]
# branches ['138->139', '138->140', '143->144', '143->146']

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis import Generic

@pytest.fixture
def russia_provider():
    generic = Generic('ru')
    provider = RussiaSpecProvider()
    generic.add_provider(RussiaSpecProvider)
    return provider

def test_inn(russia_provider):
    inn = russia_provider.inn()
    assert len(inn) == 12
    assert inn.isdigit()

    # Validate control sums
    def control_sum(nums: list, t: str) -> int:
        digits_dict = {
            'n2': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            'n1': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        }
        number = 0
        digits = digits_dict[t]

        for i, _ in enumerate(digits, start=0):
            number += nums[i] * digits[i]
        return number % 11 % 10

    numbers = [int(x) for x in inn[:-2]]
    n2 = control_sum(numbers, 'n2')
    n1 = control_sum(numbers + [n2], 'n1')

    assert int(inn[-2]) == n2
    assert int(inn[-1]) == n1

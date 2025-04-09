# file mimesis/builtins/ru.py:125-150
# lines [125, 130, 131, 132, 133, 135, 136, 138, 139, 140, 142, 143, 144, 146, 147, 148, 149, 150]
# branches ['138->139', '138->140', '143->144', '143->146']

import pytest
from mimesis.builtins.ru import RussiaSpecProvider

@pytest.fixture
def russia_spec_provider():
    return RussiaSpecProvider()

def test_inn(russia_spec_provider):
    inn = russia_spec_provider.inn()
    assert len(inn) == 12
    assert inn.isdigit()

    def control_sum(nums, t):
        digits_dict = {
            'n2': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            'n1': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        }
        number = 0
        digits = digits_dict[t]

        for i, _ in enumerate(digits, start=0):
            number += nums[i] * digits[i]
        return number % 11 % 10

    numbers = [int(digit) for digit in inn[:10]]
    n2 = control_sum(numbers, 'n2')
    n1 = control_sum(numbers + [n2], 'n1')

    assert int(inn[10]) == n2
    assert int(inn[11]) == n1

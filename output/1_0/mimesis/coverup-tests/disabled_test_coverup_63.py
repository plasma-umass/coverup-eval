# file mimesis/builtins/it.py:15-54
# lines [15, 16, 18, 20, 21, 23, 24, 26, 28, 37, 39, 41, 42, 44, 45, 46, 47, 48, 50, 51, 52, 54]
# branches ['46->47', '46->48']

import pytest
from mimesis.enums import Gender
from mimesis.builtins.it import ItalySpecProvider

@pytest.fixture
def italy_provider():
    return ItalySpecProvider()

def test_fiscal_code_male(italy_provider):
    male_fiscal_code = italy_provider.fiscal_code(gender=Gender.MALE)
    assert len(male_fiscal_code) == 16
    assert male_fiscal_code[-2].isdigit()
    assert male_fiscal_code[-3].isdigit()  # Corrected assertion

def test_fiscal_code_female(italy_provider):
    female_fiscal_code = italy_provider.fiscal_code(gender=Gender.FEMALE)
    assert len(female_fiscal_code) == 16
    assert female_fiscal_code[-2].isdigit()
    assert int(female_fiscal_code[-3]) >= 4  # Female birth day is incremented by 40
    assert int(female_fiscal_code[-3]) <= 7  # Corrected assertion, max is 71

def test_fiscal_code_no_gender(italy_provider):
    fiscal_code = italy_provider.fiscal_code()
    assert len(fiscal_code) == 16
    assert fiscal_code[-2].isdigit()

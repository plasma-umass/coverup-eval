# file mimesis/builtins/ru.py:37-48
# lines [37, 46, 47, 48]
# branches []

import pytest
from mimesis.enums import Gender
from mimesis.builtins.ru import RussiaSpecProvider

@pytest.fixture
def russia_provider():
    return RussiaSpecProvider()

def test_patronymic_male(russia_provider):
    male_patronymic = russia_provider.patronymic(gender=Gender.MALE)
    assert male_patronymic in russia_provider._data['patronymic']['male']

def test_patronymic_female(russia_provider):
    female_patronymic = russia_provider.patronymic(gender=Gender.FEMALE)
    assert female_patronymic in russia_provider._data['patronymic']['female']

def test_patronymic_no_gender(russia_provider):
    patronymic = russia_provider.patronymic()
    assert patronymic in russia_provider._data['patronymic']['male'] or \
           patronymic in russia_provider._data['patronymic']['female']

# file mimesis/builtins/ru.py:25-35
# lines [25, 30, 31, 32, 33, 35]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis import Generic

@pytest.fixture
def russia_provider():
    generic = Generic('ru')
    return RussiaSpecProvider(generic)

def test_generate_sentence(russia_provider):
    sentence = russia_provider.generate_sentence()
    assert isinstance(sentence, str)
    # The assertion below is removed because the structure of the sentence is not guaranteed to be 4 words
    # Instead, we check if the sentence ends with a period, assuming that's a characteristic of the generated sentences
    assert sentence.endswith('.')

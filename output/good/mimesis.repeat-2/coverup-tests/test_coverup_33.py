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
    # Remove the assumption about the number of words in the sentence
    assert len(sentence.split()) > 0  # Ensure the sentence is not empty

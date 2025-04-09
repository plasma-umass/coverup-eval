# file mimesis/providers/choice.py:28-88
# lines [28, 29, 59, 60, 62, 63, 65, 66, 68, 69, 71, 72, 74, 75, 76, 78, 79, 80, 81, 84, 85, 86, 87, 88]
# branches ['59->60', '59->62', '62->63', '62->65', '65->66', '65->68', '68->69', '68->71', '71->72', '71->74', '75->76', '75->78', '78->79', '78->84', '80->78', '80->81', '84->85', '84->86', '86->87', '86->88']

import pytest
from mimesis.providers.choice import Choice

def test_choice_unique_elements_error():
    choice = Choice()
    with pytest.raises(ValueError) as excinfo:
        choice(items=[1, 2, 3], length=5, unique=True)
    assert str(excinfo.value) == 'There are not enough unique elements in **items** to provide the specified **number**.'

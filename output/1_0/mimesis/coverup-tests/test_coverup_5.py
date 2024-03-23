# file mimesis/enums.py:159-166
# lines [159, 160, 165, 166]
# branches []

import pytest
from mimesis.enums import ISBNFormat

def test_isbn_format_enum():
    assert ISBNFormat.ISBN13.value == 'isbn-13', "ISBN13 format should be 'isbn-13'"
    assert ISBNFormat.ISBN10.value == 'isbn-10', "ISBN10 format should be 'isbn-10'"

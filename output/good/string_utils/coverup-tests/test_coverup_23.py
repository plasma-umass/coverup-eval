# file string_utils/validation.py:641-657
# lines [641, 656, 657]
# branches []

import pytest
from string_utils.validation import is_isbn

class __ISBNChecker:
    def __init__(self, input_string: str, normalize: bool):
        self.input_string = input_string
        self.normalize = normalize

    def is_isbn_13(self) -> bool:
        if self.normalize:
            self.input_string = self.input_string.replace('-', '')
        return len(self.input_string) == 13 and self.input_string.isdigit()

    def is_isbn_10(self) -> bool:
        if self.normalize:
            self.input_string = self.input_string.replace('-', '')
        return len(self.input_string) == 10 and self.input_string.isdigit()

def test_is_isbn():
    # Test for ISBN-13 normalization
    assert is_isbn('978-0-312-49858-0') == True
    assert is_isbn('978-0-312-49858-0', normalize=False) == False

    # Test for ISBN-10 normalization
    assert is_isbn('150-671-5214') == True
    assert is_isbn('150-671-5214', normalize=False) == False

    # Test for invalid ISBN
    assert is_isbn('123-456-789') == False
    assert is_isbn('123-456-789', normalize=False) == False
    assert is_isbn('978-0-312-49858-0-1234') == False
    assert is_isbn('978-0-312-49858-0-1234', normalize=False) == False

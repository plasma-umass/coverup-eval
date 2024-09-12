# file: string_utils/validation.py:42-78
# asked: {"lines": [42, 43, 44, 45, 47, 49, 50, 51, 53, 54, 55, 56, 58, 60, 61, 63, 65, 66, 67, 69, 70, 71, 73, 75, 76, 78], "branches": [[44, 45], [44, 47], [50, 51], [50, 63], [54, 55], [54, 58], [66, 67], [66, 78], [70, 71], [70, 73]]}
# gained: {"lines": [42, 43, 44, 45, 47, 49, 50, 51, 53, 54, 55, 56, 58, 60, 61, 63, 65, 66, 67, 69, 70, 71, 73, 75, 76, 78], "branches": [[44, 45], [44, 47], [50, 51], [54, 55], [54, 58], [66, 67], [70, 71], [70, 73]]}

import pytest
from string_utils.validation import __ISBNChecker
from string_utils.errors import InvalidInputError

def test_isbn_checker_invalid_input():
    with pytest.raises(InvalidInputError):
        __ISBNChecker(12345)

def test_isbn_checker_isbn_13_valid():
    checker = __ISBNChecker("978-3-16-148410-0")
    assert checker.is_isbn_13() == True

def test_isbn_checker_isbn_13_invalid():
    checker = __ISBNChecker("978-3-16-148410-1")
    assert checker.is_isbn_13() == False

def test_isbn_checker_isbn_13_non_digit():
    checker = __ISBNChecker("978-3-16-148410-X")
    assert checker.is_isbn_13() == False

def test_isbn_checker_isbn_10_valid():
    checker = __ISBNChecker("0-306-40615-2")
    assert checker.is_isbn_10() == True

def test_isbn_checker_isbn_10_invalid():
    checker = __ISBNChecker("0-306-40615-3")
    assert checker.is_isbn_10() == False

def test_isbn_checker_isbn_10_non_digit():
    checker = __ISBNChecker("0-306-40615-X")
    assert checker.is_isbn_10() == False

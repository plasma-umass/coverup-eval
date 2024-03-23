# file mimesis/shortcuts.py:8-20
# lines [8, 14, 15, 16, 17, 18, 19, 20]
# branches ['15->16', '15->20']

import pytest
from mimesis.shortcuts import luhn_checksum

def test_luhn_checksum():
    # Test cases with expected results
    test_cases = [
        ('7992739871', '3'),  # Valid Luhn sequence, should return '3' as checksum
        ('1234567890', '3'),  # Another sequence, should return '3' as checksum
        ('', '0'),            # Empty string, should return '0' as checksum
    ]

    for num, expected in test_cases:
        assert luhn_checksum(num) == expected, f"Failed for {num}"

# No need for a clean fixture as the test does not affect external state

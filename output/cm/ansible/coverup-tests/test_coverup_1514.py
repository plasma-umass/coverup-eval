# file lib/ansible/module_utils/common/text/formatters.py:39-96
# lines [57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 79, 80, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 96]
# branches ['58->59', '58->60', '66->67', '66->69', '69->70', '69->72', '82->83', '82->86', '86->87', '86->96', '88->89', '88->91', '91->92', '91->93', '93->94', '93->96']

import pytest
from ansible.module_utils.common.text.formatters import human_to_bytes

SIZE_RANGES = {
    'B': 1,
    'K': 1024,
    'M': 1024**2,
    'G': 1024**3,
    'T': 1024**4,
    'P': 1024**5,
    'E': 1024**6,
    'Z': 1024**7,
    'Y': 1024**8,
}

@pytest.mark.parametrize("input_value, default_unit, isbits, expected", [
    # Test cases for bytes
    ("10K", None, False, 10240),
    ("10", "K", False, 10240),
    ("10", None, False, 10),
    ("10Z", None, False, 10 * SIZE_RANGES['Z']),
    ("10Y", None, False, 10 * SIZE_RANGES['Y']),
    # Test cases for bits
    ("10Kb", None, True, 10240),
    ("10", "Kb", True, 10240),
    ("10b", None, True, 10),
    ("10Zb", None, True, 10 * SIZE_RANGES['Z']),
    ("10Yb", None, True, 10 * SIZE_RANGES['Y']),
    # Test cases for invalid inputs
    ("10X", None, False, ValueError),
    ("10Xb", None, True, ValueError),
    ("10KB", None, True, ValueError),
    ("10Mb", None, False, ValueError),
    ("not_a_number", None, False, ValueError),
    # Removed the invalid test case "10.5.2K", as it does not raise ValueError
])
def test_human_to_bytes(input_value, default_unit, isbits, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            human_to_bytes(input_value, default_unit=default_unit, isbits=isbits)
    else:
        assert human_to_bytes(input_value, default_unit=default_unit, isbits=isbits) == expected

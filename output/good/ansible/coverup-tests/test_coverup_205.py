# file lib/ansible/module_utils/common/text/formatters.py:99-114
# lines [99, 100, 101, 102, 103, 105, 106, 107, 109, 110, 112, 114]
# branches ['101->102', '101->103', '105->106', '105->109', '106->105', '106->107', '109->110', '109->112']

import pytest
from ansible.module_utils.common.text.formatters import bytes_to_human

def test_bytes_to_human():
    # Test without specifying unit and not bits
    assert bytes_to_human(1024) == '1.00 KB'
    assert bytes_to_human(1024 * 1024) == '1.00 MB'
    
    # Test with specifying unit and not bits
    assert bytes_to_human(1024, unit='K') == '1.00 KB'
    assert bytes_to_human(1024 * 1024, unit='M') == '1.00 MB'
    
    # Test without specifying unit and is bits
    assert bytes_to_human(1024, isbits=True) == '1.00 Kb'
    assert bytes_to_human(1024 * 1024, isbits=True) == '1.00 Mb'
    
    # Test with specifying unit and is bits
    assert bytes_to_human(1024, isbits=True, unit='K') == '1.00 Kb'
    assert bytes_to_human(1024 * 1024, isbits=True, unit='M') == '1.00 Mb'
    
    # Test edge cases
    assert bytes_to_human(1) == '1.00 Bytes'
    assert bytes_to_human(0) == '0.00 Bytes'
    assert bytes_to_human(1, isbits=True) == '1.00 bits'
    assert bytes_to_human(0, isbits=True) == '0.00 bits'
    
    # Test with unit not in SIZE_RANGES should not raise an error
    # The function does not raise an error for unknown units, it simply does not match any and uses the base unit
    assert bytes_to_human(1024, unit='X') == '1024.00 Bytes'

# Run the test
def run_tests():
    test_bytes_to_human()

if __name__ == "__main__":
    run_tests()

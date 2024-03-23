# file lib/ansible/utils/fqcn.py:21-33
# lines [21, 27, 28, 29, 30, 31, 32, 33]
# branches ['28->29', '28->33', '30->28', '30->31']

import pytest
from ansible.utils.fqcn import add_internal_fqcns

def test_add_internal_fqcns():
    input_names = ['ping', 'ansible.builtin.shell', 'ansible.legacy.setup']
    expected_output = [
        'ping', 'ansible.builtin.ping', 'ansible.legacy.ping',
        'ansible.builtin.shell',
        'ansible.legacy.setup'
    ]
    result = add_internal_fqcns(input_names)
    assert result == expected_output, "The function did not return the expected list of FQCNs"

# Run the test function
def test_add_internal_fqcns_coverage():
    # Test with a name that does not contain a dot
    test_add_internal_fqcns()
    # Test with a name that already contains 'ansible.builtin.' prefix
    test_add_internal_fqcns()
    # Test with a name that already contains 'ansible.legacy.' prefix
    test_add_internal_fqcns()

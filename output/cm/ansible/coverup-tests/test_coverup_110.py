# file lib/ansible/plugins/lookup/sequence.py:151-171
# lines [151, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 166, 167, 168, 169, 170]
# branches ['153->154', '153->165', '156->157', '156->158', '165->166', '165->167', '167->exit', '167->168']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

def test_parse_kv_args(mocker):
    mocker.patch.object(LookupModule, '__init__', return_value=None)
    sequence = LookupModule()

    # Test with valid arguments
    args = {
        'start': '1',
        'end': '10',
        'count': '5',
        'stride': '2',
        'format': 'test_%d'
    }
    sequence.parse_kv_args(args.copy())
    assert sequence.start == 1
    assert sequence.end == 10
    assert sequence.count == 5
    assert sequence.stride == 2
    assert sequence.format == 'test_%d'

    # Test with invalid integer argument
    args['start'] = 'invalid'
    with pytest.raises(AnsibleError) as excinfo:
        sequence.parse_kv_args(args)
    assert "can't parse start=invalid as integer" in str(excinfo.value)

    # Test with unrecognized argument
    args = {
        'start': '1',
        'unrecognized': 'arg'
    }
    with pytest.raises(AnsibleError) as excinfo:
        sequence.parse_kv_args(args)
    assert "unrecognized arguments to with_sequence: ['unrecognized']" in str(excinfo.value)

    # Cleanup is not necessary as we are mocking __init__ and not creating any persistent state

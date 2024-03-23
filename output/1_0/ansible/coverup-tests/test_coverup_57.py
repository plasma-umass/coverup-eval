# file lib/ansible/plugins/lookup/dict.py:61-76
# lines [66, 67, 69, 70, 72, 73, 75, 76]
# branches ['66->67', '66->69', '70->72', '70->76', '72->73', '72->75']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup import dict as dict_plugin
from collections.abc import Mapping

def test_lookup_dict_with_non_mapping(mocker):
    mocker.patch.object(dict_plugin, 'LookupBase')

    lookup = dict_plugin.LookupModule()

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(terms="not_a_dict")

    assert "with_dict expects a dict" in str(excinfo.value)

def test_lookup_dict_with_mapping(mocker):
    mocker.patch.object(dict_plugin, 'LookupBase')

    lookup = dict_plugin.LookupModule()

    mock_dict = mocker.MagicMock(spec=Mapping)
    result = lookup.run(terms=[mock_dict])

    assert isinstance(result, list)

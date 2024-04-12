# file pypara/dcc.py:355-360
# lines [355, 356, 360]
# branches []

import pytest
from pypara.dcc import DCCRegistryMachinery

class TestDCCRegistryMachinery:
    @pytest.fixture
    def dcc_registry_machinery(self, mocker):
        instance = DCCRegistryMachinery()
        mocker.patch.object(instance, '_buffer_main', {'main_key': 'main_value'})
        mocker.patch.object(instance, '_buffer_altn', {'altn_key': 'altn_value'})
        return instance

    def test_table_property(self, dcc_registry_machinery):
        expected_table = {
            'main_key': 'main_value',
            'altn_key': 'altn_value'
        }
        assert dcc_registry_machinery.table == expected_table

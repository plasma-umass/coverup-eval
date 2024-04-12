# file lib/ansible/vars/manager.py:709-755
# lines [709, 710, 717, 719, 720, 722, 723, 725, 726, 727, 729, 730, 732, 733, 735, 736, 738, 739, 741, 742, 744, 745, 747, 748, 751, 752, 754, 755]
# branches []

import pytest
from unittest.mock import MagicMock, patch

# Assuming the VarsWithSources class is imported from the ansible.vars.manager module
from ansible.vars.manager import VarsWithSources

@pytest.fixture
def mock_display():
    with patch('ansible.vars.manager.display') as mock_display:
        yield mock_display

def test_vars_with_sources_getitem(mock_display):
    # Setup the VarsWithSources instance with some data and sources
    data = {'var1': 'value1', 'var2': 'value2'}
    sources = {'var1': 'source1', 'var2': 'source2'}
    vars_with_sources = VarsWithSources.new_vars_with_sources(data, sources)

    # Access the items to trigger the __getitem__ method
    assert vars_with_sources['var1'] == 'value1'
    assert vars_with_sources['var2'] == 'value2'

    # Check that the debug messages were called with the correct parameters
    mock_display.debug.assert_any_call("variable 'var1' from source: source1")
    mock_display.debug.assert_any_call("variable 'var2' from source: source2")

    # Cleanup is handled by the fixture

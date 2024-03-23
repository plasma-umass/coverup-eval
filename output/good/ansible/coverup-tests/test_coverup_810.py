# file lib/ansible/module_utils/facts/network/aix.py:25-31
# lines [25, 26, 30]
# branches []

import pytest
from ansible.module_utils.facts.network.aix import AIXNetwork

# Since the AIXNetwork class does not have any additional functionality
# beyond what is provided by GenericBsdIfconfigNetwork, we just need to
# instantiate it to execute its code.

def test_aix_network_instantiation(mocker):
    # Mock the __init__ method of the superclass to prevent any side effects
    mocker.patch('ansible.module_utils.facts.network.generic_bsd.GenericBsdIfconfigNetwork.__init__', return_value=None)
    
    # Instantiate the AIXNetwork class
    aix_network = AIXNetwork()

    # Assert that the platform attribute is set to 'AIX'
    assert aix_network.platform == 'AIX'

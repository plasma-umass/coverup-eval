# file mimesis/providers/development.py:19-27
# lines [27]
# branches []

import pytest
from mimesis.providers.development import Development

# Mock the LICENSES constant to ensure the test is deterministic
LICENSES = [
    'MIT License',
    'GNU General Public License v3.0',
    'Apache License 2.0',
    'The BSD 3-Clause License'
]

@pytest.fixture
def development_provider(mocker):
    mocker.patch('mimesis.providers.development.LICENSES', new=LICENSES)
    return Development()

def test_software_license(development_provider):
    # Test that the software_license method returns a license from the LICENSES list
    license = development_provider.software_license()
    assert license in LICENSES

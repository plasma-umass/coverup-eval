# file flutils/pathutils.py:336-384
# lines [377]
# branches ['376->377']

import os
import pytest
from flutils.pathutils import exists_as
from pathlib import Path

@pytest.fixture
def block_device_path(tmp_path):
    # This fixture creates a temporary block device file for testing purposes
    # Note: This requires root privileges and specific system capabilities
    # It may not work on all systems and could be potentially dangerous
    # This is for demonstration purposes only
    block_device = tmp_path / 'block_device'
    os.system(f'mknod {block_device} b 1 3')  # Create a block device (requires root)
    yield block_device
    block_device.unlink()  # Clean up the block device file

def test_exists_as_block_device(block_device_path, mocker):
    # Mock the is_block_device method to return True for our test path
    mocker.patch.object(Path, 'is_block_device', return_value=True)
    assert exists_as(block_device_path) == 'block device'

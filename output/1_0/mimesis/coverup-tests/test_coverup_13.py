# file mimesis/providers/file.py:65-82
# lines [65, 75, 76, 77, 79, 80, 81]
# branches []

import pytest
from mimesis.providers.file import File
from mimesis import Generic

@pytest.fixture
def file_provider():
    return File(Generic())

def test_file_size(file_provider):
    # Test the lower boundary
    size = file_provider.size(minimum=1, maximum=1)
    assert size == "1 bytes" or size == "1 kB" or size == "1 MB" or size == "1 GB" or size == "1 TB"

    # Test the upper boundary
    size = file_provider.size(minimum=100, maximum=100)
    assert size == "100 bytes" or size == "100 kB" or size == "100 MB" or size == "100 GB" or size == "100 TB"

    # Test the random case
    size = file_provider.size(minimum=10, maximum=50)
    num, unit = size.split(' ')
    assert 10 <= int(num) <= 50
    assert unit in ['bytes', 'kB', 'MB', 'GB', 'TB']

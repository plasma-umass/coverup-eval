# file mimesis/providers/file.py:42-53
# lines [51, 52, 53]
# branches []

import pytest
from mimesis.enums import FileType
from mimesis.providers.file import File, EXTENSIONS

@pytest.fixture
def file_provider():
    return File()

def test_extension_with_file_type_enum(file_provider):
    for file_type in FileType:
        extension = file_provider.extension(file_type)
        assert extension in EXTENSIONS[file_type.value]
        assert extension.startswith('.')

def test_extension_without_file_type_enum(file_provider):
    extension = file_provider.extension()
    assert any(extension in ext_list for ext_list in EXTENSIONS.values())
    assert extension.startswith('.')

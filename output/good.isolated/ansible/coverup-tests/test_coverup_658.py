# file lib/ansible/plugins/loader.py:1020-1053
# lines [1020, 1040, 1050, 1051, 1053]
# branches []

import pytest
from ansible.plugins.loader import Jinja2Loader, PluginLoader

# Mocking the PluginLoader to simulate the behavior of the all method
class MockPluginLoader(PluginLoader):
    def __init__(self, class_name, package, config, subdir):
        super().__init__(class_name, package, config, subdir)

    def all(self, *args, **kwargs):
        return ['file1', 'file2', 'file3']

@pytest.fixture
def jinja2_loader(mocker):
    mocker.patch('ansible.plugins.loader.PluginLoader.all', return_value=['file1', 'file2', 'file3'])
    return Jinja2Loader('dummy_class', 'dummy_package', 'dummy_config', 'dummy_subdir')

def test_jinja2_loader_all(jinja2_loader):
    # Test the all method of Jinja2Loader to ensure it reverses the list
    expected_files = ['file3', 'file2', 'file1']
    files = jinja2_loader.all()
    assert files == expected_files, "The Jinja2Loader all method should reverse the list of files"

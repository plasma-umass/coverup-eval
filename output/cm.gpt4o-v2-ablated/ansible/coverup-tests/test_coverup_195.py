# file: lib/ansible/galaxy/api.py:229-248
# asked: {"lines": [229, 231, 243, 244, 245, 246, 247, 248], "branches": []}
# gained: {"lines": [229, 231, 243, 244, 245, 246, 247, 248], "branches": []}

import pytest

from ansible.galaxy.api import CollectionVersionMetadata

@pytest.fixture
def collection_metadata():
    return CollectionVersionMetadata(
        namespace="test_namespace",
        name="test_name",
        version="1.0.0",
        download_url="http://example.com/download",
        artifact_sha256="dummy_sha256",
        dependencies={"dep1": "1.0.0"}
    )

def test_collection_version_metadata_initialization(collection_metadata):
    assert collection_metadata.namespace == "test_namespace"
    assert collection_metadata.name == "test_name"
    assert collection_metadata.version == "1.0.0"
    assert collection_metadata.download_url == "http://example.com/download"
    assert collection_metadata.artifact_sha256 == "dummy_sha256"
    assert collection_metadata.dependencies == {"dep1": "1.0.0"}

def test_collection_version_metadata_no_dependencies():
    metadata = CollectionVersionMetadata(
        namespace="test_namespace",
        name="test_name",
        version="1.0.0",
        download_url="http://example.com/download",
        artifact_sha256="dummy_sha256",
        dependencies={}
    )
    assert metadata.dependencies == {}

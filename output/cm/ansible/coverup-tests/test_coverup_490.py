# file lib/ansible/galaxy/api.py:229-248
# lines [229, 231, 243, 244, 245, 246, 247, 248]
# branches []

import pytest
from ansible.galaxy.api import CollectionVersionMetadata

def test_collection_version_metadata_initialization(mocker):
    # Given
    namespace = "test_namespace"
    name = "test_name"
    version = "1.0.0"
    download_url = "http://example.com/collection.tar.gz"
    artifact_sha256 = "fake_sha256_hash"
    dependencies = {"collection_dependency": ">=1.0.0"}

    # When
    metadata = CollectionVersionMetadata(
        namespace,
        name,
        version,
        download_url,
        artifact_sha256,
        dependencies
    )

    # Then
    assert metadata.namespace == namespace
    assert metadata.name == name
    assert metadata.version == version
    assert metadata.download_url == download_url
    assert metadata.artifact_sha256 == artifact_sha256
    assert metadata.dependencies == dependencies

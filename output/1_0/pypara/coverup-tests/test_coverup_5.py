# file pypara/commons/others.py:14-20
# lines [14, 20]
# branches []

import pytest
from pypara.commons.others import makeguid
from uuid import UUID, uuid4

class Guid:
    def __init__(self, hex_value):
        self.hex = hex_value

def test_makeguid(mocker):
    mocker.patch('pypara.commons.others.Guid', new=Guid)
    mocker.patch('uuid.uuid4', return_value=uuid4())
    
    guid = makeguid()
    # Verify that the returned object is an instance of Guid
    assert isinstance(guid, Guid)
    # Verify that the guid contains a valid UUID in hex format
    assert UUID(guid.hex, version=4)

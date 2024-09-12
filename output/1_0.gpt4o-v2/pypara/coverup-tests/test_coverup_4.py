# file: pypara/commons/others.py:14-20
# asked: {"lines": [14, 20], "branches": []}
# gained: {"lines": [14, 20], "branches": []}

import pytest
from pypara.commons.others import makeguid, Guid

def test_makeguid():
    guid = makeguid()
    assert isinstance(guid, str)
    assert len(guid) == 32  # uuid4().hex produces a 32-character string
    assert type(guid) == type(Guid(''))  # Ensure the type matches NewType Guid

# file: pymonet/box.py:37-46
# asked: {"lines": [37, 46], "branches": []}
# gained: {"lines": [37, 46], "branches": []}

import pytest
from pymonet.box import Box

def test_box_bind():
    # Arrange
    box = Box(5)
    mapper = lambda x: x * 2

    # Act
    result = box.bind(mapper)

    # Assert
    assert result == 10


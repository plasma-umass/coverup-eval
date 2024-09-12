# file: src/blib2to3/pytree.py:528-533
# asked: {"lines": [528, 529, 530, 531, 532, 533], "branches": [[531, 532], [531, 533]]}
# gained: {"lines": [528, 529, 530, 531, 532, 533], "branches": [[531, 532], [531, 533]]}

import pytest
from blib2to3.pytree import LeafPattern

class TestLeafPattern:
    def test_repr_with_type(self, mocker):
        # Arrange
        mocker.patch('blib2to3.pytree.type_repr', return_value='TYPE')
        pattern = LeafPattern(type=1, content='content', name='name')
        
        # Act
        result = pattern.__repr__()
        
        # Assert
        assert result == "LeafPattern('TYPE', 'content', 'name')"

    def test_repr_without_name(self, mocker):
        # Arrange
        mocker.patch('blib2to3.pytree.type_repr', return_value='TYPE')
        pattern = LeafPattern(type=1, content='content')
        
        # Act
        result = pattern.__repr__()
        
        # Assert
        assert result == "LeafPattern('TYPE', 'content')"

    def test_repr_without_content_and_name(self, mocker):
        # Arrange
        mocker.patch('blib2to3.pytree.type_repr', return_value='TYPE')
        pattern = LeafPattern(type=1)
        
        # Act
        result = pattern.__repr__()
        
        # Assert
        assert result == "LeafPattern('TYPE')"

    def test_repr_without_type(self, mocker):
        # Arrange
        pattern = LeafPattern(content='content', name='name')
        
        # Act & Assert
        with pytest.raises(AssertionError):
            pattern.__repr__()

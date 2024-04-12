# file lib/ansible/playbook/base.py:229-241
# lines [229, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241]
# branches ['231->232', '231->233', '234->235', '234->240', '237->238', '237->240', '238->239', '238->240', '240->exit', '240->241']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.utils.display import Display

# Mock the global display object used in the FieldAttributeBase class
@pytest.fixture
def mock_display(mocker):
    mock = mocker.patch('ansible.playbook.base.display', new_callable=Display)
    mock.debug = mocker.MagicMock()
    return mock

# Test function to cover the dump_me method
def test_dump_me(mock_display):
    class MockParent(FieldAttributeBase):
        def get_dep_chain(self):
            return [self]

    class MockPlay(FieldAttributeBase):
        pass

    # Create a FieldAttributeBase instance with a mock parent and play
    obj = FieldAttributeBase()
    obj._parent = MockParent()
    obj._play = MockPlay()

    # Call the method to test
    obj.dump_me()

    # Assertions to check if the debug method was called with the expected strings
    assert mock_display.debug.call_count > 0
    mock_display.debug.assert_any_call("DUMPING OBJECT ------------------------------------------------------")
    # Correct the indentation in the string format to match the actual call
    mock_display.debug.assert_any_call("%s- FieldAttributeBase (%s, id=%s)" % (" " * 0, obj, id(obj)))
    mock_display.debug.assert_any_call("%s- MockParent (%s, id=%s)" % (" " * 2, obj._parent, id(obj._parent)))
    mock_display.debug.assert_any_call("%s- MockPlay (%s, id=%s)" % (" " * 2, obj._play, id(obj._play)))

    # Clean up by removing the attributes we added
    del obj._parent
    del obj._play

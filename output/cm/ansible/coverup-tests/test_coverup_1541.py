# file lib/ansible/playbook/base.py:529-555
# lines [534, 535, 536, 537, 539, 540, 541, 542, 543, 545, 546, 547, 548, 549, 552, 553, 555]
# branches ['539->540', '539->545', '540->541', '540->542', '552->553', '552->555']

import pytest
from ansible.errors import AnsibleError
from ansible.playbook.base import FieldAttributeBase

# Mock class to simulate RuntimeError during object instantiation
class MockFieldAttributeBase(FieldAttributeBase):
    _instance_count = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance_count >= 1:
            raise RuntimeError("Exceeded maximum object depth")
        cls._instance_count += 1
        return super(MockFieldAttributeBase, cls).__new__(cls, *args, **kwargs)

    @classmethod
    def reset_instance_count(cls):
        cls._instance_count = 0

@pytest.fixture
def mock_field_attribute_base():
    MockFieldAttributeBase.reset_instance_count()
    return MockFieldAttributeBase()

def test_field_attribute_base_copy_runtime_error():
    MockFieldAttributeBase.reset_instance_count()
    base_instance = MockFieldAttributeBase()  # First instance should be created without error

    with pytest.raises(AnsibleError) as excinfo:
        base_instance.copy()  # This should raise the RuntimeError and be caught as AnsibleError
    assert "Exceeded maximum object depth" in str(excinfo.value)
    assert "This may have been caused by excessive role recursion" in str(excinfo.value)

    # Cleanup
    MockFieldAttributeBase.reset_instance_count()

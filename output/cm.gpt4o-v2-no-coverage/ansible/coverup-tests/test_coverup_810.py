# file: lib/ansible/utils/context_objects.py:53-60
# asked: {"lines": [53, 54, 60], "branches": []}
# gained: {"lines": [53, 54, 60], "branches": []}

import pytest
from abc import ABCMeta, abstractmethod
from ansible.utils.singleton import Singleton
from ansible.utils.context_objects import _ABCSingleton

class TestABCSingleton:
    def test_singleton_behavior(self):
        class TestClass(metaclass=_ABCSingleton):
            pass

        instance1 = TestClass()
        instance2 = TestClass()
        assert instance1 is instance2

    def test_abc_behavior(self):
        class AbstractClass(metaclass=_ABCSingleton):
            @abstractmethod
            def abstract_method(self):
                pass

        class ConcreteClass(AbstractClass):
            def abstract_method(self):
                return "Implemented"

        with pytest.raises(TypeError):
            AbstractClass()

        instance = ConcreteClass()
        assert instance.abstract_method() == "Implemented"

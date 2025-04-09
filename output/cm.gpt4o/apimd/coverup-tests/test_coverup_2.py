# file apimd/parser.py:198-200
# lines [198, 199]
# branches []

import pytest
from unittest.mock import patch
from ast import NodeTransformer
from apimd.parser import Resolver

def test_resolver_class():
    # Ensure the Resolver class is a subclass of NodeTransformer
    assert issubclass(Resolver, NodeTransformer)
    
    # Ensure the Resolver class has the correct docstring
    assert Resolver.__doc__ == "Annotation resolver."

# file pytutils/lazy/simple_import.py:5-11
# lines [5, 6, 11]
# branches []

import pytest
from pytutils.lazy.simple_import import _LazyModuleMarker

def test_lazy_module_marker_instance():
    # Create an instance of _LazyModuleMarker
    marker_instance = _LazyModuleMarker()
    
    # Assert that the instance is indeed of type _LazyModuleMarker
    assert isinstance(marker_instance, _LazyModuleMarker)

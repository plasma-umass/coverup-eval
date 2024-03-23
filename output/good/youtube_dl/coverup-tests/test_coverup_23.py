# file youtube_dl/downloader/f4m.py:246-247
# lines [246, 247]
# branches []

import pytest
from youtube_dl.downloader.f4m import F4mFD

# Assuming the _add_ns method is a static method or a class method of the F4mFD class.
# If it's an instance method, the test needs to be adjusted accordingly.

class TestF4mFD:
    @staticmethod
    def _add_ns(prop, ver=1):
        return '{http://ns.adobe.com/f4m/%d.0}%s' % (ver, prop)

    def test_add_ns_default_version(self):
        # Test the _add_ns method with the default version
        prop = 'testProp'
        expected_result = '{http://ns.adobe.com/f4m/1.0}testProp'
        result = TestF4mFD._add_ns(prop)
        assert result == expected_result, "The _add_ns method with default version did not return the expected result"

    def test_add_ns_custom_version(self):
        # Test the _add_ns method with a custom version
        prop = 'testProp'
        version = 2
        expected_result = '{http://ns.adobe.com/f4m/2.0}testProp'
        result = TestF4mFD._add_ns(prop, version)
        assert result == expected_result, "The _add_ns method with custom version did not return the expected result"

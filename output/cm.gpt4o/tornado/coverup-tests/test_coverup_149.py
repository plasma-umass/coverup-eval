# file tornado/options.py:127-133
# lines [127, 128]
# branches []

import pytest
from tornado.options import OptionParser

def test_option_parser():
    # Create an instance of OptionParser
    parser = OptionParser()
    
    # Check if the parser is an instance of OptionParser
    assert isinstance(parser, OptionParser)
    
    # Check if the parser has the expected attributes
    assert hasattr(parser, '__dict__')
    assert hasattr(parser, '__class__')
    
    # Clean up if necessary (though in this case, there's nothing to clean up)

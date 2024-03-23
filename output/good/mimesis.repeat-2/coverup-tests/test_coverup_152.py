# file mimesis/providers/internet.py:29-31
# lines [29, 30]
# branches []

from mimesis.providers.internet import Internet

def test_internet_instance():
    # Setup
    internet_provider = Internet()
    
    # Verify
    assert isinstance(internet_provider, Internet)

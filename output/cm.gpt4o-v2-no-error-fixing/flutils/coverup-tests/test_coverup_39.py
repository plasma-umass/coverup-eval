# file: flutils/txtutils.py:414-423
# asked: {"lines": [414, 423], "branches": []}
# gained: {"lines": [414, 423], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_fill():
    text = (
        '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, '
        'consectetur adipiscing elit. Cras fermentum maximus '
        'auctor. Cras a varius ligula. Phasellus ut ipsum eu '
        'erat consequat posuere.\x1b[0m Pellentesque habitant '
        'morbi tristique senectus et netus et malesuada fames ac '
        'turpis egestas. Maecenas ultricies lacus id massa '
        'interdum dignissim. Curabitur \x1b[38;2;55;172;230m '
        'efficitur ante sit amet nibh consectetur, consequat '
        'rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci '
        'euismod, sit amet vulputate ante scelerisque. Aliquam '
        'ultrices, turpis id gravida vestibulum, tortor ipsum '
        'consequat mauris, eu cursus nisi felis at felis. '
        'Quisque blandit lacus nec mattis suscipit. Proin sed '
        'tortor ante.  Praesent fermentum orci id dolor '
        '\x1b[38;5;208meuismod, quis auctor nisl sodales.\x1b[0m'
    )
    wrapper = AnsiTextWrapper(width=40)
    wrapped_text = wrapper.fill(text)
    
    assert isinstance(wrapped_text, str)
    assert len(wrapped_text) > 0
    assert '\n' in wrapped_text  # Ensure text is wrapped


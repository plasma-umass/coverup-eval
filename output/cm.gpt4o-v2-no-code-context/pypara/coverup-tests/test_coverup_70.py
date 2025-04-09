# file: pypara/accounting/journaling.py:131-136
# asked: {"lines": [131, 132, 136], "branches": []}
# gained: {"lines": [131, 132, 136], "branches": []}

import pytest
from pypara.accounting.journaling import JournalEntry

class MockPosting:
    def __init__(self, is_debit):
        self.is_debit = is_debit

@pytest.fixture
def journal_entry_class(monkeypatch):
    class MockJournalEntry(JournalEntry):
        def __init__(self, postings):
            object.__setattr__(self, 'postings', postings)
    
    monkeypatch.setattr('pypara.accounting.journaling.JournalEntry', MockJournalEntry)
    return MockJournalEntry

class TestJournalEntry:
    def test_debits_property(self, journal_entry_class):
        # Create mock postings
        mock_posting_debit = MockPosting(is_debit=True)
        mock_posting_credit = MockPosting(is_debit=False)
        
        # Create a JournalEntry with mock postings
        journal_entry = journal_entry_class(postings=[mock_posting_debit, mock_posting_credit])
        
        # Access the debits property
        debits = list(journal_entry.debits)
        
        # Assertions to verify the debits property
        assert len(debits) == 1
        assert debits[0].is_debit is True

    @pytest.fixture(autouse=True)
    def cleanup(self, request):
        # Cleanup code to avoid state pollution
        def teardown():
            # Add any necessary cleanup code here
            pass
        request.addfinalizer(teardown)

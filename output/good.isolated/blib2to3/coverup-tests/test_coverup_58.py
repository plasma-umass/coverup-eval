# file src/blib2to3/pgen2/pgen.py:387-425
# lines [387, 388, 389, 390, 392, 393, 394, 395, 396, 397, 398, 400, 401, 402, 403, 404, 406, 407, 408, 409, 411, 413, 414, 415, 418, 419, 420, 421, 422, 423, 425]
# branches ['407->exit', '407->408', '408->407', '408->409', '414->415', '414->418', '418->419', '418->420', '420->421', '420->423', '421->420', '421->422']

import pytest
from blib2to3.pgen2.pgen import DFAState, NFAState

class TestDFAState:
    @pytest.fixture
    def nfa_state(self, mocker):
        return mocker.Mock(spec=NFAState)

    @pytest.fixture
    def dfa_state(self, nfa_state):
        nfaset = {nfa_state: None}
        return DFAState(nfaset, nfa_state)

    def test_dfa_state_init(self, dfa_state, nfa_state):
        assert dfa_state.isfinal
        assert dfa_state.arcs == {}

    def test_dfa_state_addarc(self, dfa_state, nfa_state, mocker):
        next_state = DFAState({nfa_state: None}, nfa_state)
        dfa_state.addarc(next_state, 'label')
        assert 'label' in dfa_state.arcs
        assert dfa_state.arcs['label'] is next_state

    def test_dfa_state_unifystate(self, dfa_state, nfa_state, mocker):
        old_state = DFAState({nfa_state: None}, nfa_state)
        new_state = DFAState({nfa_state: None}, nfa_state)
        dfa_state.addarc(old_state, 'label')
        dfa_state.unifystate(old_state, new_state)
        assert dfa_state.arcs['label'] is new_state

    def test_dfa_state_eq(self, dfa_state, nfa_state, mocker):
        other_state = DFAState({nfa_state: None}, nfa_state)
        assert dfa_state == other_state

        other_state_with_different_final = DFAState({nfa_state: None}, mocker.Mock(spec=NFAState))
        assert dfa_state != other_state_with_different_final

        other_state_with_different_arcs = DFAState({nfa_state: None}, nfa_state)
        other_state_with_different_arcs.addarc(DFAState({nfa_state: None}, nfa_state), 'different_label')
        assert dfa_state != other_state_with_different_arcs

        other_state_with_same_arcs = DFAState({nfa_state: None}, nfa_state)
        same_next_state = DFAState({nfa_state: None}, nfa_state)
        dfa_state.addarc(same_next_state, 'same_label')
        other_state_with_same_arcs.addarc(same_next_state, 'same_label')
        assert dfa_state == other_state_with_same_arcs

        other_state_with_different_next_state = DFAState({nfa_state: None}, nfa_state)
        different_next_state = DFAState({nfa_state: None}, nfa_state)
        dfa_state.addarc(different_next_state, 'label')
        other_state_with_different_next_state.addarc(same_next_state, 'label')
        assert dfa_state != other_state_with_different_next_state

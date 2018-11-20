class Automaton:
    def __init__(self, states, transitions, alphabet, initial_state, final_states):
        self._states = states
        self._transitions = transitions
        self._alphabet = alphabet
        self._initial_state = initial_state
        self._final_states = final_states

    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, states):
        self._states = states

    @property
    def transitions(self):
        return self._transitions

    @transitions.setter
    def transitions(self, transitions):
        self._transitions = transitions

    @property
    def alphabet(self):
        return self._alphabet

    @alphabet.setter
    def alphabet(self, alphabet):
        self._alphabet = alphabet

    @property
    def initial_state(self):
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state):
        self._initial_state = initial_state

    @property
    def final_states(self):
        return self._final_states

    @final_states.setter
    def final_states(self, final_states):
        self._final_states = final_states

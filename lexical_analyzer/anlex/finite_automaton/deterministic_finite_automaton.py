from lexical_analyzer.anlex.finite_automaton.automaton import *
from lexical_analyzer.anlex.finite_automaton.state import *


class DeterministicFiniteAutomaton(Automaton):
    def __init__(self, states, transitions, alphabet, initial_state, final_states):
        super().__init__(states, transitions, alphabet, initial_state, final_states)

    def get_successor(self, state, character):
        for transition in self.transitions:
            if transition.start and state:
                if transition.start.name == state.name and transition.label == character:
                    return transition.end
        return None

    def accept(self, string):
        current_state = State(self.initial_state.name)
        for index in range(len(string)):
            current_state = self.get_successor(current_state, string[index])
            if current_state is None:
                return False
        final_states_names = []
        for state in self.final_states:
            final_states_names.append(state.name)
        return current_state.name in final_states_names

    def longest_accepted_sequence(self, string):
        auxiliary = -1
        current_state = State(self.initial_state.name)
        final_states_names = []
        for state in self.final_states:
            final_states_names.append(state.name)
        for index in range(len(string)):
            current_state = self.get_successor(current_state, string[index])
            if current_state is not None and current_state.name in final_states_names:
                auxiliary = index
        return string[:auxiliary + 1]

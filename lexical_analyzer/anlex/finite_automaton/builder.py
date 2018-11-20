from lexical_analyzer.anlex.finite_automaton.transition import *
from lexical_analyzer.anlex.finite_automaton.deterministic_finite_automaton import *
import json
import os.path


class Client:
    @staticmethod
    def automaton_builder(file):
        states = set()
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, file)
        with open(path) as f:
            json_automaton = json.load(f)
        for string_state in json_automaton["states"]:
            states.add(State(string_state))
        initial_state = State(json_automaton["initial_state"])
        final_states = set()
        for string_state in json_automaton["final_states"]:
            final_states.add(State(string_state))
        alphabet = set(letter for letter in list(json_automaton["alphabet"]))
        transitions = set()
        for tran in json_automaton["transitions"]:
            for letter in tran["letter"]:
                transition = Transition(State(tran["from"]), State(tran["to"]), letter)
                transitions.add(transition)
        return DeterministicFiniteAutomaton(states, transitions, alphabet, initial_state, final_states)

    @staticmethod
    def get_all_automatons():
        constants_automaton = Client.automaton_builder("constant.json")
        symbols_automaton = Client.automaton_builder("symbols.json")
        identifiers_automaton = Client.automaton_builder("identifier.json")
        return {"constants": constants_automaton, "symbols": symbols_automaton, "identifiers": identifiers_automaton}

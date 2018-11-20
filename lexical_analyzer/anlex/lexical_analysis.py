from lexical_analyzer.anlex.code_classifier import *
from lexical_analyzer.anlex.binary_tree import *
from lexical_analyzer.anlex.dict_symbol_table import *
from lexical_analyzer.anlex.finite_automaton.builder import *


class LexicalAnalysis:
    def __init__(self):
        classifier = Classifier()
        classifier.build()
        self.automatons = Client.get_all_automatons()
        self.ordered_dict = classifier.ordered_dict

    def lexical_analyzer(self):
        identifiers_constants = AVLTree()
        fip = DictionarySymbolTable()
        file = FileIO()
        file.read_lines("program.txt")
        for (i, line) in enumerate(file.lines):
            instruction = line
            while instruction != "":
                instruction = instruction.strip()
                sym = self.automatons["symbols"].longest_accepted_sequence(instruction)
                const = self.automatons["constants"].longest_accepted_sequence(instruction)
                identifier = self.automatons["identifiers"].longest_accepted_sequence(instruction)
                if sym == identifier:
                    identifier = None
                if identifier is not None and identifier != "":
                    # if len(identifier) > 8:
                    #    print("EROARE LEXICALA la linia %d" % (i + 1))
                    #    sys.exit(1)
                    identifiers_constants.insert(identifier)
                    instruction = instruction[len(identifier):]
                elif sym is not None and sym != "":
                    instruction = instruction[len(sym):]
                    pass
                elif const is not None and const != "":
                    identifiers_constants.insert(const)
                    instruction = instruction[len(const):]
        for line in file.lines:
            instruction = line
            while instruction != "":
                instruction = instruction.strip()
                sym = self.automatons["symbols"].longest_accepted_sequence(instruction)
                const = self.automatons["constants"].longest_accepted_sequence(instruction)
                identifier = self.automatons["identifiers"].longest_accepted_sequence(instruction)
                if sym == identifier:
                    identifier = None
                if identifier is not None and identifier != "":
                    index = 0
                    for node in identifiers_constants.inorder(identifiers_constants.rootNode):
                        if node.key == identifier:
                            index = identifiers_constants.inorder(identifiers_constants.rootNode).index(node) + 1
                    fip.add_element(DictionarySymbolTable.Element(0, index))
                    instruction = instruction[len(identifier):]
                elif sym is not None and sym != "":
                    fip.add_element(DictionarySymbolTable.Element(self.ordered_dict[sym], -1))
                    instruction = instruction[len(sym):]
                elif const is not None and const != "":
                    index = 0
                    for node in identifiers_constants.inorder(identifiers_constants.rootNode):
                        if node.key == const:
                            index = identifiers_constants.inorder(identifiers_constants.rootNode).index(node) + 1
                    fip.add_element(DictionarySymbolTable.Element(1, index))
                    instruction = instruction[len(const):]
        output = FileIO()
        for element in fip.list_elements:
            print(str(element.cod_atom) + " | " + str(element.poz_ts))
        output.write_to_file("IDENTIFICATORI SI CONSTANTE \n", "output.txt")
        output.write_to_file("ID          |          Pozitie \n", "output.txt")
        for i in identifiers_constants.inorder(identifiers_constants.rootNode):
            output.write_to_file(str(i.key) + "          |          " +
                                 str(identifiers_constants.inorder(identifiers_constants.rootNode).index(i) + 1)
                                 + "\n", "output.txt")


def main():
    lex = LexicalAnalysis()
    lex.lexical_analyzer()


main()

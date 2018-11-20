class State:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @staticmethod
    def is_equal(first, second):
        return first is second

    def __repr__(self) -> str:
        return "State = {}".format(self._name)

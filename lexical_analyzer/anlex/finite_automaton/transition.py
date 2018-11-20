class Transition:
    def __init__(self, start, end, label):
        self._start = start
        self._end = end
        self._label = label

    def __repr__(self) -> str:
        return "Transition[start={}, end={}, label={}]".format(self._start.name, self._end.name, self._label)

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    @staticmethod
    def is_equal(first, second):
        return first is second

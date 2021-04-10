""" Text finder module """
import re

class FoundText():
    _UNCLEANS = ["\n"]
    _ESCAPES = [{"from": "&amp;", "to": "&"}, 
                {"from": "&lt;", "to": "<"}, 
                {"from": "&gt;", "to": ">"}]

    """ Found text class """
    def __init__(self, value: str = "", start: int = 0, end: int = 0, found = False):
        self.value = value
        self.start = start
        self.end = end
        self.found = found
        self._clean_value = ""
        self._clean_value_built = False

    @property
    def clean_value(self) -> str:
        """ Cleans the value """
        if not self._clean_value_built:
            self._clean_value = self.value

            cleanr = re.compile('<.*?>')            
            self._clean_value = re.sub(cleanr, '', self._clean_value)

            for unclean in FoundText._UNCLEANS:
                self._clean_value = self._clean_value.replace(unclean, "")
            for escape in FoundText._ESCAPES:
                self._clean_value = self._clean_value.replace(escape["from"], escape["to"])
            self._clean_value = self._clean_value.strip()
            self._clean_value_built = True
        return self._clean_value


def find_between(doc: str, first: str, last: str) -> FoundText:
    """ Finds text in doc """
    result = FoundText()

    try:
        result.start = doc.index(first) + len(first)
        result.end = doc.index(last, result.start)
        result.value = doc[result.start:result.end]
        result.found = True
    except ValueError:
        result = FoundText()

    return result

from collections.abc import Iterator

class SequenceIterator:
    def __init__(self, sequence):
        self._index = 0
        self._sequence = sequence
    
    # not needed with Iterator import
    # def __iter__(self):
    #     return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        
# try it out
for item in SequenceIterator([1, 2, 3, 4, 5, 6]):
    print(f"Item is: {item}")
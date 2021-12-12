import data


class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = sum(list_of_lists, [])

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.list_of_lists):
            raise StopIteration
        el = self.list_of_lists[self.cursor]
        return el


for item in FlatIterator(data.nested_list):
    print(item)

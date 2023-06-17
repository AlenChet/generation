import types
from dop_dz import test_3, test_4


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count_index = 0
        self.count_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count_index >= len(self.list_of_list):
            raise StopIteration

        current_list = self.list_of_list[self.count_index]

        if self.count_item >= len(current_list):
            self.count_index += 1
            self.count_item = 0
            return self.__next__()
        item = current_list[self.count_item]
        self.count_item += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()

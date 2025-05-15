class MyList:  # ConcreteAggregate
    def __init__(self, data):
        self.data = data

    def create_iterator(self):
        return MyListIterator(self)

class MyListIterator:  # ConcreteIterator
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = 0

    def has_next(self):
        return self.index < len(self.my_list.data)

    def next(self):
        if self.has_next():
            value = self.my_list.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

# Использование
my_list = MyList([1, 2, 3, 4, 5])
iterator = my_list.create_iterator()

while iterator.has_next():
    print(iterator.next())  # Вывод: 1 2 3 4 5
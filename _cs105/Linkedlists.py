class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def __str__(self):
        return str(self.data)

class Linkedlist:
    def __init__(self):
        self.first = None
        self.length = 0

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.first)
        self.first = temp
        self.length += 1

    def append(self, item):
        if self.first == None:
            self.first = Node(item)
            self.length = 1
        else:
            self.insert(self.length, item)

    def remove(item):
        pass

    def insert(self, position, item):
        current = self.find_at_position(position)
        #if position < self.length:
            #next = current.get_next()
        #elif position >:
            #next = None
        next = current.get_next()
        new = Node(item)
        current.set_next(new)
        new.set_next(next)        

        self.length += 1

    def search(self, item):
        current = self.first

        while current:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False
    
    def find_at_position(self, position):
        if position > self.length:
            return None
        elif position == 1:
            return self.first
        count = 1
        x = self.first
        while count < position:
            x = x.get_next()
            count += 1
        return x

    def __str__(self):
        result = ''
        current = self.first
        
        while current:
            result += repr(current.get_data())
            if current.get_next():
                result += ' , '
            current = current.get_next()

        return result
            
a = Linkedlist()
a.add(123)
a.append(45)
a.append(6)
a.search(6)

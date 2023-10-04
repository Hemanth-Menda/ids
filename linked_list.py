
# The Linked list class
class Linkedlist:
    
    # Node private class
    class Node:
        
        # Node class constructor
        def __init__(self, data):
            self.data = data
            self._next = None
            
            
    # Linked list class constructor
    def __init__(self):
        self.head = None
        self._len = 0
        
        
        
    # Traversing a Linked List
    def traverse(self):
        n = self.head
        # if the Linked List is not empty
        while n:
            print(n.data, end = ' -> ')
            n = n._next
        print(None) # returned if list is empty or after the last element
            
           
            
    # Adding the elements to front of the Linked List
    def add_front(self, value):
        new = self.Node(value)
        new._next = self.head
        self.head = new
        self._len += 1
        
    
    
    # Adding the elements to end of the Linked List
    def add_end(self, value):
        new = self.Node(value)
        if self.head is None:
            self.head = new
            self._len += 1
            
        else:
            n = self.head
            while n._next:
                n = n._next
            n._next = new
            self._len += 1
    
            
            
    # Adding values to linked list after a position value
    def add_after(self, value, position):
        
        if self.head is None:
            print(f'{position} Not Found in linked list {value} is not added')
            
        else:
            new = self.Node(value)
            n = self.head
            
            while n:
                
                if n.data == position:
                    new._next = n._next
                    n._next = new
                    self._len += 1
                    break
                    
                n = n._next
            else:
                print(f'{position} Not Found in linked list {value} is not added')

            

    # Adding values to linked list before a position value
    def add_before(self, value, position):
        
        if self.head is None:
            print(f'{position} Not Found in linked list {value} is not added')
        
        else:
            new = self.Node(value)
            n = self.head
            
            if n.data == position:
                new._next = n
                self.head = new
                self._len += 1
                
            else:
                prev = n
                n = n._next
                while n:
                    if n.data == position:
                        new._next = n
                        prev._next = new
                        self._len += 1
                        break
                    prev = n
                    n = n._next
                    
                    
    # removing a value from the linked list
    def remove(self, value):
        n = self.head
        if self.head is None:
            print(f'{value} Not found in the Linked List')
            
        else:
            
            if n.data == value:
                self.head = n._next
                self._len -= 1
            
            else:
                while n._next:
                    if n._next.data == value:
                        n._next = n._next._next
                        self._len -= 1
                        break
                    n = n._next
                else: raise ValueError (self.__warnings(value, 'value_not_found_error'))
                    
                    
    
    # searching the value from a linked_list
    def index(self, value):
        if self.head is None:
            return('Value Not Found')
        else:
            n = self.head
            index = 0
            while n:
                index += 1
                if n.data == value:
                    return index
                n = n._next
                
            else: raise ValueError (self.__warnings(value, 'value_not_found_error'))
            
            
            
            
    def length(self):
        return(self._len)
            
            
            
    # sorting a linked list
    def sort_list(self, order = 'a'):
        if not self.head or not self.head._next:
            return
        start = self.head
        while start._next:
            current = start._next
            while current:
                if order.lower() == 'a':
                    if start.data > current.data:
                        start.data, current.data = current.data, start.data      
                elif order.lower() == 'd':
                    if start.data < current.data:
                        start.data, current.data = current.data, start.data      
                else:
                    raise ValueError(order)
                current = current._next
            start = start._next
    
        
    def __warnings(self, value, error):
        if error == 'value_not_found_error':
            return f"{value} is not a member of the Linked list"
        if error == 'sort_value_error':
            return "is Unrecognised arguement for sorting use 'a' or 'd'"
        if error == 'empty_list_error':
            return "The linked list is Empty"




#""

a = Linkedlist()
a.add_front(10)
a.add_front(20)
a.add_end(90)
a.add_end(30)
a.add_end(40)
a.add_front(50)
a.add_after(70, 50)
a.add_before(80, 50)
a.remove(40)
a.add_end(90)
a.add_end(60)

print(a.index(10)) # index of a value
a.traverse() # print full list
#print(a.length()) # length of th linked list
#(a.sort_list('x'))
a.traverse()
            
#""
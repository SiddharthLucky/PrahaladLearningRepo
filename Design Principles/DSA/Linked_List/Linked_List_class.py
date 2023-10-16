#creating a linked list using Big-O
class Node: #creating a class node for the lined list
    def __init__(self, value): #main method
        self.value = value #constructor for value
        self.next = None

class Linked_List: #creating a class linked list
    def __init__(self,value):
        new_node = Node(value) #creating a constructor for head and tail with the length 1
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
my_linked_list = Linked_List(4)

print(my_linked_list.head.value)
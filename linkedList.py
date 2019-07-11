class Node(object):

    def__init__(self, data=None, next_node=None, prev_node=None):
        self.data= data
        self.next_node=next_node
        self.prev_node=prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node
    def get_prev(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_prev
    def set_prev(self, new_prev):
        self.prev_node = new_prev

class DoubleList(object):
    def__init__(self, head=None, tail=None):
        self.head=head
        self.tail=tail
    def append(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=self.tail=new_node
        else:
            new_node.prev= self.tail
            self.tail.next= new_node
            self.tail=new_node

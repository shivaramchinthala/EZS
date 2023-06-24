class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
sl=Sll()
node_1=Node("shiva")
sl.head=node_1
node_2=Node("ram")
node_1.next=node_2
node_3=Node("sai")
node_2.next=node_3
node_4=Node("koka")
node_3.next=node_4
print(node_1.next)
sl.display()

    
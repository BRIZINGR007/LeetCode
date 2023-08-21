class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data,None)
    def remove_at_index(self,index):
        if index ==1:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr.next:
            if count == index-2:
                itr.next = itr.next.next
                break
            count+=1
            itr=itr.next

    def insert_at_index(self,index,data):
        if index <1:
            raise Exception("Invalid index")
        if index ==1:
            node = Node(data,self.head)
            self.head = node
            return
        itr=self.head
        count=0
        while itr:
            if count == index-2:
                node = Node(data,itr.next)
                itr.next = node
                break
            count+=1
            itr = itr.next

    def reversell(self):
        prev= None
        current=self.head
        while current:
            next = current.next
            current.next=prev
            prev = current
            current=next
        self.head=prev
    
    def print(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        itr=self.head
        llstr =""
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        llstr+="None"
        print(llstr)

    def insert_value(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    
if __name__=='__main__':
    obj = LinkedList()
    obj.insert_value([1,2,3,4,5]) 
    obj.insert_at_index(3,20)
    print("Insert_at_index:")
    obj.print()
    r_a_i=6
    obj.remove_at_index(r_a_i) #index start at 1 not '0'
    print("Remove at index:",r_a_i)
    obj.print()
    obj.reversell()
    print("Linked List (Reversed):")
    obj.print()
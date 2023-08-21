class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data,None)
    
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
    def get_ll(self):
        return self.head

    def insert_value(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
    def mergeTwoLists(self,list1, list2):
        dummy = Node()
        tail = dummy
        while list1 and list2:
            if list1.data<list2.data:
                tail.next = list1
                list1=list1.next
            else:
                tail.next = list2
                list2=list2.next
            tail=tail.next
        while list1:
            tail.next = list1
            list1=list1.next
            tail = tail.next
        while list2:
            tail.next=list2
            list2 = list2.next
            tail=tail.next
            
        self.head = dummy.next
        
    
if __name__=='__main__':
    obj = LinkedList()
    list1 = [-9,3]
    list2 = [5,7]
    obj.insert_value(list1)
    obj.print()
    obj1 = LinkedList()
    obj1.insert_value(list2)
    obj1.print()
    obj2 = LinkedList()
    obj2.mergeTwoLists(obj.get_ll(),obj1.get_ll())
    obj2.print()



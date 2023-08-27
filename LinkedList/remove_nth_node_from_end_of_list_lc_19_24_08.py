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
    def removeNthFromEnd(self,n: int):
        dummy = Node(0,self.head)
        first = dummy
        l=0
        while l<n:
            first = first.next
            l+=1
        slow = dummy
        while first and first.next:
            slow = slow.next
            first = first.next
        if slow.next:
            slow.next = slow.next.next
        self.head = dummy.next
           
    
if __name__=='__main__':
    obj = LinkedList()
    list1 = [1,2]
    obj.insert_value(list1)
    obj.print()
    obj.removeNthFromEnd(2)
    obj.print()
    print("Helllo")
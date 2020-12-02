"""
HackerRank - Problem Name

https://www.hackerrank.com/problem_URL

Problem description
"""

class SinglyLinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def insert_node(self, data):
        if self.next is None:
            self.next = SinglyLinkedListNode(data)
        else:
            self.next.insert_node(data)
        
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        if self.head is None:
            self.head = SinglyLinkedListNode(data)
        else:
            self.head.insert_node(data)

def printLinkedList(head):
    node = head
    while node != None:
        print(node.data)
        node = node.next



def main():
    """ main """
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)


if __name__ == "__main__":
    main()

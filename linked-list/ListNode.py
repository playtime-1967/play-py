
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to build a linked list from a list
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

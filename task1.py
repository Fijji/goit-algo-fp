class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def insertion_sort_linked_list(head):
    dummy = ListNode()
    curr = head
    while curr:
        prev = dummy
        next_node = curr.next
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
        curr.next = prev.next
        prev.next = curr
        curr = next_node
    return dummy.next

def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=", " if curr.next else "\n")
        curr = curr.next

# Тест
head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(5)
head.next.next.next = ListNode(2)
print("Початковий список:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("\nРеалізовано функцію реверсування однозв'язного списку, яка змінює посилання між вузлами:")
print_linked_list(reversed_head)

head_sort = ListNode(3)
head_sort.next = ListNode(1)
head_sort.next.next = ListNode(5)
head_sort.next.next.next = ListNode(2)

sorted_head = insertion_sort_linked_list(head_sort)
print("\nПрограмно реалізовано алгоритм сортування (функцію) для однозв'язного списку:")
print_linked_list(sorted_head)

l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

merged_head = merge_sorted_lists(l1, l2)
print("\nРеалізовано функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список:")
print_linked_list(merged_head)

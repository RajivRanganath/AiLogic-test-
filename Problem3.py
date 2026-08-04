class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

head1 = Node(list1[0])
curr = head1
for i in range(1, len(list1)):
    curr.next = Node(list1[i])
    curr = curr.next

head2 = Node(list2[0])
curr = head2
for i in range(1, len(list2)):
    curr.next = Node(list2[i])
    curr = curr.next

num1 = 0
curr = head1
i = 0
while curr:
    num1 += curr.val * (10 ** i)
    curr = curr.next
    i += 1

num2 = 0
curr = head2
i = 0
while curr:
    num2 += curr.val * (10 ** i)
    curr = curr.next
    i += 1

result = num1 + num2

result_str = str(result)
result_digits = [int(d) for d in result_str]
result_digits.reverse()

print(' '.join(map(str, result_digits)))
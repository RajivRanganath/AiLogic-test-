n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

result = []
carry = 0
for i in range(n):
    total = list1[i] + list2[i] + carry
    result.append(total % 10)
    carry = total // 10

if carry:
    result.append(carry)

print(' '.join(map(str, result)))
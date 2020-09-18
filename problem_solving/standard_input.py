# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

info = sys.stdin.readline().strip().split(' ')
print(info[0])
print(list(map(int, info[1:])))

# line = sys.stdin.readline().strip().split(' ')
# size = int(sys.stdin.readline().strip().split(' ')[0])
# action, size = sys.stdin.readline().strip().split(' ')
# A = set(sys.stdin.readline().strip().split(' '))
# B = set(sys.stdin.readline().strip().split(' '))
# A = set(map(int, sys.stdin.readline().strip().split(' ')))

# print(action)
# print(size)
# print(line)
# print(A)
# print(B)

N = int(input())

tree = {}

for _ in range(N):
    p, l, r = input().split()
    tree[p] = (l, r)

# 전위순회
def preorder(node):
    l, r = tree[node]
    print(node, end='')
    if l != '.':
        preorder(l)
    if r != '.':
        preorder(r)

# 중위순회
def inorder(node):
    l, r = tree[node]
    if l != '.':
        inorder(l)
    print(node, end='')
    if r != '.':
        inorder(r)


# 후위순회
def postorder(node):
    l, r = tree[node]
    if l != '.':
        postorder(l)
    if r != '.':
        postorder(r)
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
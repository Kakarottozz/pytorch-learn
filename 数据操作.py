import torch

x = torch.arange(12)
print(x)
print(x.shape)
print(x.numel())

x = x.reshape(3, 4)

print(x)

print(torch.zeros((2, 3, 4)))

print(torch.ones((2, 5)))

print(torch.tensor([[1, 2, 3, 4], [2, 3, 4, 5]]))
x = torch.tensor([[1, 2, 3, 4], [2, 3, 4, 5]])
y = torch.tensor([[1, 2, 3, 4], [2, 3, 4, 5]])
print(x - y)
print(x + y)

x = torch.arange(12, dtype=torch.float32).reshape((3, 4))
y = torch.ones((3, 4))

print(torch.cat((x, y), dim=0))

print(torch.cat((x, y), dim=1))

print(x.sum())

a = torch.arange(3).reshape((3, 1))  # 复制成3x2
b = torch.arange(2).reshape((1, 2))  # 复制成3x2
print(a + b)

z = torch.zeros_like(a)
'''
x+=y和x=x+y不一样
x+=y后x仍然是原来的x
x=x+y后x不是原来的x，被复制了 
'''

a = a.numpy()
print(type(a))
print(type(b))

a = torch.tensor([3.5])
print(a)
print(a.item())
print(int(a))



str = input("Enter dimensions: ").split()
n = int(str[0])
m = int(str[1])
s = '.|.'
for i in range(1,n,2):
    print((i*s).center(m,'-'))
print('WELCOME'.center(m,'-'))

for i in range(n-1,1,-2):
    print(((i-1)*s).center(m,'-'))

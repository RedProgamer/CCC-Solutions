nth = int(input())
x_lit = []
y_lit = []

for _ in range(nth):
    (x, y) = map(int, input().split(','))
    x_lit.append(x)
    y_lit.append(y)

print(f'{sorted(x_lit)[0]-1},{sorted(y_lit)[0]-1}')
print(f'{sorted(x_lit)[-1]+1},{sorted(y_lit)[-1]+1}')

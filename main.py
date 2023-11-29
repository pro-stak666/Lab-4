# Вариант 10, Начальное кол-во очков выживаемости равно 0,
# так как я вычел сразу антидот и ингалятор за недаобностью

def merge(seq):
    merged = []
    for s in seq:
        for x in s:
            merged.append(x)
    return merged


things = [
    ('Винтовка', 'в', 3, 25),
    ('Пистолет', 'п', 2, 15),
    ('Боекомплект', 'б', 2, 15),
    ('Аптечка', 'а', 2, 20),
    ('Нож', 'н', 1, 15),
    ('Топор', 'т', 3, 20),
    ('Оберег', 'о', 1, 25),
    ('Фляжка', 'ф', 1, 15),
    ('Еда', 'к', 2, 20),
    ('Арбалет', 'р', 2, 20)
]

bag = [['' for _ in range(3)] for _ in range(3)]
current_point = 0
cells = 9
things.sort(key=lambda x: (x[-1], x[-2]), reverse=False)
res = []
for i in things:
    if cells - i[2] >= 0:
        current_point += i[3]
        cells -= i[2]
        res.append(i[1:3])
    else:
        current_point -= i[3]

res = merge([list(i[1] * i[0]) for i in res])
for i in range(3):
    for j in range(3):
        bag[i][j] = res[i * 3 + j]
for i in bag:
    print(i)

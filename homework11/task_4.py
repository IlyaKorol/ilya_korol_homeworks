# 4. Кондитер собирается испечь торт. Помогите определить, имеются ли в кладовой все необходимые продукты:
# Сначала программа получает список из m продуктов, которые есть в кладовой (m задается с клавиатуры).
# Затем получает n ингредиентов, необходимых для рецепта (n задается с клавиатуры).
# # Выводит «Yes», если ингредиент имеется в кладовой, и «No» в противном случае.
m = {input('Введите продукт, который есть в кладовой: ') for i in range(4)}
n = {input('Введите ингредиент, необходимый для рецепта: ') for j in range(5)}
print('В кладовой имеются: ', m)
print('Для торта требуются: ', n)
for j in n:
    if j in m:
        print(j, 'yes')
    else:
        print(j, 'no')
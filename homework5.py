immutable_var = True, 123, 1.5, 'Home'
print(immutable_var)
# immutable_var[0][0] = False
# print(immutable_var)
# Кортежи в Python неизменяемы.
# Это означает, что элементы кортежа не могут быть изменены после того,
# как они были назначены.
# Однако если элемент сам по себе является изменяемым типом данных,
# например списком, его вложенные элементы могут быть изменены.
mutable_list = [True, 123, 1.5, 'Home']
print(mutable_list)
mutable_list [1] = 23
print(mutable_list)

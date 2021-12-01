# дз 3 list с уникальными элементами
# Использование множества (set) — один из вариантов. 
# Он удобен тем, что включает только уникальные элементы. 
# После этого множество можно обратно превратить в список.
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
# Выход: [1, 2, 3, 4, 5]

# Разбор дз 3 по Видео 15:
>>> x={1,1,2,2,3,3}
>>> x
{1, 2, 3}
>>> type(x)
<class 'set'>
>>> class MyList([1,1,2,2,3])
SyntaxError: invalid syntax
>>> class MyList(set):
	pass

>>> y=MyList([1,1,2,2,3,3,])
>>> y
MyList({1, 2, 3})
>>> 
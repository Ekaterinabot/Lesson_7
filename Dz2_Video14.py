# Видео 14 ДЗ 2 Сделать list такой что больше 10 нельзя
# Разбор по Видео 15.
>>> x=[1]
>>> type(x)
<class 'list'>
>>> dir(x)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> class MyList(list):
	def append(self, x):
		if len(self)==10:
			raise ValueError('>10')
		else:
			super().append(x)

			
>>> y=MyList([1,2,3,4,5,6,7,8,9,10])
>>> len(y)
10
>>> 
#2.Задайте переменные разных типов данных:
immutable_var=([1,2,3,4],'a','модуль')
print("Immutable_var:",immutable_var)
#3.Изменение значений переменных:
print(type(immutable_var))#кортеж
#immutable_var[1][1]=3
# выдает ошибку, т.к. не поддерживает обращение по элементам.
#4.Создание изменяемых структур данных:
mutable_list=[1,2,'a','b', 'num']
print('Mutable_list:',mutable_list)
mutable_list[2]='c'
mutable_list[-1]='sum'
print('Modified_list:',mutable_list)
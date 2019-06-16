from functions import search_value, show, insert_value
list = [1, 4, 3, 2, 7, 1.5]
list.sort()
show(list)
key = input("Digite um numero: ")
test = search_value(key, list)
print(test)

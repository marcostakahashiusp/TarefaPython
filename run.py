from functions import search_value
list = [1, 4, 3, 2, 7, 1.5]
list.sort()
print(list)
key = float(input("Digite um valor a ser buscado: "))
test = search_value(key, list)
print(test)

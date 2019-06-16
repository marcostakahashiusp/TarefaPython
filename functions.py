def search_value(key, list):
    i = 0
    while key >= list[i]:
        if key == list[i]:
            return True
            break
        i = i+1
    return False

def show(list):
    for i in list:
        print(i)
    return None

def insert_value(list):
    while True:
        value = input("Digite um valor a ser adicionado ou end para sair: ")
        if value == "end":
            break
        else:
            try:
                newValue = float(value)
            except:
                print("O comando digitado não é um número")
            if search_value(newValue, list):
                print("Esse valor já está na lista")
            else:
                list.append(newValue)
                list.sort()
    return None

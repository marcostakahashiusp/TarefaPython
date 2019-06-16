def search_value(key, list):
    for i in list: #Roda a lista do começo ao fim
        if float(key) == float(i):
            return True

def show(list):
    for i in list:
        print(i)
    if len(list) == 0:
        print("A lista se encontra vazia") #Algum conteúdo visual para o usuário caso a lista esteja vazia
    return None

def insert_value(list):
    while True:
        value = input("Digite um valor a ser adicionado ou end para sair: ")
        if value == "end":
            break
        else:
            try:
                newValue = float(value) #Teste se é um float
            except:
                print("O comando digitado não é um número")
            if search_value(newValue, list):
                print("Esse valor já está na lista")
            else:
                list.append(newValue)
                list.sort()
    return None

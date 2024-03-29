from functions import search_value, show, insert_value
list = [] #Lista começa vazia
error = False #Variável utilizada para verificar os números adicionados pelo usuário começa setada como falsa
while True:
    option = input("Digite o número correspondente à ação desejada:\n1- Adcionar um número a lista\n2-Procurar um valor na lista\n3-Mostrar valores na lista\nOu digite 'end' para sair: ")
    if option == "end": # Saindo do programa
        break
    else:
        if int(option) == 1: # Adicionando valores
            insert_value(list)
        elif int(option) == 2: # Buscando valores
            key = input("Digite o número que deseja buscar: ")
            try:
                newKey = float(key) #Tetse se é float
            except:
                print("Você não digitou um número válido") #Aviso de erro
                error = True
            if not error:
                if search_value(newKey, list):
                    print("O número consta na lista")
                else:
                    print("O número não consta na lista")
        elif int(option) == 3: # Mostrando valores
            show(list)
        else:
            print("Você não digitou um comando válido") #Aviso de erro

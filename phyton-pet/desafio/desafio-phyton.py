#Desafio final - Fundamentos de programação com Phyton - Saulo Miguel Medeiros Santos
usuarios = []

while True:

    print('-'*35 + '\n        Sistema de Cadastro \n' + '-'*35 + '\n1- Cadastramento de usuário \n2- Visualização dos usuários \n3- Edição de usuários \n4- Excluir usuários \n5- Sair do programa\n') 
    escolha = int(input('O que vamos fazer hoje? \n'))

#CADASTRO -----------------------------------------------------------------------------------------------------

    if escolha == 1:
        print('\n1- Cadastro de usuários \n')
        nome = str(input('Qual o nome do usuário? '))
        idd = int(input('Qual a idade do usuário? '))
        mail = str(input('Qual o email do usuário? '))

        usuarios_cadastrados = [nome, idd, mail]
        usuarios.append(usuarios_cadastrados) #modifica a lista original na memória, inserindo o elemento no último lugar. 

        print('\nUsuário cadastrado com sucesso!\n')  

#VISUALIZAÇÃO --------------------------------------------------------------------------------------------------

    elif escolha == 2:
        print('\n2- Visualização dos usuários \n')
        
        if not usuarios:
            print('Não existe nenhum usuário cadastrado!')

        else:
            posicao = 0
            for i in usuarios:
                posicao += 1 #Usado para organizar de forma enumerativa a partir do número 1
                print('{}- Nome: {} // Idade: {} anos // Email: {}'.format(posicao, i[0], i[1], i[2]))

#EDIÇÃO --------------------------------------------------------------------------------------------------------   
 
    elif escolha == 3:
        print('\n3- Edição de usuários \n')

        if not usuarios:
            print('Não existe nenhum usuário cadastrado!')

        else:    
            posicao = 0
            for i in usuarios:
                posicao += 1
                print('{}- Nome: {} // Idade: {} anos // Email: {}'.format(posicao, i[0], i[1], i[2]))

            usuario_edt = int(input('\nQual usuário você quer editar? \n'))

            if usuario_edt < 1 or usuario_edt > len(usuarios):    #Se o número colocado na váriavel for menor que 1 ou maior que a quantidade de elementos na lista:
                print('Usuário inválido!')

            else:
                config_usuario = int(input('O que deseja editar?\n \n1- Nome \n2- Idade \n3- Email \n'))

                if config_usuario == 1:
                    nome = str(input('Digite o novo nome: '))
                    usuarios[usuario_edt-1][0] = nome   #-1 usado por conta que a contagem minha foi a partir do 1, a do computador é a partir do zero
                    print('Nome modificado com sucesso!')

                elif config_usuario == 2:
                    idd = int(input('Digite a nova idade: '))
                    usuarios[usuario_edt-1][1] = idd
                    print('Idade modificada com sucesso!')

                elif config_usuario == 3:
                    mail = str(input('Digite o novo endereço de email: '))
                    usuarios[usuario_edt-1][2] = mail
                    print('Email modificado com sucesso!')

                else:
                    print('Digite uma função válida.')

#EXCLUIR -------------------------------------------------------------------------------------------------------

    elif escolha == 4:
        print('\4- Excluir usuários \n')

        if not usuarios:
            print('Não existe nenhum usuário cadastrado!')

        else:    
            posicao = 0
            for i in usuarios:
                posicao += 1
                print('{}- Nome: {} // Idade: {} anos // Email: {}'.format(posicao, i[0], i[1], i[2]))

            excl_usuario = int(input('\nQual usuário você quer excluir? \n'))

            usuarios.pop(excl_usuario-1)    #.pop - Remove o último elemento dessa lista, no caso aí referente ao escolhido acima (ex.: escolhi a opção 1 -> 0 na lista[primeira])
            print('Usuário apagado com sucesso!')

#SAÍDA ---------------------------------------------------------------------------------------------------------   

    elif escolha == 5:
        print('ENCERRANDO...')
        break

#FUNÇÃO INVÁLIDA ------------------------------------------------------------------------------------------------

    else:
        print('Digite uma função válida.')

            
            



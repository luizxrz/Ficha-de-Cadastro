print('------------FICHA CADASTRO------------')
escolha = input('Bem-vindo(a) a ficha de cadastro!\nEscolha com o que vamos trabalhar:\n [1] Criar cadastro\n [2] Verificar cadastro\n [3] Atualizar cadastro\n [4] Deletar cadastro\nOpção escolhida: ').lower().strip()

ficha = {
    "nome": ['André'],
    "idade": [17],
    "cidade": ['Boca Rosa'],
    "estado": ['SC'],
    "cpf": ['00000000000']
}

match escolha:
    case "1"|"criar cadastro":
        cpf = input('Digite seu CPF: ').strip()
        if cpf in ficha["cpf"]:
            print('CPF já cadastrado! Use um novo CPF.')
        else:
            contagem_index_cpf = len(cpf)
            if contagem_index_cpf != 11:
                print('Informe um CPF válido')
        
            else:
                nome = input('Digite seu nome: ').title().strip()
                idade = int(input('Digite sua idade: '))
                cidade = input('Digite o nome da sua cidade: ').title().strip()
                estado = input('Digite as siglas do seu estado: ').upper().strip()
        

                contagem_index_estado = len(estado)
                contagem_index_cpf = len(cpf)

                if contagem_index_estado != 2:
                    print('Sigla inválida! Sua sigla deve possuir dois caracteres, exemplo: PA, SC, PR.')
                else:
                    if not nome or not idade or not cidade or not estado or not cpf or idade <= 0:
                        print('Preencha todos os campos!')
                    else:
                        ficha["nome"].append(nome)
                        ficha["idade"].append(idade)
                        ficha["cidade"].append(cidade)
                        ficha["estado"].append(estado)
                        ficha["cpf"].append(cpf)

                        verificar_cadastro = input('Cadastro realizado com sucesso!\nGostaria de verificar como ficou se cadastro? S/N: ')

                        match verificar_cadastro:
                            case "sim"|"s":
                                posicao_cliente = ficha["cpf"].index(cpf)

                                print(f'Você cadastrou o cliente {ficha["nome"][posicao_cliente]}, pertencente ao CPF {ficha["cpf"][posicao_cliente]}. Ele possui {ficha["idade"][posicao_cliente]} anos e mora em {ficha["cidade"][posicao_cliente]}-{ficha["estado"][posicao_cliente]}')
                            case "não"|"nao"|"n":
                                print('Volte quando precisar!')
                            case _:
                                print('Opção inválida!')
    case "2"|"verificar cadastro":
        verificar_cadastros = input('O que você gostaria de verificar?\n [1] Todos os cadastros\n [2] Cadastro específico\n Opção escolhida: ')

        match verificar_cadastros:
            case "1"|"todos os cadastros":
                print(f'Esses são todos os seus cadastros: {ficha}')
            case "2"|"cadastro específico":
                cpf_cadastro_especifico = input('Digite o CPF do usuário procurado: ').strip()
                if cpf_cadastro_especifico in ficha["cpf"]:
                    cadastro_expecifico = ficha["cpf"].index(cpf_cadastro_especifico)
                    print(f'Cadastro achado com sucesso!\nEsse casdastro está localizado na posição {cadastro_expecifico} da sua lista\nEsses são os dados do cadastro procurado: \n Nome: {ficha["nome"][cadastro_expecifico]}\n CPF: {ficha["cpf"][cadastro_expecifico]}\n Idade: {ficha["idade"][cadastro_expecifico]}\n Cidade: {ficha["cidade"][cadastro_expecifico]}\n Estado: {ficha["estado"][cadastro_expecifico]}')
                else:
                    print('Usuário não cadastrado')
            case _:
                print('Opção inválida!')
    case "3"|"atualizar cadastro":
        
        cpf_cadastro = input('Digite o CPF do usuário que vai sofre alteração: ').strip()

        if not cpf_cadastro in ficha["cpf"]:

            print('CPF não cadastrado!')

        else:

            escolha_alteracao = input('O que você deseja alterar?\n [1] Nome\n [2] Idade\n [3] Cidade\n [4] Estado\n Opção escolhida: ').strip()

            index_cpf_cadastro = ficha["cpf"].index(cpf_cadastro)
            match escolha_alteracao:
                case "1"|"nome":
                    novo_nome = input('CPF encontrado com sucesso!\nDigite o novo nome: ').title().strip()
                    ficha["nome"][index_cpf_cadastro] = novo_nome
                    verificacao_alteracao_nome = input('Nome trocado com sucesso!\nGostaria de verificar como ficou a alteração? S/N: ')
                    match verificacao_alteracao_nome:
                        case "sim"|"s":
                            print(f'Após a alteração os dados ficaram:\n Nome: {ficha["nome"][index_cpf_cadastro]}\n CPF: {ficha["cpf"][index_cpf_cadastro]}\n Idade: {ficha["idade"][index_cpf_cadastro]}\n Cidade: {ficha["cidade"][index_cpf_cadastro]}\n Estado: {ficha["estado"][index_cpf_cadastro]}')
                        case "não"|"nao"|"n":
                            print('Volte quando precisar!')
                        case _:
                            print('Opção inválida!')
                case "2"|"idade":
                    nova_idade = int(input('Digite a nova idade do usuário: '))
                    ficha["idade"][index_cpf_cadastro] = nova_idade
                    verificacao_alteracao_idade = input('Idade trocada com sucesso!\nGostaria de verificar como ficou a alteração? S/N: ')
                    match verificacao_alteracao_idade:
                        case "sim"|"s":
                            print(f'Após a alteração os dados ficaram:\n Nome: {ficha["nome"][index_cpf_cadastro]}\n CPF: {ficha["cpf"][index_cpf_cadastro]}\n Idade: {ficha["idade"][index_cpf_cadastro]}\n Cidade: {ficha["cidade"][index_cpf_cadastro]}\n Estado: {ficha["estado"][index_cpf_cadastro]}')
                        case "não"|"nao"|"n":
                            print('Volte quando precisar!')
                        case _:
                            print('Opção inválida!')
                case "3"|"cidade":
                    nova_cidade = input('Digite o nome da nova cidade do usuário: ').title().strip()
                    ficha["cidade"][index_cpf_cadastro] = nova_cidade
                    verificacao_alteracao_cidade = input('Cidade trocada com sucesso!\nGostaria de verificar como ficou a alteração? S/N: ')
                    match verificacao_alteracao_cidade:
                        case "sim"|"s":
                            print(f'Após a alteração os dados ficaram:\n Nome: {ficha["nome"][index_cpf_cadastro]}\n CPF: {ficha["cpf"][index_cpf_cadastro]}\n Idade: {ficha["idade"][index_cpf_cadastro]}\n Cidade: {ficha["cidade"][index_cpf_cadastro]}\n Estado: {ficha["estado"][index_cpf_cadastro]}')
                        case "não"|"nao"|"n":
                            print('Volte quando precisar!')
                        case _:
                            print('Opção inválida!')
                case "4"|"estado":
                    novo_estado = input('Digite os siglas do novo estado do usuário: ').upper().strip()
                    verificar_estado = len(novo_estado)
                    if verificar_estado != 2:
                        print('Sigla inválida! Sua sigla deve possuir dois caracteres, exemplo: PA, SC, PR.')
                    else:
                        ficha["estado"][index_cpf_cadastro] = novo_estado
                        verificacao_alteracao_estado = input('Estado trocado com sucesso!\nGostaria de verificar como ficou a alteração? S/N: ')
                        match verificacao_alteracao_estado:
                            case "sim"|"s":
                                print(f'Após a alteração os dados ficaram:\n Nome: {ficha["nome"][index_cpf_cadastro]}\n CPF: {ficha["cpf"][index_cpf_cadastro]}\n Idade: {ficha["idade"][index_cpf_cadastro]}\n Cidade: {ficha["cidade"][index_cpf_cadastro]}\n Estado: {ficha["estado"][index_cpf_cadastro]}')
                            case "não"|"nao"|"n":
                                print('Volte quando precisar!')
                            case _:
                                print('Opção inválida!')
                case _:
                    print('Opção inválida!')
    case "4"|"deletar cadastro":
        escolha_alteracao_deletar = input('O que você gostaria de deletar?\n [1] Todos os cadastros\n [2] Cadastro específico\n Opção escolhida:')    
        match escolha_alteracao_deletar:
            case "1"|"todos os cadastros":
                ficha["nome"].clear()
                ficha["cpf"].clear()
                ficha["idade"].clear()
                ficha["cidade"].clear()
                ficha["estado"].clear()
                verificar_cadastros_deletados = input('Deseja vericar como ficou a ficha? S/N: ')
                match verificar_cadastros_deletados:
                    case "sim"|"s":
                        print(f'Sua lista ficou assim {ficha}')
                    case "não"|"nao"|"n":
                        print('Volte quando precisar!')
                    case _:
                        print('Opção inválida!')
            case "2"|"cadastro específico":
                cpf_cadastro_especifico_deletar = input('Digite o CPF do usuário procurado: ').strip()
                if cpf_cadastro_especifico_deletar in ficha["cpf"]:
                    cadastro_expecifico_deletar = ficha["cpf"].index(cpf_cadastro_especifico_deletar)
                    del ficha["nome"][cadastro_expecifico_deletar]
                    del ficha["idade"][cadastro_expecifico_deletar]
                    del ficha["cidade"][cadastro_expecifico_deletar]
                    del ficha["estado"][cadastro_expecifico_deletar]
                    del ficha["cpf"][cadastro_expecifico_deletar]
                    print('Cadastro deletado com sucesso!')
                    verificar_cadastros_especificos_deletados = input('Deseja verificar como ficou sua ficha? S/N: ')
                    match verificar_cadastros_especificos_deletados:
                        case "sim"|"s":
                            print(f'Sua ficha ficou da seguinte forma: {ficha}')
                        case "não"|"nao"|"n":
                            print('Volte quando precisar!')
                        case _:
                            print('Opção inválida!')
                else:
                    print('Usuário não cadastrado!')
            case _:
                print('Opção inválida')
    case _:
        print('Opção inválida')
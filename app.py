def auth_votar(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print(f'Ola, você tem {idade} anos')
  
    if idade < 16:
        print('Menor de idade, seu direito ao voto: Negado')
        auth_voto = False
    elif idade >= 16 and idade < 18:
        print('Menor de idade, seu direito ao voto: Opcional')
        auth_voto = True
    elif idade >= 18 and idade < 70:
        print('Maior de idade, seu direito ao voto: Obrigatório')
        auth_voto = True
    else:
        print('Maior de idade, seu direito ao voto: Opcional')
        auth_voto = True
    return auth_voto


def total_votos():
    #resultado_dict = {k: v for k, v in zip(candidatos, total_de_votos)}
    #print(f'{resultado_dict}')
    
    for indice_candidato, votos_candidato in zip(candidatos, total_de_votos):
        tabela_votacao[indice_candidato] = votos_candidato
        #print(f'Candidato {indice_candidato}: {votos_candidato} votos')

    # print(tabela_votacao)
    totalvotos = sum(total_de_votos) 
    vencedor = max(total_de_votos)      
    
    for i in range(len(total_de_votos)):
        perc = total_de_votos[i]/totalvotos * 100    
        print(f'\nCandidato: {candidatos[i]}\nVotos: {total_de_votos[i]}\nPercentual:{perc:.2f}%')
        
        if vencedor == total_de_votos[i]:
            venceu = i
    
    if candidatos[venceu] == candidatos[3] or candidatos[venceu] == candidatos[4]:
        print('\nVotos nulos e brancos teve uma grande parcela nos votos, terá que ser feito uma nova eleição')
    else:
        print(f'\n\nO candidato {candidatos[venceu]} foi ELEITO')
    
# Init
auth_voto = True
nascimento = int(input('Em que ano você nasceu?: '))
auth_votar(nascimento)


# contabilidade
total_de_votos = [0,0,0,0,0]
candidatos =['Lula', 'Bolsonaro', 'Danilo', 'Voto Nulo', 'Voto em Branco']
tabela_votacao = {}

while auth_voto:
    
    # Listar candidatos 
    for x, item in enumerate(candidatos):
        print(f'Candidato {x + 1}: {item}')

    # input do voto
    user_votou = int(input('Digite o número do Candidato:  '))
    print('\n')
    
    if user_votou == 1:
        print(f'Seu voto foi para o candidato {candidatos[0]}')
        total_de_votos[0] += 1

    elif user_votou == 2:
        print(f'Seu voto foi para o candidato {candidatos[1]}')
        total_de_votos[1] += 1

    elif user_votou == 3:
        print(f'Seu voto foi para o candidato {candidatos[2]}')
        total_de_votos[2] += 1

    elif user_votou == 4:
        print(f'Seu voto foi para o candidato {candidatos[3]}')
        total_de_votos[3] += 1
        
    elif user_votou == 5:
        print(f'Seu voto foi para o candidato {candidatos[4]}')
        total_de_votos[4] += 1
    
    else:
        print('A votacao foi finalizada, fechando sistema!')
        print('Loading...')
        print('Contagem de votos sendo inicalizada ...')
        print('...')
        print('Contagem efeituada, segue resutados: ')
        total_votos()
        auth_voto = False



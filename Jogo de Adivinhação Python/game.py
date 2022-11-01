from random import randint
#Espaço amostral que o computador pode gerar os números: 
computador= randint(0, 5)
print('Acabei de pensar em número, entre 0 e 5... ')
print('Será que você consegue pensar qual foi o valor?.. ')
acertou=False
palpites=0
#Enquanto ainda não acertar 
while not acertou:
    jogador=int(input('Qual número?'))
    #Contagem dos palpites do jogador
    palpites+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print(' Ta friooooo...Tente mais uma vez....')
        elif jogador>computador:
            print('Ta quente...Preste mais atenção')
print('Acertou com {} tentativas. Meus Parabéns'.format(palpites))

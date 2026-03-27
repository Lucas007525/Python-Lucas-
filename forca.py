def jogar_forca():
    print('*--------------------*')
    print('BEM VINDO AO JOGO DE FORCA')
    print('*--------------------*')
    palavra_secreta = "carambóla"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    perdeu = False
    acertou = False

    while(not perdeu and not acertou):
        chute = input('Digite uma Letra: ')
        chute = chute.strip()

        #Index define a posição da letra
        index = 0

        for letra in palavra_secreta:
            if(chute.lower() == letra.lower()):
                print(f'A letra {chute} está na posição {index}!')
                letras_acertadas[index] = letra 
            index = index+1
            







if(__name__ == "__main__"):
    jogar_forca()
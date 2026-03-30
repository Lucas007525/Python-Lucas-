def jogar_forca():
    print('*--------------------*')
    print('BEM VINDO AO JOGO DE FORCA')
    print('*--------------------*')

    arquivo = open("PYTHON-LUCAS-MAIN/palavras.txt", "r")
    palavra = []

    for linha in palavra:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close

    palavra_secreta = "opa"
    letras_acertadas = []

    for letras in palavra_secreta:
        letras_acertadas.append("_")

    perdeu = False
    acertou = False
    erros = 0 
    while(not perdeu and not acertou):
        chute = input('Digite uma Letra:')
        chute = chute.strip()

        #Index define a posição da letra
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    print(f'A letra {chute} está na posição {index}!')
                    letras_acertadas[index] = letra 
                    index = index + 1 
        else:
            erros = erros + 1
            acertou = "_" not in letras_acertadas


           
            perdeu = erros == 6 
        print(letras_acertadas)
        

if(__name__ == "__main__"):
    jogar_forca()
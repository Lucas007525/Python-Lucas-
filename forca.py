def jogar_forca():
    print("--------------")
    print("Bem vindo ao jogo da forca")
    print("-----------")

    palavra_secreta = "processador"
    perdeu = False 
    acertou = False

    # Enquanto não acertar a palavra secreta.
    # O jogador pode jogar.

    while(not perdeu and not acertou):
        chute = input ("Escreva uma letra:")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
           if(chute.lower == letra.lower):
                print(letra)
            # index define a posição da letra.
        index = index + 1 
import unicodedata

           
if(__name__ == "__main__"):
    jogar_forca()

# tarefa como resolver o acento. 
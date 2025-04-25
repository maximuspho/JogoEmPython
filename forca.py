# projeto 1 - Desenvolvimento de Game em Python - Versão 1
# import
import random
from os import system, name

# função para limpar a tela a cada execução


def limpa_tela():
    # windowns
    if name == 'nt':
        _ = system('cls')
    # mac ou linux
    else:
        _ = system('clear')

# função


def game():

    limpa_tela()
    print('\nBem-Vindo ao Jogo da Forca! \nAdivinhe a Palavra abaixo\n')

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # list comprehension
    letras_descobertas = ['_' for letra in palavra]

    # numero de chances
    chances = 6
    # lista para as letras erradas
    letras_erradas = []

    # loop enquanto numero de chances dor maios do que zero
    while chances > 0:

        # print
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas: ", " ".join(letras_erradas))

        # tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # condicional
        if '_' not in letras_descobertas:
            print('\nVocê venceu, a palavra era: ', palavra)
            break

    # condicional
    if '_' in letras_descobertas:
        print('\nVocê perdeu, a palavra era: ', palavra)


# bloco main
if __name__ == '__main__':
    game()
    print('\nParabens. Voce esta aprendendo a programação em Python')

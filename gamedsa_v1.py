#v1 do game
import random
from os import system

# Função para limpar a tela
def tela_limpa():
    _ = system('clear')  # Usado 'clear' no macOS para limpar a tela

# Função do jogo
def game():

    tela_limpa()
    print('\nBem-vindo ao jogo da forca!')
    print('Adivinhe a palavra abaixo e ganhe!\n')

    # Lista de palavras para o jogo
    palavras = ['Gato', 'Pipoca', 'Feijão', 'Banana']

    # Escolher a palavra de forma randômica
    palavra = random.choice(palavras)

    # List comprehension para inicializar as letras descobertas como '_'
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 7

    # Lista para armazenar as letras erradas
    letras_erradas = []

    # Loop enquanto o número de chances for maior que 0
    while chances > 0:
        print(' '.join(letras_descobertas))
        print('\nChances restantes:', chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Entrada do usuário (tentativa)
        tentativa = input('Coloque uma letra: ').lower()  # Deixa a letra em minúsculo

        # Condicional para verificar se a tentativa está na palavra
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra  # Atualiza a letra descoberta
                index += 1  # Avança para o próximo índice

        else:
            chances -= 1  # Reduz uma chance se a letra não estiver na palavra
            letras_erradas.append(tentativa)  # Adiciona a tentativa incorreta à lista

        # Verifica se o jogador venceu (não há mais '_')
        if '_' not in letras_descobertas:
            print('\nVocê venceu! a palavra era:', palavra)
            break  # Sai do loop de jogo

    if chances == 0:  # Se o número de chances chegar a zero, o jogador perdeu
        print('\nVocê perdeu, a palavra era: ', palavra)

# Chama a função do jogo
if __name__ == '__main__':
    game()


import random
import os
from os import name, system

def clear_screen():
    
    if name == 'nt':
        _ = system('cls')

def game():
    clear_screen()
    
    try:
        with open("C:\\PythonDSA\\Learn-Python\\Lab\\projeto1\\palavras.txt", "r") as arquivo:
            conteudo = arquivo.read()

        texto_sem_espaco = conteudo.replace(" ", "")
        tamanho_da_palavra = texto_sem_espaco.split(",")
        
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        
    chances = 10
    wrong_letters = []
    
    choice_word = random.randint(0, len(tamanho_da_palavra))    
    
    size_word = ['_' for i in tamanho_da_palavra[choice_word]]
    word = tamanho_da_palavra[choice_word] 
    print(size_word)
                 
    while chances > 0:
        if '_' not in size_word:
            break
        else:
            print(f"\nTentativas restantes: {chances}")
            print(f"Letras erradas:", " ".join(wrong_letters))
            print(size_word)
            letra = input("Digite uma letra: ").lower()
            
            if letra in word:
                for i, caractere in enumerate(word):
                    if caractere == letra:
                        size_word[i] = letra
            else:
                wrong_letters.append(letra)
                
            chances -= 1
            
    if chances == 0:
        print("\nVocê perdeu!!")
        print(word.upper())
    else:
        print("\nYou're the man!!")
        print(word.upper())

if __name__ == "__main__":
    game()
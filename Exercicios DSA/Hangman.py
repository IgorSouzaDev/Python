

'''class Calculadora:

    def __init__(self,value,value2) :
        
        self.a = value
        self.b = value2
        print("Criado")

    def soma (self):
        soma= self.a + self.b
        return "soma: " + str(soma)

    def subtracao (self):
        sub = self.a - self.b
        return "subtração : " + str(sub)

    def multiplicacao (self):
        sub = self.a * self.b
        return "subtração :  " + str(sub)


conta = int(input("Se deseja Somar digite 1 \n Subtração 2\n Multiplicação 3: "))

soma = 1 
subtracao=2
multiplicacao = 3

teste = Calculadora(int(input("valor 1: ")),int(input("valor 2: ")))'''

'''if conta == soma:
    calculo = teste.soma()
    print("soma é igua há: ",calculo)

elif conta == subtracao:
        calculo =teste.subtracao()
        print("subtração é igua há: ",calculo)

elif conta == multiplicacao:
        calculo =teste.multiplicacao()
        print("multiplição é igua há: ",calculo)
'''










# Import
import random

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    def __init__(self, letra):
        self.letra = letra
        self.missed = missed = []
        self.guessed = guessed = []
	# Método para adivinhar a letra
    def guess(self, letra):
        if letra in self.letra and letra not in self.guessed:
            self.guessed.append(letra)
        elif letra not in self.letra and letra not in self.missed:
            self.missed.append(letra)
        else:
            return False
        return True
	# Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed)==6)

	# Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False
	# Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for letra in self.letra:
            if letra not in self.guessed:
                rtn += '_'
            else:
                rtn += letra
        return rtn
	# Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print (board[len(self.missed)])
        print ('\nPalavra: ' + self.hide_word())
        print ('\nLetras Erradas:', )
        for letra in self.missed:
            print(letra,)
        print()
        print("Letras Corretas:")
        for letra in self.guessed:
            print(letra,)
        print()
# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("C:\\Users\\Igor\\Documents\\Dataframe\\Python\\Exercicios DSA\\palavras.txt", "r") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()



# Função Main - Execução do Programa
def main():
    game = Hangman(rand_word())
#Enquanto o jogo não terminar print do status,solicita uma nova letra do caracter  
    while not game.hangman_over():
         game.print_game_status()
         user_input = input('\n Digite uma Letra: ')
         game.guess(user_input)

# Verifica o status do jogo
    game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print ('\nParabéns! Você venceu!!')
    else:
        print ('\nGame over! Você perdeu.')
        print ('A palavra era ' + game.word)
        
    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
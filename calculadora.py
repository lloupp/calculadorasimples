# Programa Python para criar uma GUI simples
# calculadora usando Tkinter

# importando o modulo tkinder
from tkinter import *

# Variavel global para armazenar o resultado do cálculo
expression = ""


# Funcção para atualizar a expressão
# entrada de texto
def press(num):
	#aponta a variável de expressão global
	global expression

	# concatenação de string
	expression = expression + str(num)

	# atualiza a expressão usando o método set
	equation.set(expression)


#Função para avaliar a expressão final
def equalpress():
	# A instrução try e except é usada
	# para lidar com os erros como zero
	# erro de divisão etc.

	try:

		global expression

		# função eval avalia a expressão
		# e função str convertem o resultado na string
		total = str(eval(expression))

		equation.set(total)

		#inicializa a variavel de expressão
		#vazia
		expression = ""


	except:

		equation.set(" error ")
		expression = ""


# Função para limpar o conteúdo da caixa de entrada de texto
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# cria uma janela GUI
	gui = Tk()

	# define a cor de fundo da janela GUI
	gui.configure(background="light blue")

	# Define o titulo da janela
	gui.title("Calculadora Simples")

	# Define o tamanho
	gui.geometry("350x200")

	# StringVar() é a classe variavel
	# criamos uma instancia desta classe
	equation = StringVar()

	# cria a caixa de texto
	# showing the expression .
	expression_field = Entry(gui, textvariable=equation)

	# a grade é usada para colocar os widges nas respectivas posições
	expression_field.grid(columnspan=4, ipadx=90)

	# Cria botoes e coloca em um determinadao local na janela
	# quando o usuário pressiona o botão
	# a função associada a esse botão e executada
	button1 = Button(gui, text=' 1 ', fg='black', bg='gray',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='gray',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='gray',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='gray',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='gray',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='gray',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='gray',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='gray',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='gray',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='gray',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	soma = Button(gui, text=' + ', fg='black', bg='gray',
				command=lambda: press("+"), height=1, width=7)
	soma.grid(row=2, column=3)

	subtracao = Button(gui, text=' - ', fg='black', bg='gray',
				command=lambda: press("-"), height=1, width=7)
	subtracao.grid(row=3, column=3)

	multiplicacao = Button(gui, text=' * ', fg='black', bg='gray',
					command=lambda: press("*"), height=1, width=7)
	multiplicacao.grid(row=4, column=3)

	divisao = Button(gui, text=' / ', fg='black', bg='gray',
					command=lambda: press("/"), height=1, width=7)
	divisao.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='Blue',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Limpar', fg='black', bg='gray',
				command=clear, height=1, width=7)
	clear.grid(row=5, column=1)

	Decimal= Button(gui, text='.', fg='black', bg='gray',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	# start the GUI
	gui.mainloop()

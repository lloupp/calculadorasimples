# Calculadora Simples em Python com interface gráfica usando Tkinter

from tkinter import *

# Paleta de cores
COR_FUNDO        = "#1e1e2e"
COR_DISPLAY      = "#2a2a3d"
COR_TEXTO        = "#cdd6f4"
COR_NUMERO       = "#313244"
COR_NUMERO_HOVER = "#45475a"
COR_OPERADOR     = "#f38ba8"
COR_IGUAL        = "#a6e3a1"
COR_LIMPAR       = "#fab387"
COR_DECIMAL      = "#89b4fa"

FONTE_DISPLAY = ("Segoe UI", 22, "bold")
FONTE_BOTAO   = ("Segoe UI", 14, "bold")

# Variável global para armazenar a expressão atual
expression = ""


def press(valor):
    """Acrescenta um valor à expressão atual e atualiza o display."""
    global expression
    expression += str(valor)
    equation.set(expression)


def equalpress():
    """Avalia a expressão atual e exibe o resultado."""
    global expression
    try:
        resultado = str(eval(expression))
        equation.set(resultado)
        expression = ""
    except (SyntaxError, NameError, ZeroDivisionError, TypeError, ValueError):
        equation.set("Erro")
        expression = ""


def clear():
    """Limpa a expressão e o display."""
    global expression
    expression = ""
    equation.set("")


def criar_botao(parent, texto, comando, cor_fundo, col, row, colspan=1):
    """Cria e posiciona um botão estilizado na grade."""
    btn = Button(
        parent,
        text=texto,
        font=FONTE_BOTAO,
        fg=COR_TEXTO,
        bg=cor_fundo,
        activebackground=COR_NUMERO_HOVER,
        activeforeground=COR_TEXTO,
        bd=0,
        relief=FLAT,
        cursor="hand2",
        command=comando,
        height=2,
        width=6,
    )
    btn.grid(row=row, column=col, columnspan=colspan, padx=4, pady=4, sticky="nsew")
    return btn


if __name__ == "__main__":
    gui = Tk()
    gui.title("Calculadora Simples")
    gui.configure(background=COR_FUNDO)
    gui.geometry("360x460")
    gui.resizable(False, False)

    # Configura as colunas para expandir uniformemente
    for i in range(4):
        gui.columnconfigure(i, weight=1)

    # ── Display ──────────────────────────────────────────────────────────────
    equation = StringVar()

    display_frame = Frame(gui, bg=COR_DISPLAY, bd=0)
    display_frame.grid(row=0, column=0, columnspan=4, padx=12, pady=(16, 8), sticky="ew")

    expression_field = Entry(
        display_frame,
        textvariable=equation,
        font=FONTE_DISPLAY,
        fg=COR_TEXTO,
        bg=COR_DISPLAY,
        bd=0,
        justify=RIGHT,
        insertbackground=COR_TEXTO,
        readonlybackground=COR_DISPLAY,
    )
    expression_field.pack(fill=X, ipady=14, padx=12)

    # ── Botões numéricos e operadores ─────────────────────────────────────────
    criar_botao(gui, "7", lambda: press(7), COR_NUMERO, 0, 2)
    criar_botao(gui, "8", lambda: press(8), COR_NUMERO, 1, 2)
    criar_botao(gui, "9", lambda: press(9), COR_NUMERO, 2, 2)

    criar_botao(gui, "4", lambda: press(4), COR_NUMERO, 0, 3)
    criar_botao(gui, "5", lambda: press(5), COR_NUMERO, 1, 3)
    criar_botao(gui, "6", lambda: press(6), COR_NUMERO, 2, 3)

    criar_botao(gui, "1", lambda: press(1), COR_NUMERO, 0, 4)
    criar_botao(gui, "2", lambda: press(2), COR_NUMERO, 1, 4)
    criar_botao(gui, "3", lambda: press(3), COR_NUMERO, 2, 4)

    criar_botao(gui, "0", lambda: press(0), COR_NUMERO, 0, 5)
    criar_botao(gui, ".", lambda: press("."), COR_DECIMAL, 1, 5)
    criar_botao(gui, "=", equalpress, COR_IGUAL, 2, 5)

    # ── Coluna de operadores ──────────────────────────────────────────────────
    criar_botao(gui, "+", lambda: press("+"), COR_OPERADOR, 3, 2)
    criar_botao(gui, "-", lambda: press("-"), COR_OPERADOR, 3, 3)
    criar_botao(gui, "*", lambda: press("*"), COR_OPERADOR, 3, 4)
    criar_botao(gui, "/", lambda: press("/"), COR_OPERADOR, 3, 5)

    # ── Botão Limpar (linha superior) ─────────────────────────────────────────
    criar_botao(gui, "Limpar", clear, COR_LIMPAR, 0, 1, colspan=4)

    gui.mainloop()

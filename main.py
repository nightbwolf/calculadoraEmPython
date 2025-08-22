import tkinter as tk
from tkinter import messagebox

# Funções da calculadora
def soma(a, b):
    return a + b

def subt(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        messagebox.showerror("Erro", "Divisão por zero não é permitida.")
        return None
    return a / b

# A função de média agora usa apenas dois números
def media(a, b):
    return (a + b) / 2

# Função principal para o botão de cálculo
def calcular(operacao):
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())

        if operacao == 'soma':
            resultado = soma(num1, num2)
        elif operacao == 'subtracao':
            resultado = subt(num1, num2)
        elif operacao == 'multiplicacao':
            resultado = mult(num1, num2)
        elif operacao == 'divisao':
            resultado = div(num1, num2)
        elif operacao == 'media':
            resultado = media(num1, num2)
        
        if resultado is not None:
            label_resultado.config(text=f"O resultado é: {resultado}")
            
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Bola ")
janela.geometry("300x250")
janela.config(bg="#9f53b3")

# Widgets da interface
frame_principal = tk.Frame(janela, padx=20, pady=20, bg="#3d2b8f")
frame_principal.pack(expand=True)

# Labels e Entradas
tk.Label(frame_principal, text="Número 1:", bg="#56a8b3").grid(row=0, column=0, pady=5, sticky='e')
entrada_num1 = tk.Entry(frame_principal)
entrada_num1.grid(row=0, column=1, pady=5)

tk.Label(frame_principal, text="Número 2:", bg="#56a8b3").grid(row=1, column=0, pady=5, sticky='e')
entrada_num2 = tk.Entry(frame_principal)
entrada_num2.grid(row=1, column=1, pady=5)

# Botões
frame_botoes = tk.Frame(frame_principal, bg="#3d2b8f")
frame_botoes.grid(row=2, columnspan=2, pady=10)

tk.Button(frame_botoes, text="+", width=4, command=lambda: calcular('soma')).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="-", width=4, command=lambda: calcular('subtracao')).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="*", width=4, command=lambda: calcular('multiplicacao')).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="/", width=4, command=lambda: calcular('divisao')).grid(row=0, column=3, padx=5)
tk.Button(frame_botoes, text="Média", width=6, command=lambda: calcular('media')).grid(row=0, column=4, padx=5)

# Resultado
label_resultado = tk.Label(frame_principal, text="Resultado:", font=("Arial", 12), bg="#f0f0f0")
label_resultado.grid(row=3, columnspan=2, pady=10)

# Iniciar
janela.mainloop()
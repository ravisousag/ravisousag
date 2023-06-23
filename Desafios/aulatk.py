import tkinter as tk

def clique_do_botao():
    print("O botão foi clicado!")
    botao = tk.Button(janela, text="Clique aqui!", command=clique_do_botao)
    botao.pack()

def exibir_texto():
    conteudo = caixa_entrada.get()
    rotulo.config(text=conteudo)
    caixa_entrada = tk.Entry(janela)
    caixa_entrada.pack()
    botao = tk.Button(janela, text="Exibir texto", command=exibir_texto)
    botao.pack()
 
 # Criação da janela
janela = tk.Tk()

# Configurando o título da janela
janela.title("Minha Janela")

# Configurando as dimensões da janela
janela.geometry("400x300")

# Executando o loop principal da janela
janela.mainloop()

# Criação de um rótulo (Label)
rotulo = tk.Label(janela, text="Olá, mundo!")
rotulo.pack()

# Criação de um botão (Button)
botao = tk.Button(janela, text="Clique aqui!")
botao.pack()







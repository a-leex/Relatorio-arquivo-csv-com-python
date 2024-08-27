import pandas as pd
from tkinter import Tk, Label, Button, Listbox, Scrollbar, END, StringVar, Entry, messagebox

#Autor do projeto Alex Souza

# Carregar o arquivo CSV
file_path = 'br_ibge_censo_2022_populacao_grupo_idade_uf.csv'
df = pd.read_csv(file_path)

# As funções do app
def ordenar_populacao(ordem):
    df_ordenado = df.sort_values(by='populacao', ascending=ordem)
    atualizar_lista(df_ordenado)

def relatorio_estado():
    estado = estado_entry.get().upper()
    resultado = df[df['sigla_uf'] == estado]
    if resultado.empty:
        messagebox.showerror("Erro", f"Nenhum dado encontrado para o estado {estado}.")
    else:
        atualizar_lista(resultado)

def atualizar_lista(dataframe):
    lista.delete(0, END)
    for idx, row in dataframe.iterrows():
        lista.insert(END, f"{row['sigla_uf']} - {row['grupo_idade']}: {row['populacao']}")

# Interface gráfica configuração
root = Tk()
root.title("IBGE - Censo 2022")

Label(root, text="IBGE - Instituto Brasileiro de Geografia e Estatistica", font=("Arial", 14)).pack(pady=10)

Button(root, text="Ordenar do maior para o menor", command=lambda: ordenar_populacao(False)).pack(pady=5)
Button(root, text="Ordenar do menor para o maior", command=lambda: ordenar_populacao(True)).pack(pady=5)

Label(root, text="Consultar estado (sigla):").pack(pady=5)
estado_entry = Entry(root)
estado_entry.pack(pady=5)

Button(root, text="Consultar", command=relatorio_estado).pack(pady=5)

lista = Listbox(root, width=50, height=15)
lista.pack(pady=10)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

lista.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista.yview)

Button(root, text="Sair", command=root.quit).pack(pady=10)

root.mainloop()

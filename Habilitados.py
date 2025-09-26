import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Abrir janela para selecionar múltiplos arquivos
root = tk.Tk()
root.withdraw()  # não mostrar a janela principal
caminhos = filedialog.askopenfilenames(
    title="Selecione os arquivos CSV exportados do Google Forms",
    filetypes=[("Arquivos CSV", "*.csv")]
)

# Função para normalizar os nomes
def normalizar(coluna):
    return coluna.str.strip().str.lower()

arquivos = []
for caminho in caminhos:
    df = pd.read_csv(caminho)
    # Garante que a coluna "Nome Completo" existe
    if "Nome Completo" in df.columns:
        df["Nome Completo"] = normalizar(df["Nome Completo"])
        arquivos.append(df)
    else:
        print(f"Aviso: '{caminho}' não possui a coluna 'Nome Completo'.")

# Concatenar todos os nomes em um único DataFrame
todos_nomes = pd.concat([f["Nome Completo"] for f in arquivos])

# Contar quantas vezes cada nome apareceu
contagem = todos_nomes.value_counts().reset_index()
contagem.columns = ["Alunos", "Quantidade"]

# Criar IDs
contagem.insert(0, "ID", range(1, len(contagem) + 1))

# Salvar em Excel
contagem.to_excel("habilitados_contagem.xlsx", index=False)

print("✅ Planilha 'habilitados_contagem.xlsx' criada com sucesso!")

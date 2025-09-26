import pandas as pd

# Carregar os arquivos exportados do Google Forms (CSV)
form1 = pd.read_csv("IREDE.csv")
form2 = pd.read_csv("IDESCO.csv")
form3 = pd.read_csv("IEPRO.csv")
form4 = pd.read_csv("Instituto Iracema.csv")
form5 = pd.read_csv("NEPEN.csv")
form6 = pd.read_csv("Apresentação.csv")
form7 = pd.read_csv("pichts ICTS.csv")

# Função para normalizar os nomes
def normalizar(coluna):
    return coluna.str.strip().str.lower()

# Normalizar os nomes em todos os arquivos
arquivos = [form1, form2, form3, form4, form5, form6, form7]
for f in arquivos:
    f["Nome Completo"] = normalizar(f["Nome Completo"])

# Concatenar todos os nomes em um único DataFrame
todos_nomes = pd.concat([f["Nome Completo"] for f in arquivos])

# Contar quantas vezes cada nome apareceu
contagem = todos_nomes.value_counts().reset_index()
contagem.columns = ["Alunos", "Quantidade"]

# Criar IDs
contagem.insert(0, "ID", range(1, len(contagem) + 1))

# Salvar em Excel
contagem.to_excel("habilitados_contagem.xlsx", index=False)

print("Planilha 'habilitados_contagem.xlsx' criada com sucesso!")

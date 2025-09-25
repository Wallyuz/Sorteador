import pandas as pd

# Carregar os arquivos exportados do Google Forms (CSV)
form1 = pd.read_csv("IREDE.csv")
form2 = pd.read_csv("IDESCO.csv")
form3 = pd.read_csv("IEPRO.csv")
form4 = pd.read_csv("Instituto Iracema.csv")
form5 = pd.read_csv("NEPEN.csv")
form6 = pd.read_csv("Apresentação.csv")
form7 = pd.read_csv("pichts ICTS.csv")

# Normalizar os nomes (remover espaços extras e deixar minúsculo)
def normalizar(coluna):
    return coluna.str.strip().str.lower()

form1["Nome Completo"] = normalizar(form1["Nome Completo"])
form2["Nome Completo"] = normalizar(form2["Nome Completo"])
form3["Nome Completo"] = normalizar(form3["Nome Completo"])
form4["Nome Completo"] = normalizar(form4["Nome Completo"])
form5["Nome Completo"] = normalizar(form5["Nome Completo"])
form6["Nome Completo"] = normalizar(form6["Nome Completo"])
form7["Nome Completo"] = normalizar(form7["Nome Completo"])

# Interseção de todos os conjuntos
habilitados = set(form1["Nome Completo"]) & set(form2["Nome Completo"]) & set(form3["Nome Completo"]) & set(form4["Nome Completo"]) & set(form5["Nome Completo"]) & set(form6["Nome Completo"]) & set(form7["Nome Completo"])

# Converter para lista sem ordenação
habilitados_lista = list(habilitados)

# Criar DataFrame com ID
df_habilitados = pd.DataFrame({
    "ID": range(1, len(habilitados_lista) + 1),
    "Alunos Habilitados": habilitados_lista
})

# Salvar em uma nova planilha 
df_habilitados.to_excel("habilitados.xlsx", index=False)

print("Planilha 'habilitados.xlsx' criada com sucesso com IDs!")

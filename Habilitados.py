import pandas as pd

# Carregar os arquivos exportados do Google Forms (CSV)
form1 = pd.read_csv("form1.csv")
form2 = pd.read_csv("form2.csv")
form3 = pd.read_csv("form3.csv")
form4 = pd.read_csv("form4.csv")

# Normalizar os nomes (remover espaços extras e deixar minúsculo)
def normalizar(coluna):
    return coluna.str.strip().str.lower()

form1["Nome"] = normalizar(form1["Nome"])
form2["Nome"] = normalizar(form2["Nome"])
form3["Nome"] = normalizar(form3["Nome"])
form4["Nome"] = normalizar(form4["Nome"])

# Interseção de todos os conjuntos
habilitados = set(form1["Nome"]) & set(form2["Nome"]) & set(form3["Nome"]) & set(form4["Nome"])

# Converter para lista e ordenar alfabeticamente (opcional)
habilitados_ordenados = sorted(list(habilitados))

# Criar DataFrame com ID
df_habilitados = pd.DataFrame({
    "ID": range(1, len(habilitados_ordenados) + 1),
    "Alunos Habilitados": habilitados_ordenados
})

# Salvar em uma nova planilha 
df_habilitados.to_excel("habilitados.xlsx", index=False)

print("Planilha 'habilitados.xlsx' criada com sucesso com IDs!")

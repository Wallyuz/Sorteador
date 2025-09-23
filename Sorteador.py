import pandas as pd
import random

# ---- Configuração: número de vencedores ----
quantidade_vencedores = 3  # Altere para quantos vencedores quiser

# ---- Ler a planilha de habilitados -----
habilitados_df = pd.read_excel("habilitados.xlsx")
participantes = habilitados_df["Alunos Habilitados"].tolist()

# ---- Sorteio ----
if len(participantes) >= quantidade_vencedores:
    vencedores = random.sample(participantes, quantidade_vencedores)
elif participantes:
    print("⚠️ Menos participantes do que vencedores solicitados. Sorteando todos disponíveis.")
    vencedores = participantes
else:
    print("⚠️ Nenhum participante habilitado.")
    vencedores = []

# ---- Salvar os vencedores em uma nova planilha ---- -
if vencedores:
    pd.DataFrame({"Vencedores": vencedores}).to_excel("vencedores.xlsx", index=False)
    print(f"Planilha 'vencedores.xlsx' criada com sucesso! Vencedores: {', '.join(vencedores)}")

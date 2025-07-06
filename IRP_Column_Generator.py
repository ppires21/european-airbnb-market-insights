import pandas as pd

# Diretoria do CSV original e de saída
input_csv_path = '/Users/pires/Desktop/Mestrado/AVI/Momento3/IRP_airbnb_dataset_merged.csv'
output_csv_path = '/Users/pires/Desktop/Mestrado/AVI/Momento3/IRP_airbnb_dataset_merged_updated.csv'

# Carregar o dataset
df = pd.read_csv(input_csv_path)

# Garantir que as colunas necessárias existem e preencher valores nulos, se necessário
df['realSum'] = df['realSum'].fillna(0)
df['guest_satisfaction_overall'] = df['guest_satisfaction_overall'].fillna(0)
df['dist'] = df['dist'].fillna(0)
df['metro_dist'] = df['metro_dist'].fillna(0)
df['host_is_superhost'] = df['host_is_superhost'].fillna("False").astype(str)
df['Period'] = df['Period'].fillna("weekday")
df['person_capacity'] = df['person_capacity'].fillna(1)

# Criar a nova coluna IRP
def calculate_irp(row):
    preco_medio_noite = row['realSum'] / 2
    base_ocupacao = 0.3  # Base inicial de 30%
    avaliacoes = 0.1 if row['guest_satisfaction_overall'] > 80 else 0
    proximidade = 0.1 if row['dist'] < 3 or row['metro_dist'] < 3 else 0
    superhost = 0.1 if row['host_is_superhost'] == "True" else 0
    fim_de_semana = 0.1 if row['Period'] == "weekend" else 0
    taxa_ocupacao = min(base_ocupacao + avaliacoes + proximidade + superhost + fim_de_semana, 0.3)  # Máximo de 30%
    receita_anual = preco_medio_noite * taxa_ocupacao * 365 * row['person_capacity']
    return receita_anual

# Aplicar a função para calcular o IRP
df['IRP'] = df.apply(calculate_irp, axis=1)

# Salvar o dataset atualizado para um novo ficheiro CSV
df.to_csv(output_csv_path, index=False)

print(f"Novo ficheiro com IRP salvo em: {output_csv_path}")

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('IXRDProsame.csv')

# Conversão das datas
for col in ['Admissao', 'Qualificacao', 'Habilitacao', 'Execucao']:
    dados[col] = pd.to_datetime(
        dados[col],
        dayfirst=True,
        errors='coerce'
    )

# Primeira data existente do banco
inicio = dados['Admissao'].min()

# Última data existente considerando todas as etapas
fim = pd.concat([
    dados['Admissao'],
    dados['Qualificacao'],
    dados['Habilitacao'],
    dados['Execucao']
]).max()

# Deve-se editar os períodos para mostrar as reuniões deliberativas em vez de tempo corrido.
# Além disso, após a criação da imagem é de interesse ressaltar as datas de movimentações das propostas mais relevantes.

# Marcos semestrais
periodos = pd.date_range(
    start=inicio,
    end=fim,
    freq='1MS'
)

serie = []

for data_ref in periodos:

    admissao = (
        (dados['Admissao'] <= data_ref) &
        (
            dados['Qualificacao'].isna() |
            (dados['Qualificacao'] > data_ref)
        )
    ).sum()

    qualificacao = (
        (dados['Qualificacao'] <= data_ref) &
        (
            dados['Habilitacao'].isna() |
            (dados['Habilitacao'] > data_ref)
        )
    ).sum()

    habilitacao = (
        (dados['Habilitacao'] <= data_ref) &
        (
            dados['Execucao'].isna() |
            (dados['Execucao'] > data_ref)
        )
    ).sum()

    execucao = (
        (dados['Execucao'] <= data_ref)
    ).sum()

    serie.append([
        data_ref,
        admissao,
        qualificacao,
        habilitacao,
        execucao
    ])

df = pd.DataFrame(
    serie,
    columns=[
        'Semestre',
        'Admissao',
        'Qualificacao',
        'Habilitacao',
        'Execucao'
    ]
)

plt.figure(figsize=(14,8))

plt.stackplot(
    df['Semestre'],
    df['Admissao'],
    df['Qualificacao'],
    df['Habilitacao'],
    df['Execucao'],
    labels=[
        'Admissão',
        'Qualificação',
        'Habilitação',
        'Execução'
    ],
    alpha=0.85
)

plt.title('Evolução da Carteira de Propostas por Semestre')
plt.xlabel('Semestre')
plt.ylabel('Quantidade de Propostas')
plt.legend(loc='upper left')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
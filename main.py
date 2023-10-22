import pandas as pd, openai

#Chave API para chat GPT
API_KEY = 'sua_chave_aqui'

#Extracao
#Extrai os dados de um arquivo csv com a biblioteca pandas
df = pd.read_csv('dados.csv')

#cria uma lista com os valores de cada linha
dados = [(row['Conta'], row['Nome'], row['Saldo'],) for (index, row) in df.iterrows()]

#Transformacao
openai.api_key = API_KEY

def criar_mensagem(nome_cliente, saldo_cliente):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário."
            },
            {
                "role": "user",
                "content": f"Escreva uma mensagem para {nome_cliente}, com o nome dele, sobre a importância de investir o saldo de {saldo_cliente} reais que ele possui. (máximo de 100 caracteres)"}
        ]
    )

    mensagem_cliente = completion.choices[0].message.content.strip('"\n')
    return mensagem_cliente

for cliente in dados:
#    print(cliente[1], cliente[2])
    texto = criar_mensagem(nome_cliente=cliente[1], saldo_cliente=cliente[2])
    with open(f"Mensagem para {cliente[1]}.txt", "w") as arquivo:
        arquivo.write(texto)
from flask import Flask, render_template, request
from pyspark.sql import SparkSession
import pandas as pd

app = Flask(__name__)

# Configuração do Spark
spark = SparkSession.builder.appName("DataSciencePlatform").getOrCreate()

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar dados
@app.route('/processar-dados', methods=['POST'])
def processar_dados():
    # Obter o arquivo enviado pelo usuário
    arquivo = request.files['arquivo']
    
    # Ler dados usando Pandas
    dados_pandas = pd.read_csv(arquivo)

    # Criar um DataFrame Spark a partir do DataFrame Pandas
    dados_spark = spark.createDataFrame(dados_pandas)

    # Realizar operações de processamento com Spark
    # Por Exemplo: Contar o número de registros
    contagem_registros = dados_spark.count()

    return f'O número de registros no arquivo é: {contagem_registros}'

if __name__ == '__main__':
    app.run(debug=True)

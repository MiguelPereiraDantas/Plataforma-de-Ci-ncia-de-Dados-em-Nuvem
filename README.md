# Plataforma de Ciência de Dados em Nuvem

Este projeto é uma plataforma simples de ciência de dados em nuvem que permite a análise de dados em larga escala. A aplicação é construída em Python usando Flask para o servidor web, Pandas para manipulação de dados e PySpark para processamento de dados distribuído.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas em seu ambiente Python:

```bash
pip install flask pandas pyspark
```

## Executando a Aplicação

Execute o seguinte comando para iniciar a aplicação:
```bash
python app.py
```
Acesse a plataforma no seu navegador em http://127.0.0.1:5000/. Você será recebido por uma interface simples para fazer upload e processar arquivos CSV.

### Estrutura do Projeto

`app.py`: O arquivo principal que contém a aplicação Flask.

`templates/`: Diretório que contém os templates HTML. Atualmente, apenas `index.html` está presente.

### Funcionalidades

1. Upload de Arquivos: Os usuários podem fazer upload de arquivos CSV por meio da interface da web.

2. Processamento de Dados com PySpark: Os dados são processados usando PySpark, permitindo operações distribuídas em larga escala.

3. Exemplo de Operação: O exemplo atual conta o número de registros no arquivo CSV.

## Personalização

Sinta-se à vontade para personalizar e expandir este projeto conforme suas necessidades. Adicione mais funcionalidades, conecte a serviços de armazenamento em nuvem ou integre outras ferramentas de ciência de dados.

Observação: Este projeto é uma implementação básica e pode exigir melhorias para ambientes de produção, considerações de segurança e escalabilidade.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e propor melhorias.

##  Licença
Este projeto está licenciado sob a Licença MIT.
 
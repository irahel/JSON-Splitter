# Json Splitter

Esse scritp em `Python` divide um arquivo base `JSON` em múltiplos arquivos menores também no formato `JSON`.

## Instalando Requisitos

O script usa algumas bibliotecas externas e portanto necessita que estejam devidamente instaladas.
Também é necessaria que o módulo `pip` esteja instalado.

Para instalá-las utilize:
```
$ pip install -r requirements.txt
```
## Utilizando o script

A utilização do script é feita passando os parâmetros necessários pelo próprio terminal com a seguinte formatação:

```
$ python3 json_splitter.py <Arquivo JSON BASE> <JSON SAIDA 1> <JSON SAIDA 2> ...
```
- O **Arquivo JSON BASE** deve ser um arquivo válido no formato `JSON`.

- Os campos **JSON SAIDA** precisam conter apenas o nome do arquivo `JSON` sem necessidade de se indicar o formato.

exemplo de utilização que criou os arquivos presentes neste repositório
```
$ python3 json_splitter.py exemplo.json arquivo1 arquivo2 arquivo3
```

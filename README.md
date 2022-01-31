# Json Splitter

Esse scritp em `Python` divide um arquivo base `JSON` em múltiplos arquivos menores também no formato `JSON`.

## Instalando Requisitos

O script usa a biblioteca `numpy` e portanto necessita que esteja devidamente instalada.
Também é necessaria que o `pip` esteja instalado.

Para instalar utilize:
```
$ pip install numpy
```
## Utilizando o script

A utilização do script é feita passando os parâmetros necessários pelo prŕoprio terminal com a seguinte formatação

```
$ python3 json_splitter.py <Arquivo JSON BASE> <JSON SAIDA 1> <JSON SAIDA 2> ...
```
- O **Arquivo JSON BASE** deve ser um arquivo válido no formato `JSON`.

- Os campos **JSON SAIDA** precisam conter apenas o nome do arquivo `JSON` sem necessidade de se indicar o formato.

exemplo de utilização que criou os arquivos presente neste repositório
```
$ python3 json_splitter.py exemplo.json arquivo1 arquivo2 arquivo3
```

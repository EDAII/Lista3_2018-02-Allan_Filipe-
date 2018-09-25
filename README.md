## Lista 4 - Árvores Balanceadas
### Sistema Armazenador de Registros ".csv" em Árvore Balanceada

##### Alunos

| Matrícula | Nome | GitHub |
|--|--|--|
| 15/0029624 | Allan Jefrey Pereira Nobre | @AllanNobre |
| 15/0059213 | Filipe Coelho Hilário Barcelos | @FilipeKN4 |

##### Para executar
O ambiente deve ser configurado para a utilização do framework Django na versão 2.1. Após a configuração, deve-se executar o comando abaixo: 

```sh
$ python3 manage.py runserver
```

Após a execução abra o link do servidor em http://127.0.0.1:8000/.

##### Descrição

Lê-se um arquivo ".csv" de registros, nos quais são armazenados em uma AVL, possibilitando a ordenação rápida pela trajetória em ordem da árvore. Ao final da execução, são mostradas as rotações realizadas, a árvore final e a lista ordenada de registros através da travessia da árvore.

##### Visualização

Para a visualização dos resultados foi utilizado o Framework Django da linguagem de programação Python, de modo que foi possível criar uma interface Web estilizada por meio do framework Bootstrap.  

##### AVL

São indicadas na tela as rotações necessárias para balancear a árvore nas inserções e o resultado final da árvore após a transcrição completa do ".csv" para estas. 

##### Vermelha e Preto

Ainda não implementado.

##### Observações

Seguem dois ".csv" de exemplo de entrada para a aplicação, um com mais registros e outro com menos.
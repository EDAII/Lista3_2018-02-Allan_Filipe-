## Lista 3 - Ordenação O(n log n)
### Sistema Ordenador de Registros em ".csv"

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
A aplicação consiste na leitura de um arquivo de registros ".csv", no qual deve seguir alguns padrões de tratamento de dados antes de ser utilizado como entrada nesse software. As regras de formatação do arquivo de registro são:

- Deve ser um arquivo ".csv";
- A primeira linha do seu arquivo ".csv" deve conter os títulos de descrição das colunas;
- A primeira coluna do seu arquivo ".csv" deve conter a informação que será o parâmetro de busca;
- Os valores da primeira coluna do ".csv" e o parâmetro de busca devem, ambos, ser valores numéricos;
- Os valores da primeira coluna do ".csv" não devem se repetir, ou seja, tem de ser uma Chave Primária;
- Recomenda-se que o arquivo ".csv" nã0 possua valores de céculas vazias;

Após a leitura do ".csv", são executados quatro algorítmos de ordenação e os resultados fornecidos são:

- os tempos de execução de cada um dos algorítmos ao ordenar os registros fornecidos pelo ".csv" escolhido. O formato de saída é:

```sh
nome algorítmo: tempo de execução em segundos
```

Exemplo:

    "Selection Sort Time: 0.000001"

- uma tabela que oferece os registros devidamente ordenados e a possibilidade de busca de qualquer registro por qualquer uma das colunas existentes, além de exportar a tabela ordenada para arquivos das extensões: ".csv", excell, ".pdf". É possível, também, copiar a tabela ou realizar um printscreen.  

É muito importante ressalta que os algorítmos O(n²) aumentam o tempo de execução de forma exponencial dependendo da quantidade de dados, de modo que, um aumento de apenas 1000 dados, por exemplo, pode causar uma demora extremamente maior no tempo de execução.

##### Visualização

Para a visualização dos resultados foi utilizado o Framework Django da linguagem de programação Python, de modo que foi possível criar uma interface Web estilizada por meio do framework Bootstrap.  

##### Ordenação O(n²)

Foram implementados os algorítmos: Insertion Sort, Selection Sort, Bubble Sort e Shell Sort.

##### Ordenação O(n log n)

Foram implementados os algorítmos: Counting Sort, Radix Sort e Quick Sort.

##### Observações
Seguem dois ".csv" de exemplo de entrada para a aplicação, um com mais registros e outro menor.
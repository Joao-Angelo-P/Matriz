# Matriz
Criação de um objeto tipo matriz com métodos e operações de matrizes
Com o intuito de resolver algumas operações com matrizes, esse é objetivo.
OBSERVAÇÕES: não há todos os métodos inclusos de operações de matrizes como matriz inversa, determinante de matriz, operações com 4x4 e por fim ainda não coloquei condições que possam invalidar uma operação matricial, outro exemplo é adição de matrizes com dimensões diferentes.Então, preste atenção que não há condições para acontecer uma operação. veja no livro ou na internet as condiçoes para ocorrer a operação, tudo bem?
Mais tarde posso resolver esses problemas. Mas fique a vontade para baixar e implementar, comentar modificações e tudo de mais.

Vamos a explicação:
Deixei 2 matrizes dentro no arquivo:m1=Matriz([1, 2], [5, 0]) e m2=Matriz([3, -1], [0, 8])
1) Quantidade de vetores: len(m1) --->  2 
2) Adição: m1 + m2 ---> [(4, 1), (5, 8)]
3) Subtração: m1 - m2 ---> [(-2, 3), (5, -8)]
4) Multiplicação: m1 * m2 ---> [(3, 15), (15, -5)]
5) Transposta: m1.t() ---> [[1, 5], [2, 0]]

Para criar objetos: matriz_xemplo = Matriz(n, m), onde n é o numero de listas e m quantidade de números dentro de cada lista. E de novo, fique a vontade pra mandar sugestões ou críticas.

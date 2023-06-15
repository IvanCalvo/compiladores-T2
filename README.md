## Trabalho 2 da disciplina de Compiladores

## Autores

  Ivan Duarte Calvo - RA: 790739  
  João Ricardo Lopes Lovato - RA: 772138  
  Vinícius Borges de Lima - RA: 795316  

## Programas necessários

  O código foi escrito na linguagem *Python 3.10*, e também foi utilizado o *ANTLR 4.12.0*. Os arquivos e instruções para *downloads* e instalações podem ser encontrados nos seguintes endereços:  
  https://www.python.org/downloads/  
  https://www.antlr.org/download.html
    
## Compilação e execução do programa
  
  O arquivo *Lexer* gerado pelo *ANTLR* pode ser criado através do seguinte comando:
     
     antlr4 -Dlanguage=Python3 gramatica.g4

Após isso, a compilação e execução do código *main.py* é realizada com o comando:

    python3 main.py arquivo_de_entrada arquivo_de_saida

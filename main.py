'''
    Autores:
    Ivan Duarte Calvo RA: 790739
    João Ricardo Lopes Lovato RA: 772138
    Vinícius Borges de Lima RA: 795316

    COMPILAÇÃO:
    o programa pode ser compilado através do seguinte comando:
        python3 main.py arquivo_de_entrada.txt arquivo_de_saida.txt
'''

import sys
from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from antlr4.error.ErrorListener import ErrorListener

#classe de mensangens customizadas de erros léxicos
class GramaticaLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        erro = str(e.input)[e.startIndex]

        if erro == '"':
            raise Exception(f'Linha {line}: cadeia literal nao fechada')
        elif erro == '{':
            raise Exception(f'Linha {line}: comentario nao fechado')       
        else:
            raise Exception(f'Linha {line}: {erro} - simbolo nao identificado')

#classe de mensangens customizadas de erros léxicos
class GramaticaParserErrorListener(ErrorListener):
     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        errorText = offendingSymbol.text

        if errorText == '<EOF>':
            errorText = 'EOF'
        
        raise Exception(f'Linha {offendingSymbol.line}: erro sintatico proximo a {errorText}')

# Verificando se todos os argumentos necessarios foram passados
if len(sys.argv) < 3:
    print("É necessário fornecer o nome dos arquivos de entrada e saida como argumento.")
    sys.exit(1)

# Os argumentos representam os arquivos de entrada e saida respectivamente 
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

# Criando um InputStream atraves do arquivo de entrada
input_stream = FileStream(input_file_name, encoding='utf-8')

#Criando um arquivo de saida
output_file = open(output_file_name,"w")

# Utilizando o lexer criado com o ANTLR
lexer = gramaticaLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = gramaticaParser(stream)

#removendo mensagens de erro padrão do ANTLR
lexer.removeErrorListeners()
parser.removeErrorListeners()

#adicionando mensagens de erro customizadas
lexer.addErrorListener(GramaticaLexerErrorListener())
parser.addErrorListener(GramaticaParserErrorListener())

#lista vazia com os erros
listaErros = []

#chamada principal do programa
try:
    parser.programa()

except Exception as error:
    #caso haja erros, coloca os erros na lista
    listaErros.append(str(error))
    listaErros.append("Fim da compilacao")

    #imprime a lista de erros no arquivo de saida
    for item_erro in listaErros:
        output_file.write(f"{item_erro}\n")

output_file.close()
# Generated from gramatica.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#programa.
    def enterPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#programa.
    def exitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#declaracoes.
    def enterDeclaracoes(self, ctx:gramaticaParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#declaracoes.
    def exitDeclaracoes(self, ctx:gramaticaParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:gramaticaParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by gramaticaParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:gramaticaParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by gramaticaParser#variavel.
    def enterVariavel(self, ctx:gramaticaParser.VariavelContext):
        pass

    # Exit a parse tree produced by gramaticaParser#variavel.
    def exitVariavel(self, ctx:gramaticaParser.VariavelContext):
        pass


    # Enter a parse tree produced by gramaticaParser#identificador.
    def enterIdentificador(self, ctx:gramaticaParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#identificador.
    def exitIdentificador(self, ctx:gramaticaParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#dimensao.
    def enterDimensao(self, ctx:gramaticaParser.DimensaoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#dimensao.
    def exitDimensao(self, ctx:gramaticaParser.DimensaoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#tipo.
    def enterTipo(self, ctx:gramaticaParser.TipoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#tipo.
    def exitTipo(self, ctx:gramaticaParser.TipoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#tipo_basico.
    def enterTipo_basico(self, ctx:gramaticaParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#tipo_basico.
    def exitTipo_basico(self, ctx:gramaticaParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:gramaticaParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by gramaticaParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:gramaticaParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by gramaticaParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:gramaticaParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:gramaticaParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#valor_constante.
    def enterValor_constante(self, ctx:gramaticaParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by gramaticaParser#valor_constante.
    def exitValor_constante(self, ctx:gramaticaParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by gramaticaParser#registro.
    def enterRegistro(self, ctx:gramaticaParser.RegistroContext):
        pass

    # Exit a parse tree produced by gramaticaParser#registro.
    def exitRegistro(self, ctx:gramaticaParser.RegistroContext):
        pass


    # Enter a parse tree produced by gramaticaParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:gramaticaParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by gramaticaParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:gramaticaParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by gramaticaParser#parametro.
    def enterParametro(self, ctx:gramaticaParser.ParametroContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parametro.
    def exitParametro(self, ctx:gramaticaParser.ParametroContext):
        pass


    # Enter a parse tree produced by gramaticaParser#parametros.
    def enterParametros(self, ctx:gramaticaParser.ParametrosContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parametros.
    def exitParametros(self, ctx:gramaticaParser.ParametrosContext):
        pass


    # Enter a parse tree produced by gramaticaParser#corpo.
    def enterCorpo(self, ctx:gramaticaParser.CorpoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#corpo.
    def exitCorpo(self, ctx:gramaticaParser.CorpoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmd.
    def enterCmd(self, ctx:gramaticaParser.CmdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmd.
    def exitCmd(self, ctx:gramaticaParser.CmdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdLeia.
    def enterCmdLeia(self, ctx:gramaticaParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdLeia.
    def exitCmdLeia(self, ctx:gramaticaParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:gramaticaParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:gramaticaParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdSe.
    def enterCmdSe(self, ctx:gramaticaParser.CmdSeContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdSe.
    def exitCmdSe(self, ctx:gramaticaParser.CmdSeContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdCaso.
    def enterCmdCaso(self, ctx:gramaticaParser.CmdCasoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdCaso.
    def exitCmdCaso(self, ctx:gramaticaParser.CmdCasoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdPara.
    def enterCmdPara(self, ctx:gramaticaParser.CmdParaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdPara.
    def exitCmdPara(self, ctx:gramaticaParser.CmdParaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:gramaticaParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:gramaticaParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdFaca.
    def enterCmdFaca(self, ctx:gramaticaParser.CmdFacaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdFaca.
    def exitCmdFaca(self, ctx:gramaticaParser.CmdFacaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdAtribuicao.
    def enterCmdAtribuicao(self, ctx:gramaticaParser.CmdAtribuicaoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdAtribuicao.
    def exitCmdAtribuicao(self, ctx:gramaticaParser.CmdAtribuicaoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdChamada.
    def enterCmdChamada(self, ctx:gramaticaParser.CmdChamadaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdChamada.
    def exitCmdChamada(self, ctx:gramaticaParser.CmdChamadaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#cmdRetorne.
    def enterCmdRetorne(self, ctx:gramaticaParser.CmdRetorneContext):
        pass

    # Exit a parse tree produced by gramaticaParser#cmdRetorne.
    def exitCmdRetorne(self, ctx:gramaticaParser.CmdRetorneContext):
        pass


    # Enter a parse tree produced by gramaticaParser#selecao.
    def enterSelecao(self, ctx:gramaticaParser.SelecaoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#selecao.
    def exitSelecao(self, ctx:gramaticaParser.SelecaoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#item_selecao.
    def enterItem_selecao(self, ctx:gramaticaParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#item_selecao.
    def exitItem_selecao(self, ctx:gramaticaParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#constantes.
    def enterConstantes(self, ctx:gramaticaParser.ConstantesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#constantes.
    def exitConstantes(self, ctx:gramaticaParser.ConstantesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:gramaticaParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by gramaticaParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:gramaticaParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by gramaticaParser#op_unario.
    def enterOp_unario(self, ctx:gramaticaParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by gramaticaParser#op_unario.
    def exitOp_unario(self, ctx:gramaticaParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by gramaticaParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:gramaticaParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:gramaticaParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#termo.
    def enterTermo(self, ctx:gramaticaParser.TermoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#termo.
    def exitTermo(self, ctx:gramaticaParser.TermoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#fator.
    def enterFator(self, ctx:gramaticaParser.FatorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#fator.
    def exitFator(self, ctx:gramaticaParser.FatorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#op1.
    def enterOp1(self, ctx:gramaticaParser.Op1Context):
        pass

    # Exit a parse tree produced by gramaticaParser#op1.
    def exitOp1(self, ctx:gramaticaParser.Op1Context):
        pass


    # Enter a parse tree produced by gramaticaParser#op2.
    def enterOp2(self, ctx:gramaticaParser.Op2Context):
        pass

    # Exit a parse tree produced by gramaticaParser#op2.
    def exitOp2(self, ctx:gramaticaParser.Op2Context):
        pass


    # Enter a parse tree produced by gramaticaParser#op3.
    def enterOp3(self, ctx:gramaticaParser.Op3Context):
        pass

    # Exit a parse tree produced by gramaticaParser#op3.
    def exitOp3(self, ctx:gramaticaParser.Op3Context):
        pass


    # Enter a parse tree produced by gramaticaParser#parcela.
    def enterParcela(self, ctx:gramaticaParser.ParcelaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parcela.
    def exitParcela(self, ctx:gramaticaParser.ParcelaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#parcela_unario.
    def enterParcela_unario(self, ctx:gramaticaParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parcela_unario.
    def exitParcela_unario(self, ctx:gramaticaParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by gramaticaParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:gramaticaParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:gramaticaParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by gramaticaParser#exp_relacional.
    def enterExp_relacional(self, ctx:gramaticaParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by gramaticaParser#exp_relacional.
    def exitExp_relacional(self, ctx:gramaticaParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by gramaticaParser#op_relacional.
    def enterOp_relacional(self, ctx:gramaticaParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by gramaticaParser#op_relacional.
    def exitOp_relacional(self, ctx:gramaticaParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expressao.
    def enterExpressao(self, ctx:gramaticaParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expressao.
    def exitExpressao(self, ctx:gramaticaParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#termo_logico.
    def enterTermo_logico(self, ctx:gramaticaParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#termo_logico.
    def exitTermo_logico(self, ctx:gramaticaParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#fator_logico.
    def enterFator_logico(self, ctx:gramaticaParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#fator_logico.
    def exitFator_logico(self, ctx:gramaticaParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#parcela_logica.
    def enterParcela_logica(self, ctx:gramaticaParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#parcela_logica.
    def exitParcela_logica(self, ctx:gramaticaParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#op_logico_1.
    def enterOp_logico_1(self, ctx:gramaticaParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by gramaticaParser#op_logico_1.
    def exitOp_logico_1(self, ctx:gramaticaParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by gramaticaParser#op_logico_2.
    def enterOp_logico_2(self, ctx:gramaticaParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by gramaticaParser#op_logico_2.
    def exitOp_logico_2(self, ctx:gramaticaParser.Op_logico_2Context):
        pass



del gramaticaParser
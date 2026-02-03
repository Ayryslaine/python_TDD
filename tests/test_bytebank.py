from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_200_retornar_25(self):
        #Given
        entrada = "13/03/2000" 
        esperado = 25

        #criando a instância
        funcionario_teste = Funcionario('Teste', entrada, 1111)

        #When
        acao = funcionario_teste.idade()

        #then
        assert acao == esperado

    def test_quando_sobrenome_recebe_Ayryslaine_Leal_deve_retornar_Carvalho(self):
        #Given
        entrada = " Ayryslaine Leal "
        esperado = "Leal"

        ayryslaine = Funcionario(entrada, "18/05/2004", 1111)

        #When
        acao = ayryslaine.sobrenome()

        #then
        assert acao == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        #Given 
        entrada_salario = 100000
        entrada_nome = "Ayryslaine Leal"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "18/05/2004", entrada_salario)

        #When
        acao = funcionario_teste.decrescimo_salario()

        #Then
        assert acao == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
         #Given 
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario("teste", "18/05/2004", entrada_salario)

        #When
        acao = funcionario_teste.calcular_bonus()

        #Then
        assert acao == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_mais_que_1000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            #Given
            entrada_salario = 1000000
            # não é necessário colocar um esperado devido ao Exception

            funcionario_teste = Funcionario("teste", "18/05/2004", entrada_salario)

            #When
            acao = funcionario_teste.calcular_bonus()

            #Then
            assert acao

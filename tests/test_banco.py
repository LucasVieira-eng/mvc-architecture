import unittest
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from model.Cliente import Cliente
from model.Conta import Conta
from model.BancoDados import BancoDados
from controller.Conta_controller import ContaController
from controller.Cliente_controller import ClienteController
from view.Conta_view import ContaView


class MockView:
    """Mock View para testar a comunicação entre Controller e View."""
    def __init__(self):
        self.conta_exibida = None
        self.metodo_chamado = None

    def exibir_conta_criada(self, conta: Conta):
        self.conta_exibida = conta
        self.metodo_chamado = "exibir_conta_criada"

    def imprimir_dados_conta(self, conta: Conta):
        self.conta_exibida = conta
        self.metodo_chamado = "imprimir_dados_conta"


class TestSistemaBancarioMVC(unittest.TestCase):

    def setUp(self):
        self.banco = BancoDados()
        self.banco.limpar()

    def test_criar_cliente(self):
        cliente = Cliente("Carlos Eduardo", "123.456.789-00")
        self.assertEqual(cliente.nome, "Carlos Eduardo")
        self.assertEqual(cliente.cpf, "123.456.789-00")

    def test_cliente_nome_vazio(self):
        with self.assertRaises(ValueError):
            Cliente("", "12345678900")

    def test_criar_conta(self):
        cliente = Cliente("Ana Beatriz", "111.222.333-44")
        conta = Conta(numero=1001, cliente=cliente, saldo_inicial=250.0)
        self.assertEqual(conta.numero, 1001)
        self.assertEqual(conta.cliente.nome, "Ana Beatriz")
        self.assertEqual(conta.saldo, 250.0)

    def test_conta_saldo_negativo(self):
        cliente = Cliente("Ana Beatriz", "111.222.333-44")
        with self.assertRaises(ValueError):
            Conta(numero=1001, cliente=cliente, saldo_inicial=-50.0)

    def test_banco_dados_armazenamento(self):
        cliente = Cliente("Lucas Silva", "000.111.222-33")
        conta = Conta(numero=1001, cliente=cliente, saldo_inicial=100.0)
        
        self.banco.salvar_conta(conta)
        contas = self.banco.obter_todas_contas()
        
        self.assertEqual(len(contas), 1)
        self.assertEqual(contas[0].numero, 1001)

        busca = self.banco.buscar_por_numero(1001)
        self.assertIsNotNone(busca)
        self.assertEqual(busca.cliente.nome, "Lucas Silva")

    def test_controller_fluxo_mvc_completo(self):
        """
        Testa o requisito:
        'Controller: Deve receber os dados da View, instanciar o Cliente,
        instanciar a Conta, salvar na lista do "Model" e, por fim,
        comandar a View para exibir a conta criada.'
        """
        mock_view = MockView()
        controller = ContaController(banco_dados=self.banco, view=mock_view)

        conta_criada = controller.criar_conta(
            nome="Mariana Costa",
            cpf="99988877766",
            saldo_inicial=500.0
        )

        # 1. Verifica se a conta e cliente foram instanciados corretamente
        self.assertIsInstance(conta_criada, Conta)
        self.assertIsInstance(conta_criada.cliente, Cliente)
        self.assertEqual(conta_criada.cliente.nome, "Mariana Costa")
        self.assertEqual(conta_criada.cliente.cpf, "999.888.777-66")
        self.assertEqual(conta_criada.saldo, 500.0)

        # 2. Verifica se foi salvo no Model (BancoDados)
        contas_no_banco = self.banco.obter_todas_contas()
        self.assertEqual(len(contas_no_banco), 1)
        self.assertEqual(contas_no_banco[0].numero, conta_criada.numero)

        # 3. Verifica se a View foi comandada a exibir a conta
        self.assertEqual(mock_view.metodo_chamado, "exibir_conta_criada")
        self.assertEqual(mock_view.conta_exibida, conta_criada)

    def test_formatacao_view(self):
        cliente = Cliente("Roberto Dias", "123.456.789-00")
        conta = Conta(numero=1050, cliente=cliente, saldo_inicial=1234.56)
        texto = ContaView.formatar_dados_conta(conta)
        self.assertIn("1050", texto)
        self.assertIn("Roberto Dias", texto)
        self.assertIn("123.456.789-00", texto)
        self.assertIn("1,234.56", texto)


if __name__ == "__main__":
    unittest.main()

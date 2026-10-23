from typing import Optional, List
from model.Cliente import Cliente
from model.Conta import Conta
from model.BancoDados import BancoDados
from controller.Cliente_controller import ClienteController


class ContaController:
    """
    Controller responsável por intermediar a lógica de negócios de Contas
    entre a View e os Models (Cliente, Conta, BancoDados).
    """

    def __init__(self, banco_dados: Optional[BancoDados] = None, view=None):
        self._banco_dados = banco_dados if banco_dados is not None else BancoDados()
        self._view = view

    @property
    def banco_dados(self) -> BancoDados:
        return self._banco_dados

    def criar_conta(self, nome: str, cpf: str, saldo_inicial: float, view=None) -> Conta:
        """
        Fluxo solicitado pela especificação MVC:
        1. Recebe os dados da View (nome, cpf, saldo_inicial)
        2. Instancia o Cliente
        3. Instancia a Conta
        4. Salva na lista do "Model" (BancoDados)
        5. Comanda a View para exibir a conta criada
        """
        view_destino = view or self._view

        # Validações dos dados de entrada
        ClienteController.validar_dados(nome, cpf)

        try:
            saldo_num = float(saldo_inicial)
        except (ValueError, TypeError):
            raise ValueError("O saldo inicial deve ser um valor numérico válido.")

        if saldo_num < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")

        # 1 & 2. Instancia o Cliente
        cliente = ClienteController.criar_cliente(nome, cpf)

        # 3. Instancia a Conta
        numero_nova_conta = self._banco_dados.gerar_proximo_numero()
        conta = Conta(numero=numero_nova_conta, cliente=cliente, saldo_inicial=saldo_num)

        # 4. Salva na lista do "Model"
        self._banco_dados.salvar_conta(conta)

        # 5. Comanda a View para exibir a conta criada
        if view_destino is not None:
            if hasattr(view_destino, "exibir_conta_criada"):
                view_destino.exibir_conta_criada(conta)
            elif hasattr(view_destino, "imprimir_dados_conta"):
                view_destino.imprimir_dados_conta(conta)

        return conta

    def buscar_conta_por_numero(self, numero: int, view=None) -> Optional[Conta]:
        """
        Busca uma conta pelo número e comanda a View para exibi-la.
        """
        view_destino = view or self._view
        conta = self._banco_dados.buscar_por_numero(numero)

        if view_destino is not None:
            if hasattr(view_destino, "imprimir_dados_conta"):
                view_destino.imprimir_dados_conta(conta)

        return conta

    def listar_contas(self) -> List[Conta]:
        """
        Retorna todas as contas armazenadas no banco de dados simulado.
        """
        return self._banco_dados.obter_todas_contas()

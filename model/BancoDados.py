from typing import List, Optional
from model.Conta import Conta


class BancoDados:
    """
    Simulação de banco de dados em memória utilizando uma Lista/Array.
    Armazena e gerencia o ciclo de vida das contas criadas.
    """

    _contas_armazenadas: List[Conta] = []
    _sequencial_conta: int = 1001

    def __init__(self):
        # Utiliza a lista compartilhada em nível de classe para garantir
        # persistência durante as reexecuções de scripts (ex: Streamlit)
        self._contas = BancoDados._contas_armazenadas

    def salvar_conta(self, conta: Conta) -> None:
        """
        Adiciona a conta criada na lista/array do banco de dados.
        """
        self._contas.append(conta)

    def obter_todas_contas(self) -> List[Conta]:
        """
        Retorna a lista com todas as contas registradas.
        """
        return list(self._contas)

    def buscar_por_numero(self, numero: int) -> Optional[Conta]:
        """
        Busca e retorna uma conta pelo seu número identificador.
        """
        try:
            num = int(numero)
        except (ValueError, TypeError):
            return None

        for conta in self._contas:
            if conta.numero == num:
                return conta
        return None

    def buscar_por_cpf(self, cpf: str) -> List[Conta]:
        """
        Busca contas vinculadas a um determinado CPF.
        """
        cpf_numeros = "".join(filter(str.isdigit, cpf))
        resultado = []
        for conta in self._contas:
            conta_cpf_numeros = "".join(filter(str.isdigit, conta.cliente.cpf))
            if conta_cpf_numeros == cpf_numeros:
                resultado.append(conta)
        return resultado

    def gerar_proximo_numero(self) -> int:
        """
        Gera o próximo número sequencial de conta único.
        """
        numero = BancoDados._sequencial_conta
        BancoDados._sequencial_conta += 1
        return numero

    def limpar(self) -> None:
        """
        Limpa a lista de contas (útil para testes unitários).
        """
        self._contas.clear()
        BancoDados._sequencial_conta = 1001

from model.Cliente import Cliente


class Conta:
    """
    Model representando a Conta bancária associada a um Cliente.
    """

    def __init__(self, numero: int, cliente: Cliente, saldo_inicial: float = 0.0):
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        self._numero = int(numero)
        self._cliente = cliente
        self._saldo = float(saldo_inicial)

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        self._saldo += valor
        return True

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

    def __str__(self) -> str:
        return (
            f"Conta nº: {self._numero} | "
            f"Titular: {self._cliente.nome} | "
            f"CPF: {self._cliente.cpf} | "
            f"Saldo: R$ {self._saldo:,.2f}"
        )

    def __repr__(self) -> str:
        return f"Conta(numero={self._numero}, cliente={repr(self._cliente)}, saldo={self._saldo})"

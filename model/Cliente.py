class Cliente:
    """
    Model representando o Cliente do banco.
    """

    def __init__(self, nome: str, cpf: str):
        if not nome or not nome.strip():
            raise ValueError("O nome do cliente não pode ser vazio.")
        if not cpf or not cpf.strip():
            raise ValueError("O CPF do cliente não pode ser vazio.")
        self._nome = nome.strip()
        self._cpf = cpf.strip()

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("O nome do cliente não pode ser vazio.")
        self._nome = valor.strip()

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("O CPF do cliente não pode ser vazio.")
        self._cpf = valor.strip()

    def __str__(self) -> str:
        return f"Cliente: {self._nome} | CPF: {self._cpf}"

    def __repr__(self) -> str:
        return f"Cliente(nome='{self._nome}', cpf='{self._cpf}')"

class ClienteView:
    """
    View responsável pelas operações de apresentação e entrada de dados do Cliente.
    """

    @staticmethod
    def formatar_cpf(cpf: str) -> str:
        """
        Formata o CPF no formato 000.000.000-00.
        """
        numeros = "".join(filter(str.isdigit, cpf))
        if len(numeros) == 11:
            return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
        return cpf

    @staticmethod
    def ler_nome() -> str:
        """Método de entrada via console/terminal para o Nome do cliente."""
        return input("Digite o nome do titular: ").strip()

    @staticmethod
    def ler_cpf() -> str:
        """Método de entrada via console/terminal para o CPF do cliente."""
        return input("Digite o CPF do titular: ").strip()

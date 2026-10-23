import re
from model.Cliente import Cliente


class ClienteController:
    """
    Controller para operações envolvendo Clientes.
    """

    @staticmethod
    def validar_dados(nome: str, cpf: str) -> None:
        """
        Valida os dados informados para o cliente.
        """
        if not nome or not nome.strip():
            raise ValueError("O nome do cliente é obrigatório e não pode ser vazio.")

        cpf_limpo = re.sub(r"\D", "", cpf)
        if len(cpf_limpo) != 11:
            raise ValueError("O CPF deve conter exatamente 11 dígitos numéricos.")

    @staticmethod
    def criar_cliente(nome: str, cpf: str) -> Cliente:
        """
        Valida e instancia um objeto Cliente.
        """
        ClienteController.validar_dados(nome, cpf)
        
        # Formata o CPF
        numeros = re.sub(r"\D", "", cpf)
        cpf_formatado = f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
        
        return Cliente(nome=nome.strip(), cpf=cpf_formatado)

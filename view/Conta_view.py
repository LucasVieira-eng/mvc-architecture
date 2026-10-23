from typing import Optional
from model.Conta import Conta


class ContaView:
    """
    View responsável pelas operações de apresentação e entrada relacionadas à Conta bancária.
    """

    @staticmethod
    def ler_saldo_inicial() -> float:
        """Método de entrada via console/terminal para o Saldo Inicial."""
        while True:
            try:
                valor = float(input("Digite o saldo inicial (R$): ").replace(",", "."))
                if valor < 0:
                    print("O saldo inicial não pode ser negativo. Tente novamente.")
                    continue
                return valor
            except ValueError:
                print("Valor inválido. Por favor, insira um número válido.")

    @staticmethod
    def formatar_dados_conta(conta: Conta) -> str:
        """
        Retorna uma string formatada com todas as informações da conta.
        """
        linha_separadora = "=" * 48
        return (
            f"\n{linha_separadora}\n"
            f"          DADOS DA CONTA BANCÁRIA          \n"
            f"{linha_separadora}\n"
            f"  Número da Conta : {conta.numero}\n"
            f"  Titular         : {conta.cliente.nome}\n"
            f"  CPF             : {conta.cliente.cpf}\n"
            f"  Saldo Atual     : R$ {conta.saldo:,.2f}\n"
            f"{linha_separadora}\n"
        )

    @classmethod
    def imprimir_dados_conta(cls, conta: Optional[Conta]) -> None:
        """
        Método para imprimir os dados da conta formatados.
        Suporta exibição tanto em console quanto com Streamlit se estiver disponível.
        """
        if conta is None:
            mensagem = "Conta não encontrada."
            try:
                import streamlit as st
                st.warning(mensagem)
            except Exception:
                print(mensagem)
            return

        texto_formatado = cls.formatar_dados_conta(conta)

        # Se executado dentro do Streamlit, renderiza no display do Streamlit
        try:
            import streamlit as st
            st.success("Conta exibida com sucesso!")
            st.markdown(
                f"""
                <div style="background-color: #f0f7f4; padding: 20px; border-radius: 10px; border: 1px solid #b2dfdb;">
                    <h3 style="color: #004d40; margin-top: 0;">Dados da Conta #{conta.numero}</h3>
                    <p><strong>Titular:</strong> {conta.cliente.nome}</p>
                    <p><strong>CPF:</strong> {conta.cliente.cpf}</p>
                    <p><strong>Saldo Disponível:</strong> <span style="color: #2e7d32; font-size: 1.2em; font-weight: bold;">R$ {conta.saldo:,.2f}</span></p>
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception:
            # Fallback para console padrão
            print(texto_formatado)

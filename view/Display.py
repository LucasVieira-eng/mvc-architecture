import os
import sys
from typing import Optional

# Garante que o diretório raiz do projeto esteja no sys.path para importações absolutas
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
from model.BancoDados import BancoDados
from model.Conta import Conta
from controller.Conta_controller import ContaController
from view.Conta_view import ContaView


class DisplayView:
    """
    View principal com interface gráfica (Streamlit) e métodos de entrada/saída formatada.
    """

    def __init__(self, controller: Optional[ContaController] = None):
        self._controller = controller or ContaController(view=self)

    # -------------------------------------------------------------
    # Métodos de Entrada
    # -------------------------------------------------------------
    def ler_nome(self, chave: str = "nome_input") -> str:
        """Lê o nome do cliente a partir do formulário da interface."""
        return st.session_state.get(chave, "").strip()

    def ler_cpf(self, chave: str = "cpf_input") -> str:
        """Lê o CPF do cliente a partir do formulário da interface."""
        return st.session_state.get(chave, "").strip()

    def ler_saldo_inicial(self, chave: str = "saldo_input") -> float:
        """Lê o saldo inicial a partir do formulário da interface."""
        return float(st.session_state.get(chave, 0.0))

    # -------------------------------------------------------------
    # Métodos de Exibição / Saída Formatada
    # -------------------------------------------------------------
    def imprimir_dados_conta(self, conta: Optional[Conta]) -> None:
        """
        Método formatador responsável por exibir os dados da conta de forma visual e estilizada.
        """
        if not conta:
            st.error("❌ Nenhuma conta encontrada com o número informado.")
            return

        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #f8fbfd 0%, #e8f4f8 100%);
                padding: 24px;
                border-radius: 14px;
                border: 1px solid #c2e1ed;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
                margin: 15px 0;
            ">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #0288d1; padding-bottom: 12px; margin-bottom: 15px;">
                    <h3 style="color: #01579b; margin: 0; font-size: 1.4rem;">🏦 Conta Bancária #{conta.numero}</h3>
                    <span style="background-color: #0288d1; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: bold;">ATIVA</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; font-size: 1.05rem;">
                    <div>
                        <p style="color: #546e7a; margin: 2px 0; font-size: 0.85rem; text-transform: uppercase; font-weight: bold;">Titular</p>
                        <p style="color: #263238; margin: 0; font-size: 1.15rem; font-weight: 600;">{conta.cliente.nome}</p>
                    </div>
                    <div>
                        <p style="color: #546e7a; margin: 2px 0; font-size: 0.85rem; text-transform: uppercase; font-weight: bold;">CPF</p>
                        <p style="color: #263238; margin: 0; font-size: 1.15rem; font-weight: 600;">{conta.cliente.cpf}</p>
                    </div>
                    <div style="grid-column: span 2; background-color: #ffffff; padding: 12px 18px; border-radius: 8px; border-left: 4px solid #2e7d32;">
                        <p style="color: #546e7a; margin: 2px 0; font-size: 0.85rem; text-transform: uppercase; font-weight: bold;">Saldo Disponível</p>
                        <p style="color: #2e7d32; margin: 0; font-size: 1.6rem; font-weight: bold;">R$ {conta.saldo:,.2f}</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    def exibir_conta_criada(self, conta: Conta) -> None:
        """
        Método chamado pelo Controller ao finalizar a criação e persistência da conta.
        """
        st.balloons()
        st.success(f"✅ Conta **#{conta.numero}** criada com sucesso para o cliente **{conta.cliente.nome}**!")
        self.imprimir_dados_conta(conta)

    # -------------------------------------------------------------
    # Renderização da Interface Gráfica Streamlit
    # -------------------------------------------------------------
    def render(self) -> None:
        """Renderiza todo o front-end Streamlit."""
        st.set_page_config(
            page_title="Sistema Bancário MVC",
            page_icon="🏦",
            layout="centered",
            initial_sidebar_state="expanded"
        )

        st.title("🏦 Sistema de Gerenciamento Bancário")
        st.caption("Arquitetura MVC • Model - View - Controller")

        # Sidebar para navegação
        st.sidebar.image("https://img.icons8.com/color/96/bank.png", width=70)
        st.sidebar.title("Menu Bancário")
        opcao = st.sidebar.radio(
            "Selecione uma operação:",
            ("➕ Criar Conta", "🔍 Exibir Dados da Conta", "📋 Todas as Contas"),
            index=0
        )

        st.sidebar.markdown("---")
        st.sidebar.markdown(
            "**Instruções do Sistema:**\n"
            "- **Model**: `Cliente`, `Conta`, `BancoDados`\n"
            "- **View**: `Display.py`, `Conta_view.py`, `Cliente_view.py`\n"
            "- **Controller**: `Conta_controller.py`, `Cliente_controller.py`"
        )

        # ---------------------------------------------------------
        # Aba 1: Criar Conta
        # ---------------------------------------------------------
        if opcao == "➕ Criar Conta":
            st.subheader("Cadastro de Nova Conta Bancária")
            st.write("Preencha as informações do titular para abrir uma nova conta corrente:")

            with st.form("form_criar_conta", clear_on_submit=True):
                nome = st.text_input(
                    "Nome Completo do Titular *",
                    placeholder="Ex: Maria Silva",
                    key="nome_input"
                )
                
                cpf = st.text_input(
                    "CPF do Titular (apenas números ou formatado) *",
                    placeholder="Ex: 123.456.789-00 ou 12345678900",
                    key="cpf_input",
                    max_chars=14
                )
                
                saldo_inicial = st.number_input(
                    "Saldo Inicial (R$) *",
                    min_value=0.0,
                    value=0.0,
                    step=50.0,
                    format="%.2f",
                    key="saldo_input"
                )

                submeter = st.form_submit_button("🚀 Abrir Conta Bancária", use_container_width=True)

            if submeter:
                try:
                    # Envia os dados para o Controller processar
                    self._controller.criar_conta(
                        nome=nome,
                        cpf=cpf,
                        saldo_inicial=saldo_inicial,
                        view=self
                    )
                except ValueError as erro:
                    st.error(f"⚠️ Erro ao criar conta: {str(erro)}")
                except Exception as ex:
                    st.error(f"❌ Ocorreu um erro inesperado: {str(ex)}")

        # ---------------------------------------------------------
        # Aba 2: Exibir Dados da Conta
        # ---------------------------------------------------------
        elif opcao == "🔍 Exibir Dados da Conta":
            st.subheader("Consultar Dados da Conta")
            st.write("Informe o número da conta cadastrada para visualizar as informações formatadas:")

            contas_existentes = self._controller.listar_contas()

            if not contas_existentes:
                st.info("ℹ️ Nenhuma conta cadastrada no momento. Crie uma conta no menu 'Criar Conta'.")
            else:
                opcoes_contas = {f"Conta #{c.numero} - {c.cliente.nome}": c.numero for c in contas_existentes}
                
                col1, col2 = st.columns([2, 1])
                with col1:
                    selecao = st.selectbox(
                        "Selecione uma conta para visualizar:",
                        options=list(opcoes_contas.keys())
                    )
                with col2:
                    st.write("")
                    st.write("")
                    buscar_selecionada = st.button("🔎 Visualizar Conta", use_container_width=True)

                if buscar_selecionada and selecao:
                    num_conta = opcoes_contas[selecao]
                    conta_encontrada = self._controller.buscar_conta_por_numero(num_conta, view=self)

                st.markdown("---")
                st.write("**Ou busque digitando o número exato da conta:**")
                col_num, col_btn = st.columns([2, 1])
                with col_num:
                    numero_digitado = st.number_input(
                        "Número da Conta",
                        min_value=1,
                        step=1,
                        value=contas_existentes[0].numero if contas_existentes else 1001
                    )
                with col_btn:
                    st.write("")
                    st.write("")
                    btn_buscar = st.button("Buscar por Número", use_container_width=True)

                if btn_buscar:
                    conta_encontrada = self._controller.buscar_conta_por_numero(int(numero_digitado), view=self)

        # ---------------------------------------------------------
        # Aba 3: Todas as Contas
        # ---------------------------------------------------------
        elif opcao == "📋 Todas as Contas":
            st.subheader("Relatório Geral de Contas Cadastradas")
            contas = self._controller.listar_contas()

            if not contas:
                st.info("ℹ️ Nenhuma conta cadastrada no momento.")
            else:
                dados_tabela = [
                    {
                        "Número": c.numero,
                        "Titular": c.cliente.nome,
                        "CPF": c.cliente.cpf,
                        "Saldo (R$)": f"R$ {c.saldo:,.2f}"
                    }
                    for c in contas
                ]
                st.dataframe(dados_tabela, use_container_width=True)
                
                total_saldo = sum(c.saldo for c in contas)
                m1, m2 = st.columns(2)
                m1.metric("Total de Contas", len(contas))
                m2.metric("Montante Total Custodiado", f"R$ {total_saldo:,.2f}")


def main():
    display = DisplayView()
    display.render()


if __name__ == "__main__":
    main()

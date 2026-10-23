"""
Ponto de entrada principal da aplicação bancária MVC.
Pode ser executado com: streamlit run app.py
"""
import sys
import os

# Adiciona diretório raiz ao path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from view.Display import DisplayView

if __name__ == "__main__":
    app = DisplayView()
    app.render()

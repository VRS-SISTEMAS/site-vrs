import os
import sys
from streamlit.web import cli as stcli

# Garante que o entrada.py seja o ponto de partida da VR Soluções
def main():
    sys.argv = [
        "streamlit",
        "run",
        "entrada.py",
        "--server.port",
        "8080",
        "--server.address",
        "0.0.0.0",
    ]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()
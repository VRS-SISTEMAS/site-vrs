import os
import sys
from streamlit.web import cli as stcli

def main():
    # Isso aqui avisa que o entrada.py é o coração do site
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
import json
import os

class CarregadorBaseConhecimento:
    def __init__(self, base_dir="src/base_conhecimento"):
        self.base_dir = base_dir
        self.fatos_path = os.path.join(base_dir, "fatos.json")
        self.regras_path = os.path.join(base_dir, "regras.json")

    def carregar_fatos(self):
        try:
            with open(self.fatos_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise FileNotFoundError(f"Erro ao carregar fatos.json: {e}")

    def carregar_regras(self):
        try:
            with open(self.regras_path, "r", encoding="utf-8") as f:
                dados = json.load(f)
                regras = dados.get("regras", [])
                if len(regras) < 20:
                    print(f"Aviso: A base possui apenas {len(regras)} regras. O ideal é ter no mínimo 20.")
                return regras
        except Exception as e:
            raise FileNotFoundError(f"Erro ao carregar regras.json: {e}")

if __name__ == "__main__":
    carregador = CarregadorBaseConhecimento()
    fatos = carregador.carregar_fatos()
    regras = carregador.carregar_regras()
    print(f"Sucesso! Carregados {len(fatos['planos_disponiveis'])} planos e {len(regras)} regras de produção.")
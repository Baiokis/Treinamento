import os
import subprocess

YOLOV5_DIR = "yolov5"  # Caminho para o diretório YOLOv5
MODEL_PATH = ".pt"  # Caminho para os pesos do modelo
DATA_YAML_PATH = "data.yaml"  # Caminho para o arquivo de configuração de dados

val_command = [
    "python", os.path.join(YOLOV5_DIR, "val.py"),
    "--weights", MODEL_PATH,
    "--data", DATA_YAML_PATH,
    "--img", "640",  # Tamanho da imagem para validação
]

print("Iniciando a validação do modelo...")
try:
    subprocess.run(val_command, check=True)
    print("Validação concluída com sucesso!")
except subprocess.CalledProcessError as e:
    print(f"Erro durante a validação: {e}")

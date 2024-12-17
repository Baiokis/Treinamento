import os
import subprocess
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

YOLOV5_DIR = "yolov5"
DATA_YAML_PATH = "data.yaml"

HYPERPARAMETERS = {
    "epochs": 450,
    "batch_size": 16,
    "img_size": 640,
}

train_command = [
    "python", os.path.join(YOLOV5_DIR, "train.py"),
    "--img", str(HYPERPARAMETERS["img_size"]),
    "--batch", str(HYPERPARAMETERS["batch_size"]),
    "--epochs", str(HYPERPARAMETERS["epochs"]),
    "--data", DATA_YAML_PATH,
    "--weights", "",  # Treinamento do zero
    "--cfg", os.path.join(YOLOV5_DIR, "models", "yolov5s.yaml")  # Configuração do modelo
]


print("Iniciando o treinamento do modelo do zero com YOLOv5...")
try:
    subprocess.run(train_command, check=True)
    print("Treinamento concluído com sucesso!")
except subprocess.CalledProcessError as e:
    print(f"Erro durante o treinamento: {e}")

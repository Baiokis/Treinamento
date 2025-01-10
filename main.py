import os
import subprocess
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

YOLOV5_DIR = "yolov5"
DATA_YAML_PATH = "data.yaml"

HYPERPARAMETERS = {
<<<<<<< HEAD
    "epochs": 200,
=======
    "epochs": 450,
    "batch_size": 16,
    "img_size": 640,
>>>>>>> ee33b1232dc363bda87e29ed99b0d22d983d832b
}

train_command = [
    "python", os.path.join(YOLOV5_DIR, "train.py"),
<<<<<<< HEAD
    "--epochs", str(HYPERPARAMETERS["epochs"]),
    "--data", DATA_YAML_PATH,
    "--weights", "",
=======
    "--img", str(HYPERPARAMETERS["img_size"]),
    "--batch", str(HYPERPARAMETERS["batch_size"]),
    "--epochs", str(HYPERPARAMETERS["epochs"]),
    "--data", DATA_YAML_PATH,
    "--weights", "",  # Treinamento do zero
>>>>>>> ee33b1232dc363bda87e29ed99b0d22d983d832b
    "--cfg", os.path.join(YOLOV5_DIR, "models", "yolov5s.yaml")
]


print("Iniciando o treinamento do modelo do zero com YOLOv5...")
try:
    subprocess.run(train_command, check=True)
    print("Treinamento concluído com sucesso!")
except subprocess.CalledProcessError as e:
<<<<<<< HEAD
    print(f"Erro durante o treinamento: {e}")
=======
    print(f"Erro durante o treinamento: {e}")
>>>>>>> ee33b1232dc363bda87e29ed99b0d22d983d832b

from ultralytics import YOLO


def main():
    # Load a model
    model = YOLO("yolov8n.pt")  # build a new model from scratch

    # Use the model
    results = model.train(
        data="00_config.yaml", epochs=1, batch=32, workers=2, device=0
    )  # train the model, puedes usar tambien el parametro workers=1 para mejorar el rendimiento, patience=10 para early stopping, imgsz=640 para mejorar el rendimiento,


if __name__ == "__main__":
    main()

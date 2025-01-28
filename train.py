from ultralytics import YOLO

model = YOLO("pretrained_weights/yolo11m.pt")

if __name__ == '__main__':
    output = model.train(
        data=r"C:\Users\edmun\Desktop\VSCode Projects\Yonder\Yonder-CV-Experimenting\datasets\sc_uni_dataset\data.yaml", 
        epochs=300,
        batch=16,
        imgsz=640,
        device='cuda',
        workers=10,
        lr0=1e-6,
        patience=15
    )

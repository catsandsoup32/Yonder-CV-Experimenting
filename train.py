from ultralytics import YOLO

model = YOLO("pretrained_weights/yolo11s.pt")

output = model.train(
    data="datasets/baseline_data/data.yaml", 
    epochs=10,
    batch=16,
    imgsz=640,
    device='cuda',
    workers=0
)

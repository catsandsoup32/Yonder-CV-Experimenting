from ultralytics import YOLO

model = YOLO("pretrained_weights/yolo11s.pt")

output = model.train(
    data="datasets/sc_uni_dataset/data.yaml", 
    epochs=150,
    batch=16,
    imgsz=640,
    device='cuda',
    workers=0
)

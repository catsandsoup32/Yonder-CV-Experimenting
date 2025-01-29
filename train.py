from ultralytics import YOLO

model = YOLO("pretrained_weights/yolo11s.pt")

if __name__ == '__main__':
    output = model.train(
        data=r"C:\Users\edmun\VSC_DIRS\Yonder-CV-Experimenting\datasets\january_data\data.yaml", 
        epochs=1000,
        batch=16,
        imgsz=640,
        device='cuda',
        workers=8,
        optimizer='AdamW',
        lr0=1e-5,
        patience=20,
        pretrained=True
    )

# Training notes

# YoloV11 with january dataset, 300/100 COCO in train/val
# auto -> train5

# YoloV11 with january dataset, 300/100 COCO in train/val
# 1e-5 -> train6
from ultralytics import YOLO

#model = YOLO("pretrained_weights/yolo8s.pt")
model = YOLO("yolo11s.pt")

if __name__ == '__main__':
    output = model.train(
        data=r"C:\Users\edmun\VSC_DIRS\Yonder-CV-Experimenting\datasets\march_data_large_flip\data.yaml", 
        epochs=1000,
        batch=16,
        imgsz=640,
        device='cuda',
        workers=8,
        optimizer='AdamW',
        lr0=1e-5,
        patience=20,
        weight_decay=1e-4,
        pretrained=True
    )

# Training notes

# YoloV11 with january dataset, 300/100 COCO in train/val
# auto -> train5

# YoloV11 with january dataset, 300/100 COCO in train/val
# 1e-5 -> train6

# YoloV8 with sc dataset, 300/100 COCO in train/val
# lr=1e-5 weightdecay=1e-4 -> train7

# YOLO11 with march dataset (max roboflow flip), same COCO numbers
# lr0=1e-5 weightdecay=1e-4
# trying medium instead of small
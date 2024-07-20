from ultralytics import YOLO

# Initialize model
model = YOLO('yolov8n.pt')
# 训练
model.train(data='./data/data.yaml', epochs=50,batch=8,imgsz=640,device=0)
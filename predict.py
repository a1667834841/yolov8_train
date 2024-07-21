import os
from ultralytics import YOLO

# 检测目标

save_dir = 'data/test/results'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

    
# model = YOLO('yolov8n.pt')
model = YOLO('best.pt')
results = model('test/images', save=True, show=True) 

print(results)
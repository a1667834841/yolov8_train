import os
from ultralytics import YOLO

# 检测目标

save_dir = 'data/test/results'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

    
model = YOLO('best.pt')
results = model('data/test/images', save=True, save_conf=True, conf=0.60, show=True,save_dir=save_dir) 

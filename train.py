from ultralytics import YOLO
import ultralytics 

import torch

# ultralytics.checks()  

# print(torch.cuda.device_count()) # 显卡数量

# print(torch.__version__) # pytorch版本
# print(torch.version.cuda) # cuda版本
# print(torch.cuda.is_available()) # 查看cuda是否可用



if __name__ == '__main__':
    # Initialize model
    model = YOLO('yolov8n.pt')
    # 训练
    model.train(data='./data/data.yaml', epochs=100,batch=8,imgsz=640,device=0,workers=2)
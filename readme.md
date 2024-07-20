## 资料
https://www.javabase.cn/docs/ai/yolov8/yolo-v8-1

https://www.bilibili.com/video/BV1jm421579G/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=da86a2897103c910b7b5cff1f2618ad9

一、yolo10 本部部署
1、安装好python3.10和Git
2、创建一个yolo10文件夹
3、命令窗口执行安装指令
pip install supervision labelme  labelme2yolo huggingface_hub google_cloud_audit_log
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install git+https://github.com/THU-MIG/yolov10.git
二、yolo10 摄像头检测物体
1、python yolov10-infer.py 训练之前测试
2、python gen-imgs.py 运行截图程序准备训练数据
3、roboflow在线标注(或者本地用labelme标注 )
4、yolo detect train data=yolo10-test/data.yaml model=yolov10n.pt epochs=30 batch=8 imgsz=640 device=0
5、python yolov10-detect.py 测试训练后的模型
三、本地标注工具
1、labelme 运行本地标注工具
2、labelme2yolo --json_dir D:\github\yolo10\output_images
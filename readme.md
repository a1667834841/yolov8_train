## 资料
https://www.javabase.cn/docs/ai/yolov8/yolo-v8-1

https://www.bilibili.com/video/BV1jm421579G/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=da86a2897103c910b7b5cff1f2618ad9


## 测试命令·
### 目标检测
yolo task=detect mode=predict model="./yolov8n.pt" conf=0.25 source="./ultralytics/assets/bus.jpg"


### 具体步骤
一、yolo10 本部部署
1、安装好python3.10和Git
2、创建一个yolo10文件夹
3、命令窗口执行安装指令

```sh
<!-- 安装 ultralytics-->
pip install ultralytics

pip install supervision labelme  labelme2yolo huggingface_hub google_cloud_audit_log

# 如果有显卡可以使用 下面命令 来训练支持显卡
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 (Python 3.10.7 无效)
# 显卡1050ti python 环境3.7 适合下面这条（梯子勿开）

pip install torch==1.8.2 torchvision==0.9.2 torchaudio==0.8.2 --extra-index-url https://download.pytorch.org/whl/lts/1.8/cu102 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com


pip install git+https://github.com/THU-MIG/yolov10.git

# 模型验证
yolo task=detect mode=val model=runs/detect/train11/weights/best.pt data=data/data.yaml
```

二、yolo10 摄像头检测物体
1、python yolov10-infer.py 训练之前测试
2、python gen-imgs.py 运行截图程序准备训练数据
3、roboflow在线标注(或者本地用labelme标注 )
4、yolo detect train data=yolo10-test/data.yaml model=yolov10n.pt epochs=30 batch=8 imgsz=640 device=0
5、python yolov10-detect.py 测试训练后的模型
三、本地标注工具
1、labelme 运行本地标注工具
2、labelme2yolo --json_dir D:\github\yolo10\output_images

## 结果
### 20240721
![20240721161106](https://img.ggball.top/picGo/20240721161106.png)

## 相关资料

### 在线标注


### python虚拟环境管理工具venv教程
https://vra.github.io/2021/01/03/venv-intro/

```sh
## 创建虚拟环境
python -m venv yolov8

## 激活虚拟环境
.\yolov8\Scripts\activate

# 删除虚拟环境
rm -rf 

```

### anaconda 教程
https://www.runoob.com/python-qt/anaconda-tutorial.html

### 问题解决

#### 训练出现 Broken pipe
![20240721154513](https://img.ggball.top/picGo/20240721154513.png)
```sh
\yolo\lib\multiprocessing\reduction.py", line 60, in dump
    ForkingPickler(file, protocol).dump(obj)
BrokenPipeError: [Errno 32] Broken pipe
```
https://blog.csdn.net/qq_44703886/article/details/116749321

解决办法 
调整workers数量 默认为8
![20240721154818](https://img.ggball.top/picGo/20240721154818.png)
```sh
model.train(data='./data/data.yaml', epochs=100,batch=8,imgsz=640,device=0,workers=2)
```


![20240721154524](https://img.ggball.top/picGo/20240721154524.png)
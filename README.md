## yolov8-yolov8-obb
### 使用yolov8-obb进行图像检测训练
#### 1.在虚拟环境里安装yolo运行环境
yolo8为例

'''
pip install ultralytics==8.0.0 
'''
#### 2.准备数据集
原始图像和对应的json文件，使用labels_obb转为.txt文件\
原始图片和对应的.txt文件。按照data_build里面的格式创建
#### 3.运行train.py

import os 
import random 
import shutil 
from pathlib import Path 
 
def split_dataset(image_dir, label_dir, output_root, ratio=0.9):
    """
    按比例划分数据集 
    
    参数：
        image_dir: 图片源目录 
        label_dir: 标签源目录 
        output_root: 输出根目录 
        ratio: 训练集比例（默认0.9）
    """
    # 创建输出目录结构 
    (Path(output_root)/'images/train').mkdir(parents=True, exist_ok=True)
    (Path(output_root)/'labels/train').mkdir(parents=True, exist_ok=True)
    (Path(output_root)/'images/val').mkdir(parents=True, exist_ok=True)
    (Path(output_root)/'labels/val').mkdir(parents=True, exist_ok=True)
    
    # 获取匹配的文件对（去除扩展名）
    images = {f.stem:  f for f in Path(image_dir).glob('*') if f.suffix.lower()  in ['.jpg','.png']}
    labels = {f.stem:  f for f in Path(label_dir).glob('*') if f.suffix.lower()  in ['.txt','.json']}
    
    # 校验匹配性 
    common_keys = set(images.keys())  & set(labels.keys()) 
    print(f"共找到 {len(common_keys)} 对有效数据")
    
    # 随机划分 
    key_list = sorted(common_keys)
    random.seed(42)   # 固定随机种子确保可复现 
    random.shuffle(key_list) 
    
    split_idx = int(len(key_list) * ratio)
    train_keys = key_list[:split_idx]
    test_keys = key_list[split_idx:]
    
    # 文件复制（保持原名）
    for key in train_keys:
        shutil.copy2(images[key],  Path(output_root)/'images/train')
        shutil.copy2(labels[key],  Path(output_root)/'labels/train/')
        
    for key in test_keys:
        shutil.copy2(images[key],  Path(output_root)/'images/val')
        shutil.copy2(labels[key],  Path(output_root)/'labels/val')
    
    print(f"划分完成：训练集 {len(train_keys)} 对 | 测试集 {len(test_keys)} 对")
 
# 使用示例 
split_dataset(
    image_dir='文件夹路径',
    label_dir='文件夹路径', 
    output_root='文件夹路径'
)
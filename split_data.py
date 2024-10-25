import os
import shutil
import random

def split_data(source_dir, train_dir, val_dir, split_size=0.8):
    for category in os.listdir(source_dir):
        category_path = os.path.join(source_dir, category)
        if os.path.isdir(category_path):
            images = os.listdir(category_path)
            random.shuffle(images)

            split_point = int(len(images) * split_size)
            train_images = images[:split_point]
            val_images = images[split_point:]

            train_category_dir = os.path.join(train_dir, category)
            val_category_dir = os.path.join(val_dir, category)

            os.makedirs(train_category_dir, exist_ok=True)
            os.makedirs(val_category_dir, exist_ok=True)

            for img in train_images:
                shutil.copy(os.path.join(category_path, img), train_category_dir)
            
            for img in val_images:
                shutil.copy(os.path.join(category_path, img), val_category_dir)

source_dir = 'D:\\EifficientNet\\ALL'  # Thư mục chứa toàn bộ dữ liệu ban đầu
train_dir = 'D:\\EifficientNet\\data\\train' # Thư mục chứa ảnh huấn luyện
val_dir = 'D:\\EifficientNet\\data\\val'     # Thư mục chứa ảnh validation

split_data(source_dir, train_dir, val_dir)

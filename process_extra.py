# Adds 5000 coco 2017 val images to a dataset
from pathlib import Path
import shutil
import os

new_dir = Path(r"C:\Users\edmun\VSC_DIRS\Yonder-CV-Experimenting\datasets\val2017")

def add_coco_data(new_dir):
    
    for idx, file in enumerate(new_dir.glob("*")):
        file_name = str(file).split("\\")[-1].removesuffix(".jpg") + ".txt"

        if idx < 300: save_dir = 'train' 
        elif idx < 400: save_dir = 'valid'
        else: break
            #save_dir = 'test'

        shutil.copy(file, rf"C:\Users\edmun\VSC_DIRS\Yonder-CV-Experimenting\datasets\sc_data\{save_dir}\images")
        with open(rf"C:\Users\edmun\VSC_DIRS\Yonder-CV-Experimenting\datasets\sc_data\{save_dir}\labels\{file_name}", 'w') as file: pass
        print(idx)

def loop_remove(data_path, dir_type):
    for idx, file in enumerate(os.listdir(os.path.join(data_path, f'{dir_type}/images'))):
        file_name = str(file).removesuffix(".jpg")
        file_first_char = file_name[0]
        if (file_first_char == '0'):
            os.remove(os.path.join(data_path, f'{dir_type}/images', file_name + '.jpg'))
            os.remove(os.path.join(data_path, f'{dir_type}/labels', file_name +'.txt'))

def remove_all_coco_imgs(data_path):
    loop_remove(data_path, 'train')
    loop_remove(data_path, 'valid')
    loop_remove(data_path, 'test')


# test path is Path object 
def add_test_data_to_train(test_path, train_path):
    for file in os.listdir(os.path.join(test_path, "/images")):
        label_name = str(file).removesuffix(".jpg") + '.txt' 
        shutil.copy(file, f"datasets/{train_path}/images")
        with open(f"datasets/{train_path}/labels/{label_name}", 'w') as file: pass
        
    

if __name__ == '__main__':
    add_coco_data(new_dir)
    #remove_all_coco_imgs(Path(r"C:\Users\edmun\Desktop\VSCode Projects\Yonder\Yonder-CV-Experimenting\datasets\sc_uni_dataset"))
    pass        
        
        
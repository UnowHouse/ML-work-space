import os
import shutil

"""
    ck+的label
"""
labels = {'0':'neutral','1':'anger','2':'contempt','3':'disgust','4':'fear','5':'happy','6':'sadness','7':'surprise','8':'null_msg','-1':'unknown'}

"""
    数据集：path->label
"""
dataset={}

"""
    读取label信息

    1. 迭代读取目录
    2. 读取label文件的信息
        1).判断是否含有label文件
        2).f.read()[0:1]截取label信息的主要部分
        3).相对格式化路径
        4).存入字典   
    3. 传入的参数，即路径为所有文件的最近一级的汇总目录     
"""
def read_dir_load_dataset(path):

    childs = os.listdir(path)
    if not childs:
        path = format_path(path,'Emotion/','')
        dataset[path] = '-1'

    for child in childs:
        childpath = os.path.join(path,child)
        if os.path.isdir(childpath):
            readDir(childpath)
        else:
            with open(childpath,'r+') as f:                 
                label = f.read().strip()[0:1]
                if len(label) == 0:
                    label = '8'
                path = format_path(childpath,'Emotion/','_emotion.txt')
                dataset[path] = label

"""
    格式化路径
"""
def format_path(path,prefix,suffix):
    pre_len = len(prefix)
    return path[path.index(prefix)+pre_len:path.rfind(suffix)]

"""
    复制并分类数据到工作空间
    
    1.遍历dataset字典
        1).格式化拼接路径
        2).判断是否有字典中是否有label
    2.移动数据
        1).将数据复制到相对应的label目录
        2).若不存在该label目录，则新建
        3).将不存在label的数据统一存放到unknown目录

    3.传入的参数，即路径为所有文件的最近一级的汇总目录
    参数格式：data_path='dir1/',save_path='dir2/' 
            !! data_path,save_path 必须是以/结尾   
"""
def classify_save(data_path,save_path,img_type='.png'):
    if not os.path.exists(data_path):
        raise "data_path isn't exist!"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for key in dataset:
        label_path = save_path+labels[dataset[key]]
        if not os.path.exists(label_path):
            os.makedirs(label_path)
        if dataset[key] == '-1':
            dir_path = os.path.join(data_path,key)
            dst_dir = os.path.join(label_path,key)
            shutil.copytree(dir_path,dst_dir)
            print(dir_path,dst_dir)
            continue

        file_path = data_path+key+img_type    
        print(label_path,file_path[file_path.rfind('/'):])
        dstfile = os.path.join(label_path,file_path[file_path.rfind('/')+1:])
        shutil.copyfile(file_path,dstfile)

"""
    移动没有label文件的unknown数据

    1.遍历data_path,!注意：data_path必须是所有文件的汇总目录
        1)判断是否为目录
        2)递归遍历子目录
    2.判断新目录是否存在
        1)创建
    3.移动目录中最后一个文件和中间文件到新目录，移完结束该次遍历
"""
def move_ck_file_from_unknown(data_path,save_path):
    files = os.listdir(data_path)
    for path in files:
        child_path = os.path.join(data_path,path)
        if os.path.isdir(child_path):
            move_ck_file_from_unknown(child_path,save_path)
            continue
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        # print(data_path)
        mid = int(len(files)/2)
        startpath1 = os.path.join(data_path,files[-2])
        startpath2 = os.path.join(data_path,files[mid])
        # print(startpath1,startpath2)
        endpath1 = os.path.join(save_path,files[-1])
        endpath2 = os.path.join(save_path,files[mid])
        # print("hehe",endpath1,endpath2)
        
        try:
            print(startpath1+"->"+endpath1)
            shutil.move(startpath1,endpath1)
            print(startpath2+"->"+endpath2)
            shutil.move(startpath2,endpath2)
        except FileNotFoundError as e:
            continue
        continue

if __name__ == '__main__':
    move_ck_file_from_unknown('beautiful_data/unknown','beautiful_unknown')
    # read_dir_load_dataset('Emotion_labels/Emotion/')
    # classify_save('extended-cohn-kanade-images/cohn-kanade-images/','beautiful_data/')
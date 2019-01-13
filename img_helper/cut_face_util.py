# -*- coding: UTF-8 -*-  
import cv2
import os
import argparse

FaceXmlPath = "opencv-master/data/haarcascades/haarcascade_frontalface_alt2.xml"

face_cascade = cv2.CascadeClassifier(FaceXmlPath)



def cut_face_from_img(img_path,new_path,type='jpg',is_rgb=False):

    index = 0
    img = cv2.imread(img_path)
    try:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    except:
        gray = img    
    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.15,minNeighbors = 5,minSize = (5,5),flags = 2)	
    if len(faces)>0:
        for(x,y,w,h) in faces:

            img = img[y:y+h,x:x+w] if is_rgb else gray[y:y+h,x:x+w]
            if w>160:
                img = cv2.resize(img,(160,160),interpolation=cv2.INTER_AREA)
            if w<160:
                img = cv2.resize(img,(160,160),interpolation = cv2.INTER_CUBIC)

            name = new_path+"_"+str(index)+'.'+type
            cv2.imwrite(name,img)
            print('finished ',name)
            index += 1

def cut_face_from_dir(dir_path,save_path):
    list = os.listdir(dir_path)
    is_exist = os.path.exists(save_path)
    if not is_exist:
        os.makedirs(save_path)

    for image in list:
        id_tag = image.find(".")
        name = image[0:id_tag]
        cut_face_from_img(dir_path+'/'+image,save_path+'/'+name)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--input_path', type=str)
    parser.add_argument('--save_path', type=str)
    args = parser.parse_args()

    if args.input_path is None or args.save_path is None:
        raise RuntimeError("must be input the arguments,such as --input_dir=xx,--save_dir=xx")

    input_path = args.input_path
    save_path = args.save_path
    cut_face_from_dir(input_path,save_path)
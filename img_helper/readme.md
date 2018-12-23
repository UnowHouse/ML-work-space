
## 数据收集助手

### spider

- `/utils/spider_util/baidu_spider.py`，爬取baidu.image
- `/utils/spider_util/proxy_ip.txt` ，代理ip集

使用：
```sh
python3 baidu_spider.py --keywords=key1,key2,... --save_path=./ --pages=5
```
- --keywords 要搜索的关键字，可以同时爬取多个关键字，以逗号隔开，不可为空
- --save_path 保存的路径，不可为空
- --pages 爬取的页数，默认为5

### 截取图片人脸

`cut_face_util.py`
读取目录下所有的图片文件，截取人脸，图片保存格式为jpg，命名为遍历序号


- --input_path 要读取的目录路径，不可为空
- --save_path 要保存的目录路径，不可为空

要保存的路径不存在则会自动创建，保存的图片shape为160\*160\*1

人脸检测模型使用opencv的haarcascade_frontalface_alt2分类器



###安装opencv-python

在ubuntu下安装cv2
```bash
pip3 install opencv-python

```
完成之后若导入时出现以下错误
![1545026746(1)](assets\1545026746(1).jpg)

安装对应的软件包解决

```bash
apt-get install libsm6
apt-get install libxrender1
apt-get install libxext-dev
```

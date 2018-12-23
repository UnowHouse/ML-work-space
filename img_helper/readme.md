##数据收集助手

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

人脸检测模型使用opencv的haarcascade_frontalface_alt2分类器

默认shape为160*160*1

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

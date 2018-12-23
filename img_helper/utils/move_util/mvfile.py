import os,shutil

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print ("move %s -> %s"%( srcfile,dstfile))

# root = "vehicle2"
# for dirpath, dirnames, filenames in os.walk(root):
# 	print(dirpath,dirnames,filenames[1])
# 	print(len(filenames))

def splitDir(srcdir):
	index = 0
	currentDir = ''
	for dirpath, dirnames, filenames in os.walk(srcdir):
	    for i in range(len(filenames)):
	    	if i % 500 == 0:
	    		index += 1
	    		currentDir = srcdir+str(index)
	    		if not os.path.exists(currentDir):
	    			os.makedirs(currentDir)
	    	shutil.move(os.path.join(dirpath, filenames[i]),os.path.join(currentDir, filenames[i]))
	os.rmdir(srcdir)    	
splitDir('baidu_img')	    	
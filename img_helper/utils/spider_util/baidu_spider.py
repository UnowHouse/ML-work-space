import requests
from urllib.parse import urlencode
import argparse
import random
import os


"""
输入参数有 保存的路径，关键字组，要保存多少页，每页是30张
"""
def get_page(keyword, i, base_url,proxy):
	"""
        获取动态加载返回的Response
		参数：keyword(搜索关键字) i(ajax变化的参数) base_url(请求的url的前半部分)
		返回值：ajax请求的json数据
	"""
	# url的参数
	params = {
		'tn': 'resultjson_com',
		'ipn': 'rj',
		'ct': 201326592,
		'is': '',
		'fp': 'result',
		'queryWord': keyword,
		'cl': '',
		'lm': '',
		'ie': 'utf-8',
		'oe': 'utf-8',
		'adpicid': '',
		'st': '',
		'z': '',
		'ic': '',
		'word': keyword,
		's': '',
		'se': '',
		'tab': '',
		'width': '',
		'height': '',
		'face': '',
		'istype': '',
		'qc': '',
		'nc': '',
		'fr': '',
		'pn': i,
		'rn': 30,
		'gsm': '3c',
		'1530894241678': '',
	}
	# 请求头
	headers = {
		'Host': 'image.baidu.com',
		'X-Requested-With': 'XMLHttpRequests',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	}
	# 完整url
	url = base_url + urlencode(params)
	# 获取html
	response = requests.get(url,headers=headers,proxies=proxy)
	try:
		# 根据状态码判断是否访问成功
		if response.status_code == 200:
			# 返回网页请求的json数据
			return response.json()
	except requests.ConnectionError as e:
		print('Error', e.args)


def parse_page(json):
	"""
		解析json,获取图片的url
	"""
	# 储存图片路径
	img_urls = []
	if json:
		items = json.get('data')
		for item in items:
			img_url = item.get('hoverURL')
			if img_url != None and img_url != '':
				img_urls.append(img_url)
	return img_urls

def download_img(img_url, save_path, img_num,proxy):
	"""
		下载图片
	"""
	try:
		is_exist = os.path.exists(save_path)
		if not is_exist:
			os.makedirs(save_path)
		num = img_num
		img_path = save_path + str(num) + '.jpg'
		response = requests.get(img_url,proxies=proxy).content
		with open(img_path, 'wb') as f:
			f.write(response)
		img_num += 1
		return img_num
	except Exception as e:
		print(e)


if __name__ == '__main__':
	#接收命令行参数
	parser = argparse.ArgumentParser(description='manual to this script')
	#关键字数组
	parser.add_argument('--keywords', type=str)
	#保存的路径
	parser.add_argument('--save_path', type=str)
	#要爬取的页数，默认是5
	parser.add_argument('--pages', type=int,default=5)
	args = parser.parse_args()

	if args.keywords is None or args.save_path is None:
		raise RuntimeError("must be input the arguments,such as --keywords=xx,--save_dir=xx")

	# 代理ip
	proxies=[]
	with open('proxy_ip.txt','r+') as f:
		for line in f:
			(key,value) = line.strip().split()
			proxies.append({key:value})

	#关键字列表
	keywords = args.keywords.split(',')
	# 百度图片url
	base_url = 'https://image.baidu.com/search/acjson?'
	# keyword为搜索关键字，pn为动态加载图片
	# 保存位置
	save_path = args.save_path
	#要爬取的页数
	pages = args.pages
	# 图片序号
	img_num = 0


	for keyword in keywords:
		print(keyword)
		#改变ajax参数
		for i in range(1,pages+1,1):
			i *= 30	
			print(i)	
			# 获取所有图片的url
			img_urls = parse_page(get_page(keyword,i,base_url,random.choice(proxies)))
			for img_url in img_urls:
				img_num = download_img(img_url, save_path, img_num,random.choice(proxies))
				print(keyword + '--finished' + str(img_num),'-- url:'+img_url)
	print('下载图片完成！')
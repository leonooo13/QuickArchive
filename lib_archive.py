# archive.py
import os

def isImg(img_path:str)->bool:
	# 判断是否是图片
	ext=os.path.splitext(img_path)[1].lower()
	image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
	if ext in image_extensions:
		return True
	else:
		return False
def DEBUG():
	img_path='/look/02项目启动阶段/a.png'
	res=isImg(img_path)
	assert res==True
# DEBUG()

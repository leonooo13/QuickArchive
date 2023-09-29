from Docx_render import render_all_docx
from DoDict import genReview
import zipfile
import os
import shutil
def compress_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

def gendox(MyData):
    review=genReview()
    MyData.update(review)
    short={'CorpSName':MyData['CorpSName'].upper()}
    MyData.update(short)
    print(MyData)
    print("render_all_docx")
    render_all_docx(MyData)
    dox_folder="快归_"+MyData['CorpName']
    dox_zip="快归_"+MyData['CorpName']+".zip"
    compress_folder(dox_folder,dox_zip)
    # 删除原始文件
    if os.path.exists(dox_folder):
        shutil.rmtree(dox_folder)
        print("文件夹删除成功！")
    else:
        print("文件夹不存在！")
    if 'img' in MyData and os.path.exists(MyData['img']):
        os.remove(MyData['img'])
    print("创建",dox_zip)
    return dox_zip
# if __name__=="__main__":
#     gendox(mydic)
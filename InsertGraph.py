import docxtpl
from docx.shared import Mm


# 要编辑的docx文档模板路径
def insertImgWord(docx_path,img_path):
    daily_docx = docxtpl.DocxTemplate(docx_path)

    insert_image = docxtpl.InlineImage(daily_docx, img_path, width=Mm(140))
    # 渲染内容
    context = {
        "img":insert_image,
        
    }

    daily_docx.render(context)
    # 保存docx
    daily_docx.save(docx_path)

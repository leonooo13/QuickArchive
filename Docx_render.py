from docxtpl import DocxTemplate, InlineImage
import glob
import os
from docx.shared import Mm
from lib_archive import isImg
# from Datajson import mydic

def replace_placeholder(template, params, output):
    output_dir = os.path.dirname(output)
    os.makedirs(output_dir, exist_ok=True)
    # 加载模板文件
    doc = DocxTemplate(template)
    # 替换模板中的占位符
    doc.render(params)
    doc.save(output)
    # 保存输出文件
    print('归档后的路径' + output)

def render_phase_docx(Phase, params):
    print("render_phase_docx")
    CorpName = params['CorpName']
    docx_template_files = glob.glob(os.path.join(Phase, '*.docx'))
    for docx_template in docx_template_files:
        output_path = docx_template.replace('DocxTemplate', "快归_" + CorpName).replace('_template', '').replace('\\',
                                                                                                               '/')
        docx_template = docx_template.replace('\\', '/')
        if '0305' in docx_template:
            # 单独处理0305
            graph_docx = DocxTemplate(docx_template)
            if os.path.exists(params['img']) and isImg(params['img']):
                # 存在并且是图片
                insert_image = InlineImage(graph_docx, params['img'], width=Mm(140))
                params.update({"img": insert_image})
                graph_docx.render(params)
                graph_docx.save(output_path)
                print('归档后的路径' + output_path)
            else:
                params.update({"img": "请插入拓扑图"})
                graph_docx.render(params)
                graph_docx.save(output_path)
                print('归档后的路径' + output_path)
        else:
            replace_placeholder(docx_template, params, output_path)


def render_all_docx(params):
    # 模板阶段
    Phases = ['DocxTemplate/02项目启动阶段/',
              'DocxTemplate/03项目编制阶段/',
              'DocxTemplate/04现场测评阶段/',
              'DocxTemplate/05分析与报告编制阶段/',
              'DocxTemplate/06项目验收阶段/',
              'DocxTemplate/07资料整理归档阶段/',
              ]
    for i in range(6):
        render_phase_docx(Phases[i], params)
# if __name__=="__main__":
#     render_all_docx(mydic)

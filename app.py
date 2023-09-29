from flask import Flask, render_template, request, send_file
from GenDox import gendox
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("hi")
        Y,AppDateM,AppDateD=request.form.get("AppDate").split('-')
        print("end")
        Y,PreM,PreD=request.form.get("PreDate").split('-')
        Y,PlanM,PlanD=request.form.get("PlanDate").split('-')
        Y,FaM,FaD=request.form.get("FaDate").split('-')
        Y,FpM,FpD=request.form.get("FpDate").split('-')
        Y,EpM,EpD=request.form.get("EpDate").split('-')
        Y,BgRM,BgRD=request.form.get("BgReviewDate").split('-')
        Y,JieXM,JieXD=request.form.get("JieXDate").split('-')
        print("end1")
        Topfile = request.files['TopImg']
        print("hi1")
        data = {
        "PM": request.form.get("PM"),
        "CorpName": request.form.get("CorpName"),
        "ContractNo": request.form.get("ContractNo"),
        "SysName": request.form.get("SysName"),
        "Mider1": request.form.get("Mider1"),
        "Mider2": request.form.get("Mider2"),
        "Lower": request.form.get("Lower"),
        "CorpSName": request.form.get("CorpSName"),
        "Year": int(request.form.get("Year")),
        "AppDateM": AppDateM.zfill(2),
        "AppDateD": AppDateM.zfill(2),
        "PreM": PreM.zfill(2),
        "PreD": PreD.zfill(2),

        "PlanM": PlanM.zfill(2),
        "PlanD":PlanD.zfill(2),

        "FaM": FaM.zfill(2),
        "FaD": FaD.zfill(2),
        "img": Topfile.filename,

        "FpM": FpM.zfill(2),
        "FpD": FpD.zfill(2),
        "AWner": request.form.get("AWner"),

        "EpM": EpM.zfill(2),
        "EpD": EpD.zfill(2),

        "BgRM": BgRM.zfill(2),
        "BgRD": BgRD.zfill(2),

        "JieXM": JieXM.zfill(2),
        "JieXD": JieXD.zfill(2),
        "PmTel": request.form.get("PmTel")
        }
        if Topfile.filename:
            Topfile.save(Topfile.filename)
        print(data)
        print("gendox")
        dox_zip=gendox(data)
        print(dox_zip)
        print(data)
        if os.path.isfile(dox_zip):
            return render_template('index.html',show_download=True,StatuAQ="归档成功",doxzip=dox_zip)
        else:
            return render_template('index.html',show_download=False,StatuAQ="归档失败")
    return render_template('index.html')	
@app.route('/download',methods=['GET', 'POST'])
def download():
    dox_zip = request.args.get('dox_zip')
    print(dox_zip)
    file_path = os.path.join('', dox_zip)  # 使用相对路径，文件放在 static 文件夹下
    @app.after_request
    def remove_file(response):
        try:
            print("开始删除")
            os.remove(file_path)  # 删除文件
        except OSError:
            pass
        return response

    return send_file(file_path, download_name=dox_zip, as_attachment=True)    

if __name__ == '__main__':
    app.run()

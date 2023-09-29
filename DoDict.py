from random import randint

plan_review={
		'record':["描述准确合理，无明显错误及标识","计划时间节点、风险管控、人员安排合理"],
		'res':"通过"
		}

Fa_review={
	"record":["核实拓扑图，并按照不同区域进行互相渗透分析，然后核对资产","资产名称需核实并对应，刷新目录"],
	"res":"修改后可交付客户"
}
Bg_review={
	"record":["1.	资产统计全面合理。\n2. 资产名称需核实并对应，刷新目录。"],
	"res":"修改后可交付客户"
}

def genReview():
	plan_len=len(plan_review['record'])-1
	Fa_len=len(Fa_review['record'])-1
	Bg_len=len(Bg_review['record'])-1

	review={
	'PlanReviewRecord':plan_review['record'][randint(0,plan_len)],
	'PlanReviewRes':plan_review['res'],
	
	'FaReviewRecord':Fa_review['record'][randint(0,Fa_len)],
	'FaReviewRes':Fa_review['res'],

	'BgReviewRecord':Bg_review['record'][randint(0,Bg_len)],
	'BgReviewRes':Bg_review['res']
	}
	return review
# def shortUpper():
# 	short={'CorpSName':MyData['CorpSName'].upper()}
# 	return short

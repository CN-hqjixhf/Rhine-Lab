import json
import base64
from pathlib import Path
import os
#调用文件路径，送去读取
File_name="student_scores.json"
output_name="report.json"
road1=Path(__file__).parent
road2=(road1/"data"/File_name).resolve()
def load_records(road2):
    path=Path(road2)
    if not path.exists:
        raise FileNotFoundError(f"数据文件不存在: {path}")
    try:
        with path.open("r",encoding="utf-8") as f:
            scores=json.load(f)
    except json.JSONDecodeError as exc:
        raise json.JSONDecodeError(
            f"json语法错误:第{exc.lineno}行第{exc.colno}列--{exc.msg}"
            )from exc
    except UnicodeDecodeError as exc:
        raise (f"编码方式错误") from exc 
    if not isinstance(scores,list):
        raise ValueError("文件格式错误")
    return scores
#读取后的数据存入scores
scores=load_records(road2)
def decode_marked_value(value,i):
        result=value[i]
        name=result["name"]
        student_id=result["student_id"]
        str_score=str(result["score"])
        gender=result["gender"]
        submit_time=result["submit_time"]
        if name.startswith("#"):
            result["name"] = normalize_record(name)
        if student_id.startswith("#"):
            result["student_id"] = normalize_record(student_id)
        if str_score.startswith("#"):
            result["score"] = normalize_record(str_score)
        if isinstance(result["score"], str) and result["score"].strip().isdigit():
            result["score"] = int(result["score"])
        if gender.startswith("#"):
            result["gender"] = normalize_record(gender)
        if submit_time.startswith("#"):
            result["submit_time"] = normalize_record(submit_time)
        return result
#去掉开头的"#"，把数据解码后以utf-8返回
def normalize_record(s:str)->bytes:
    s=s.replace("#","")
    try:
        return base64.urlsafe_b64decode(s).decode("utf-8")
    except Exception as e1:
        raise ValueError(f"Failed to decode Base64 string: {str(e1)}")
#把解码后的数据存储进新列表
new_list=[]    
for i in range(0,len(scores)):
    output=decode_marked_value(scores,i)
    new_list.append(output)
#检验空数据和非法数据
def validate_record(record):
    None_error=0
    illegal_error=0
    for i in range(len(record)):
        result=record[i]
        name = str(result.get("name") or "").strip()
        student_id = str(result.get("student_id") or "").strip()
        score = result.get("score")
        score_text = str(score if score is not None else "").strip()
        gender = str(result.get("gender") or "").strip()
        submit_time = str(result.get("submit_time") or "").strip()
        if not (name and student_id and score_text and gender and submit_time):#检查空数据，非空则检验非法数据
            None_error+=1
            empty=1
        else: empty=0
        if empty==0:
            if not(student_id.startswith("2026") and len(student_id) == 10):
                illegal_error+=1
            elif not isinstance(score, int) or not 0 <= score <= 100:
                illegal_error+=1
            elif not ("15:00"<=str(submit_time)<="16:30"):
                illegal_error+=1
    return {"None_error":None_error,"illegal_error":illegal_error}
#统计列表数据
def summarize(records,pass_score):
    total=0
    passed=0
    man=0
    woman=0
    error=0
    after4=0
    before4=0
    for i in range(len(records)):
        alist=[]
        alist.append(records[i])
        info={}
        info=validate_record(alist)
        if info["None_error"]!=0 or info["illegal_error"]!=0:
            error+=1
        else:
                score=alist[0]["score"]
                if not isinstance(score,int):
                    continue
                else:total+=score
                if score >= pass_score:
                    passed+=1
                if alist[0]["gender"]=="男":
                    man+=1
                elif alist[0]["gender"]=="女":
                    woman+=1
                if "16:00"<str(alist[0]["submit_time"])<="16:30":
                    after4+=1
                elif "15:00"<=str(alist[0]["submit_time"])<="16:00":
                    before4+=1
    count=len(records)-error
    average=total/count
    return{
        "count":count,
        "average":average,
        "passed":passed,
        "pass_score":pass_score,
        "gender_counts":{
            "男":man,
            "女":woman,
        },
        "after4":after4,
        "before4":before4,
    }
def write_report(summarize):
    data=summarize
    if not os.path.exists(f"{road1}\\output"):
        os.makedirs(f"{road1}\\output")
    road3=(road1/"output"/output_name)
    path=Path(road3)
    with path.open("w",encoding="utf-8") as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
def main():
    write_report(summarize(new_list,80))
    error=validate_record(new_list)
    print(f"原始数据:{len(scores)}条,有效数据:{len(scores)-error["None_error"]-error["illegal_error"]}")
    print(f"空数据错误数:{error["None_error"]},非法数据错误数:{error["illegal_error"]}")
    print(f"平均分:{summarize(new_list,80)["average"]},80分及格人数:{summarize(new_list,80)["passed"]}")
    print(f"男生有:{summarize(new_list,80)["gender_counts"]["男"]}人,女生有:{summarize(new_list,80)["gender_counts"]["女"]}人")
    print(f"15:30-16:00(含16:00)提交人数:{summarize(new_list,80)["before4"]},16:00-16:30(不含16:00)提交人数:{summarize(new_list,80)["after4"]}")
    print("原始信息输出json到output/output.json")
if __name__ == "__main__":
    raise SystemExit(main())
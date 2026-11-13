import json
import base64
from pathlib import Path
#调用文件路径，送去读取
File_name="student_scores.json"
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
def smmarize(records,pass_score):
    total=0
    passed=0
    man=0
    woman=0
    error=0
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
    }
output2=smmarize(new_list,60)
print(output2)
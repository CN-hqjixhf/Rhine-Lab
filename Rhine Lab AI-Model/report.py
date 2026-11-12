import json
import base64

with open(r"D:\Rhine Lab\Rhine Lab AI-Model\data\student_scores.json","r",encoding="utf-8") as f:
    scores=json.load(f)

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
        if gender.startswith("#"):
            result["gender"] = normalize_record(gender)
        if submit_time.startswith("#"):
            result["submit_time"] = normalize_record(submit_time)
        return result

def normalize_record(s:str)->bytes:
    s=s.replace("#","")
    try:
        return base64.urlsafe_b64decode(s).decode("utf-8")
    except Exception as e1:
        raise ValueError(f"Failed to decode Base64 string: {str(e1)}")

new_list=[]    
for i in range(0,len(scores)):
    output=decode_marked_value(scores,i)
    new_list.append(output)

def validate_record(record):
    None_error=0
    illegal_error=0
    for i in range(0,len(record)):
        result=record[i]
        name=str(result["name"] or "").strip()
        student_id=str(result["student_id"] or "").strip()
        str_score=str(result["score"] or "").strip()
        gender=str(result["gender"] or "").strip()
        submit_time=str(result["submit_time"] or "").strip()
        if not (name and student_id and str_score and gender and submit_time):
            None_error+=1
            empty=1
        else: empty=0
        if empty==0:
            if not(student_id.startswith("2026") and len(student_id) == 10):
                illegal_error+=1
            elif (int(result["score"])>100):
                illegal_error+=1
            elif not ("15:00"<=str(submit_time)<="16:30"):
                illegal_error+=1
    return {"None_error":None_error,"illegal_error":illegal_error}
wrong_list=validate_record(new_list,)
print(wrong_list)
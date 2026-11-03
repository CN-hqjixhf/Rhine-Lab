scores=[58,76,92,60,45,88,100,67,60,83]
print(f"人数：{len(scores)},总分:{sum(scores)}")
print(f"平均分：{sum(scores)/len(scores):.2f}")
new_scores=sorted(scores)
print(f"最小值为：{new_scores[0]},最大值为：{new_scores[-1]}")
good=0
yes=0
nogood=0
for i in scores:
    if i>=90:
        print(f"{i}：优秀")
        good+=1
    elif i<90 and i>=60:
        print(f"{i}：及格但未优秀")
        yes+=1
    else:
        print(f"{i}：不及格，{scores.index(i)}")
        nogood+=1
print(f"优秀人数：{good},及格但未优秀人数：{yes},不及格人数：{nogood}")
def summarize_scores(score,pass_line):
    yes2=0
    for score in scores:
        if score>=pass_line:
            yes2+=1
    return yes2
if scores ==[] :
    print("ValueError")
yes3=summarize_scores(scores,60)
yes4=summarize_scores(scores,70)
dict1={}
dict1["人数:"]=len(scores)
dict1["平均分:"]=sum(scores)/len(scores)
dict1["pass_line=60时及格人数:"]=yes3
dict1["pass_line=60时及格率:"]=yes3/len(scores)
print(dict1)
dict2={}
dict2["人数:"]=len(scores)
dict2["平均分:"]=sum(scores)/len(scores)
dict2["pass_line=70时及格人数:"]=yes4
dict2["pass_line=70时及格率:"]=yes4/len(scores)
print(dict2)
def solution(numbers, hand):
    answer = ''
    left_data = ["1", "4", "7"]
    right_data = ["3", "6", "9"]
    both_data = ["2", "5", "8", "0"] 
    dic={"L":"*","R":"#",
        "2":{
            '0':3,'1': 1, '2':0 ,'3':1,'4':2,'5':1,'6':2,'7':3,'8':2,'9':3,'*':4,'#':4  
            },
        "5":{
            '0':2,'1': 2,'2':1,'3':2,'4':1,'5':0,'6':1,'7':2,'8':1,'9':2,'*':3,'#':3 
            },
        "8":{
            '0':1,'1': 3,'2':2,'3':3,'4':2,'5':1,'6':2,'7':1,'8':0,'9':1,'*':2,'#':2 
            },
        "0":{
            '0':0,'1': 4,'2':3,'3':4,'4':3,'5':2,'6':3,'7':2,'8':1,'9':2,'*':1,'#':1
            }
    }
    for data in numbers:
        data = str(data)
        if data in left_data:

            answer+= "L"
            dic["L"] = data
        
        elif data in right_data:
            print("right")
            answer+= "R"
            dic["R"] = data
        
        elif data in both_data:
            print("L_data: ",dic["L"],"L_dis: " ,dic[data][dic["L"]],"R_data: ",dic["R"], "R_dis: ",dic[data][dic["R"]])
            #누를 번호의 거리와 왼쪽, 오른쪽 손가락의 거리 비교
            if dic[data][dic["L"]] < dic[data][dic["R"]]:
                answer+="L"
                dic["L"] = data

            elif dic[data][dic["L"]] > dic[data][dic["R"]]:
                answer+="R"
                dic["R"] = data

            else:
                print("same")
                if hand == "right":
                    answer+="R"
                    dic["R"] = data
                else:
                    answer+="L"
                    dic["L"] = data
                
    return answer

numbers =[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
#LRLLRRLLLRR
print(solution(numbers, hand))
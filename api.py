import requests, json
from pprint import pprint
a= requests.get("http://saral.navgurukul.org/api/courses").text
b=json.loads(a)
print(b)
d, c, data_list = 1, b["availableCourses"], []
for i in c:
    print(((str(d)+" => "+i["name"])))
    d+=1
    data_list.append(i["id"])
user=int(input(" PLEASE SELECT UR ID,,,,"))
e=data_list[user-1]
f=requests.get('http://saral.navgurukul.org/api/courses/' + str(e) + '/exercises').text
pprint(f)
g=json.loads(f)
# pprint(g)
h=open("saral.json","w")
json.dump(g,h,indent=4)
h.close()
c, slug_lst= 1, []
for i in g["data"]:
    for j in i:
        if j=="childExercises":
            h=1
            for k in i["childExercises"]:
                print("     "+str(c-1)+"."+str(h)+"  "+k["slug"])
                h+=1
    print(str(c)+"  "+i["slug"])
    c+=1
user_input2=input("please select your course")

        
 





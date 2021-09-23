# import json
# user = json.loads('{"__type__": "User", "name": "John Smith", "username": "jsmith"}')
# print(user['name'])
# print(user['username'])
# import json
# json_data = ('{"name":"satyam","class":"chudai","age":"17"}')


# print(json.loads(json_data))

# ###################################         QUESTION:-2        ##################################

# import json
# user={
#          "name": "David",
#      "class":"I",
#      "age": 6  
#  }
# f=open("s.json","w")
# json.dump(user,f,indent=4)
# f.close()
# f=open("s.json","r")
# print(f.read())

# ###############################          QUESTION:-3          ###################################
# import json
# user={"Name":"Ram","Class":"IV","Age":9}
# a=json.dumps(user)
# print(type(a))

#############################            QUESTION:-4           ###################################
# import json
# b=({
    
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4
# })
# a=json.dumps(b,sort_keys=True)
# if type(a)==complex:
#     print("yes")
# else:
#     print("no")
##############################           QUESTION:-5        #####################################

# import json
# b={
    
#     '4': 5, 
#     '6': 7, 
#     '1': 3,
#     '2': 4+2j
# }
# a=json.load(b,sort_keys=True)
# print(type(a))


##########################               QUESTION:-6       #####################################

# import json
# b=('{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}')
# a=json.loads(b)
# print(a)

############################       QUESTION:-7            #####################################


# myfile = open("text.txt", 'r')
# data_dict = {}
# for line in myfile:
#     k, v = line.strip().split('=')
#     data_dict[k.strip()] = v.strip()

# myfile.close()

# print(' text file to dictionary =\n ',data_dict)


##########################       QUESTION:-8              ########################################
# emp_det = open("emp_data.txt", "r").read()
# emp_det = list(emp_det.split())     # emp name post salary and  
# print(emp_det)
# emp_serial_no = []                 #   ['emp1', 'emp2', 'emp3', 'emp4']
# emp_details = ['name', 'designation', 'age', 'salary']
# for i in emp_det:                   #   ['emp1', 'emp2', 'emp3', 'emp4']
#     emp_serial_no.append('emp' + str(emp_det.index(i) + 1))

# for i in emp_det:
#     i = list(i)
#     print(type (i))
# for i, j in zip(emp_serial_no, emp_det):
#     # for j in emp_det:
#     print(type(i), type(j))
# # for i, k in zip(emp_serial_no,emp_details):
# #     print(i,k)
# import json
# a=[["suraj","HR",21,22000],["Pawan","manager",22,20000],["ashok","fm",19,10000]]
# b=["NAME","DESIG","AGE","SALARY"]
# c=["emp1","emp2","emp3"]
# dic0={}
# index_c=0
# for de in a:
#     in_dic=zip(b , de)
#     dic0[c[index_c]]=dict(in_dic)
#     index_c+=1
# print(dic0)
# f=open("satyam.json","w")
# f.write(str(dic0))

# f.close()



# f=open("emp_data.txt","r")
# # a=[["neelam","programer","24","2400"],
# # ["komal","trainer","24","20000"],
# # ["anuradha","HR","25","40000"],
# # ["Abhishek","manager","29","63000"]]
# b=["NAME","DESIG","AGE","SALARY"]
# c=["emp1","emp2","emp3","emp4"]
# dic0={}
# index_c=0
# for de in f:
#     in_dic=zip(b , de)
#     dic0[c[index_c]]=dict(in_dic)
#     index_c+=1
# print(dict(dic0))
############################            question :- 9        ###########################


# {
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }



###############################################################################################


























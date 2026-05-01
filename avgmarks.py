names=["ramesh","rajesh","suresh","mahesh","paramesh"]
marks=[[20,30,40],[40,50,60],[30,50,60],[70,50,30],[68,97,55]]
for i in range(5):
  a=sum(marks[i])//3
  print("{}.{} has scored{}".format(i+1,names[i],a))
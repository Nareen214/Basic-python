Name=["Nareen","ranji","hemanth","ansh","nikhil"]
Marks=[50,60,68,20,39]
p=1
for i in range(5):
    if Marks[i]>45:
        print("{}. {} has scored {}%". format(p, Name[i], Marks[i]))
        p=p+1
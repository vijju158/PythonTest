print("While Loop")
count=0
while(count<5):
    print(count)
    count+=1
print("Good Bye")

print("For Loop")
count=1
for i in range(10):
    print(str(i)*i)

    for j in range(0,i):
        count+=1

print("---------Loop Control--------------")
for i in range(10,50):
    print(i)
    if(i==30):
        break

for j in range(1,11):
    print(j)
    if(j==5):
        continue
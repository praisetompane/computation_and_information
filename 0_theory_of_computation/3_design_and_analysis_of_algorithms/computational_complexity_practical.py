from datetime import datetime

print("what n² loks like for 10000 input size")

print(f"starting computation: {datetime.now()}")
n = 10001
for i in range(0, n):
    for j in range(0, n):
        print(i*j)
print(f"computation completed: {datetime.now()}")

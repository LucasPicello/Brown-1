print("Input a value ")
V = int(input())
print("what unit is the value(H\M)")
A1 = input()
if A1 == "H":
    V2 = V * 60
    print(V, " hours is ", V2, " minutes")
if A1 =="M":
    V2 = V/60
    print(V, " minutes is ", V2, " hours")

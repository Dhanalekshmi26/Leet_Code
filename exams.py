T = int(input())
for _ in range(T):
    X,Y,Z = map(int,input().split())
    total_students_attended = X*Y
    pass_percentage = (Z/total_students_attended)*100
    if pass_percentage > 50:
        print("Yes")
    else:
        print("No")

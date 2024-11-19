v1 = [1,2,3]
v2 = [1,-1,0];

def dot(v1,v2):
    v = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    return v
print("The Vector is: ",dot(v1,v2))
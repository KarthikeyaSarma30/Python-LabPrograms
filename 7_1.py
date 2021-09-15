def fun(x1,y1,r1,x2,y2,r2):
    distance=((x2-x1)**2+(y2-y1)**2)**0.5
    if distance<=r1+r2:
        print("balls will collide")
    else:
        print("balls will not collide")
fun(2,3,4,5,6,7)

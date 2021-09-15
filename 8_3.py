def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)
def lcm(a,b):
    lcm_=(a*b)/hcf(a,b)
    return lcm_
print(hcf(6,8))
print(lcm(6,8))

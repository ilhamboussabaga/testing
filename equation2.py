from cmath import sqrt
def equation1(a,b,c):
    delta=(b*b)-(4*a*c)
    d=sqrt(delta)
    if delta<0 :
        return "pas de solution"
    elif delta==0 :
        return -b/(2*a)
    elif delta>0 :
        s1=(-b-d)/(2*a)
        s2=(-b+d)/(2*a)
        return s1,s2



import numbers

def maximumEdgeofTriangle(a,b):
    if(a<0 or b<0):
        return 'Sides of Triangle cannot be negative'
    if(isinstance(a, numbers.Integral) and isinstance(b, numbers.Integral)):
        return (a+b)-1
    return "Sides of Triangle cannot be float or double numbers"


print(maximumEdgeofTriangle(5,-6))

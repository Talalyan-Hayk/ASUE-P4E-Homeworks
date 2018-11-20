def func( x ): 
    return 0.05 * x * x * x * x + 0.1 * x * x * x + 0.5 * x * x +10 * x + 5
  
def derivFunc_1( x ): 
    return 0.2 * x * x * x + 0.3 * x * x + x + 10

def derivFunc_2( x ):
    return 0.6 * x * x + 0.6 * x + 1

def newton( x ):  
    h = derivFunc_1(x) / derivFunc_2(x)
    iteration = 0 
    while abs(h) >= 0.0001: 
        h = derivFunc_1(x)/derivFunc_2(x)  
        x = x - h
        iteration += 1 
        print("Estimated value of x_min after iteration " + str(iteration) + " : " + str(x)) 
    print ("x_min = " + str(x))
    print ("y_min = " + str(func(x)))  


x0 = -20  
newton(x0) 

  
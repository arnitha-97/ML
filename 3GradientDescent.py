import numpy as np 

def gradient_descent(x,y):
    m_curr=b_curr=0
    iterations=10000
    learning_rate=0.08  #we choose by trail and error
    n=len(x)

    for i in range(iterations):
        der_m=(-2/n)*sum(x*(y-(m_curr*x + b_curr)))
        der_b=(-2/n)*sum(1*(y-(m_curr*x + b_curr)))
        cost=(1/n)*sum([val**2 for val in (y-(m_curr*x+b_curr))])
        m_curr=m_curr-learning_rate*der_m
        b_curr=b_curr-learning_rate*der_b
        print(f'{m_curr} {b_curr} {cost} {i}')   #remember the cost should decrease 

    
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

gradient_descent(x,y)
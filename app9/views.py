from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def isPrime(request):
    n1 = request.GET.get('n1')
    n = int(n1)
    flag1 = False
    status = ""
    if n > 1:
        for i in range(2, n):
            if(n % i) == 0:
                flag1 = True
                break
    if flag1:
        status1="this is not a prime number"
    else:
        status1 = "This is a prime number"
    return Response(status1)  

@api_view(['GET'])
def isArmstrong(request):
    num = request.GET.get('num')
    status=""
    num1 = int(num)
    sum = 0
    t = num1
    while t > 0:
        digit = t % 10
        sum += digit ** 3
        t //= 10
        
         
    if num1 == sum:
        status ="This is an armstrong number"
    else:
        status = "This is  not an armstrong number"
    return Response(status)                        
                
        
            
   
            
        
    

            
    
    

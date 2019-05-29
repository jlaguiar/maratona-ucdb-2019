def primo(n):
    if(n<5 or n%2==0 or n%3==0):
        if(n==2 or n==3):
            return "eh primo"
        else:
            return "nao eh primo"
    
    maxP = int(n**0.5)+2
    p = 5
    while (p<maxP):
        if(n%p==0 or n%(p+2)==0):
            return "nao eh primo"
            
        p+=6
        
    return "eh primo"
  
x = int(input())
for i in range(x):
    value = int(input())
    print(value, primo(value))
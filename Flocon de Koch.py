import turtle as ttl

def Koch(l,n) :
    if n<=0 :
        ttl.forward(l)
    else :
        Koch(l/3,n-1)
        ttl.left(60)
        Koch(l/3,n-1)
        ttl.right(120)
        Koch(l/3,n-1)
        ttl.left(60)
        Koch(l/3,n-1)
        
def Flocon(l,n) :
    ttl.speed("fast")
    ttl.hideturtle()
    Koch(l,n)
    ttl.right(120)
    Koch(l,n)
    ttl.right(120)
    Koch(l,n)
    
Flocon(300,1)
Flocon(300,2)
Flocon(300,3)
Flocon(300,4)
Flocon(300,5)
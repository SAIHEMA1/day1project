While True:
        except
        x=int(input('please enter a number:'))
        try valueerror:
                print('not a valaid number,try again...')







#def unique_list(l):
 #       for a in l:
 #           if a not in x
  #              x=[]
   #             x.append(a)
    #            return x
#print(unique_list([1,2,3,3,3,34,5]))
        








   # CALENDAR #

#import calendar
#yy=int(input("enter a year"))
#mm=int(input("ënter a month"))
#print(calendar.month(yy,mm))

     # OR #

#import calendar
#yy=2020
#mm=5
#print(calendar.month(yy,mm))


        # RECURSIVE FUNCTION #


#def factorial(n):
#    if n==1:
#        return n
 #   else:
  #      return(n*factorial(n-1))
#n=int(input("enter a number"))
 #     print(factorial(n))




#n=int(input("enter a number"))
#fact=1
#for i in range(1,n+1):
 #   fact=fact*i
#print(fact)

         # OR  #

#def factorial(n):
 #   fact=1
  #  for i in range(1,n+1):
   #     fact=fact*i
    #return(fact)
#n=int(input("enter a number"))
#print(factorial(n))





# TUPLES :(index),(count),(del),(min,max)

#a=(2,4,6,8,1,9)
#for i in a:
#    print(i)



#a=["Banana","grapes","pineapple"]
#m=len(a[0])
#for i in a:
 #   if len(i)>m:
  #      m=len(i)
#print(m)




#a=[]
#print(a)
#for i in range(5):
 #   b=int(input("enter a number"))
 #   a.append(b)
#print(a)
#for i in a:
 #   c=0
  #  for j in range(1,i+1):
   #     i%j==0
    #    c+=1
    #if c==2:
     #   print(i,"prime")



#a=[]
#print(a)
#for i in range(5):
 #   b=int(input("enter a number"))
  #  a.append(b)
#m=int(input("enter a element to.serch"))
#c=0
#for i in a:
#    i==m
 #   c+=1
#print(m,"occured",c,"times")
    


#a=[]
#print(a)
#for i in range(5):
 #   b=int(input("enter list of elements"))
   # a.append(b)
  #  print(a)
    
            

#x=int(input())
#y=int(input())
#x = x%y
#x = x%y
#y = y%x
#print(y)


#x=1
#y=2
#z=x
#x=y
#y=z
#print(x,y)



#a=[1,3,4,6,9]
#m=a[0]
#for i in a:
 #  if m<i:
  #     m=i
#print("maximum",m)
        

#a=[1,3,4,6,9]
#m=a[0]
#for i in a:
 #  if m>i:
  #     m=i
#print("minimum",m)



#a=[1,3,4,6,9]
#c=0
#for i in a:
 #   c+=1
  #  print(c)


#a=[1,3,4,6,9]
#b=int(input("ënter a number"))
#for i in a:
 #   print(i,"*",b,"=",i*b)




#a=[1,3,4,6,9]
#for i in a:
 #   print(i)


#a=[4,5,3,2,8]
#for i in range(len(a)):
 #   print("index:",i,"value:",a[i])



#a=[2,4,6,3,7,9]
#for i in range(0,len(a)):
   #print("index:",i,"value:",a[i])
   


#a=[2,4,6,3,7,9]s
#for i in range(0,6):
 #   print("index:",i,"value:",a[i])



#n=1234
#r=0
#res=0
#n>0
#while True:
 #   r=n%10
  #  n=n//10
   # res=res*10+5



#import math
#math.sin(45)


#LOCAL AND GLOBAL 

#a=10
#def sample(a):
 #   global b
  #  b=11
   # print("inside",b)
#sample(a) 
#print("outside",a)



#a=10
#print(a)
#def sample():
 #   a=12
  #  a+=1print(a)
   # print(a)
#sample()
#print(a)



#FUNCTIONS:

#print("1 for addition","2 for substration","3 for multiplication","4 for division")
#n=int(input("enter a number for calculation"))
#a=int(input("enter a number"))
#b=int(input("enter b number"))
#def calculation(a,b):
    #if n==1:
     #   print(a+b)
    #if n==2:
     #   print(a-b)
    #if n==3:
   #     print(a*b)
  #  if n==4:
 #       print(a/b)
#print(calculation(a,b))




#n=int(input("enter a number for calculation"))
#a=int(input("enter a number"))
#b=int(input("enter b number"))
#def add(a,b):
 #   return(a+b)
#def sub(a,b):
 #   return(a-b)
#def div(a,b):
 #   return(a/b)
#def mul(a,b):
 #   return(a*b)
#if n==1:
 #   print(add(a,b))
#if n==2:
 #   print(sub(a,b))
#if n==3:
 #   print(div(a,b))
#if n==4:
 #   print(mul(a,b))

      # OR #

#a=int(input("enter a number"))
#b=int(input("enter b number"))
#def add(a,b):
 #   return(a+b)
#def sub(a,b):
 #   return(a-b)
#def div(a,b):
 #   return(a/b)
#def mul(a,b):
 #   return(a*b)
#print(add(a,b))
#print(sub(a,b))
#print(div(a,b))
#print(mul(a,b))



#n=int(input("enter a number"))
#def prime():
 #   c=0
  #  for i in range(1,n+1):
   #     if n%i==0:
    #        c+=1
     #       if c==2:
      #          print("prime")
       #     else:
        #        print("not prime")

#prime()




#def div():
 #   a=10
  #  b=20
   # print(a%b)
#div()


#a=int(input("enter a number"))
#b=int(input("enter b number"))
#def add():
 # print(a+b)
#add()



#a=[2,5,3,7,8,77]
#m=a[0]
#for i in a:
 #   if m<i:
  #      m=i
#print("maximum",m)and minimum(m>i)




#a=[1,4,6,3,2]
#b=int(input("enter a number"))
#for i in a:
 #   print(i,"*",b,"=",i*b)



#a=[2,3,4,5]
#for i in range(0,4):
   # print(a[i])
 #  print("index:",i,"value:",a[i])


#a=[2,6,8,4,1]
#for i in range(len(a)):
 #   print(i,a[i])


#a=[2,6,7,3,9]
#cnt=0
#for i in a:
 #   cnt+=1
  #  print(cnt)




#n=int(input("enter a number"))
#a=len(str(n))
#cnt=0
#x=0
#for i in range(1,n+1):
  #  if n%i==0:
 #       cnt+=1
#if cnt==2:
 #   print(n,"prime")
#while n!=0:
 #   c=0
  #  rem=n%10
   # for i in range(1,rem+1):
    #    if rem%i==0:
     #       c+=1
    #if c==2:
     #   print(rem,"prime")
      #  x+=1
       # n=n//10
        #if x==a:
         #   print("mega prime as well")
        #else:
         #   print("not a mega prime")
#else:
 #   print("not a prime")
        


#n=int(input("enter a number"))
#while n!=0:
 #   c=0
  #  rem=n%10
   # for i in range(1,rem+1):
    #    if rem%i==0:
     #       c+=1
  #  if c==2:
 #       print(rem)
#    n=n//10
          




#s=int(input("enter starting point"))
#e=int(input("enter ending point"))
#for j in range(s,e+1):
# cnt=0
 #for i in range(1,j+1):
  #  if j%i==0:
   #  cnt+=1
 #if cnt==2:
  #  print(j,"prime")
    




#for i in range(0,5):
 #   print(i)


#i=0
#while i<=5:
 #   print(i)
  #  i+=1



#n=int(input("enter a number"))
#cnt=0
#for i in range(1,n+1):
 #   if n%i==0:
  #      cnt+=1
#if cnt==2:
 #   print("prime")
#else:
 #   print("not prime")




#n=int(input("enter a number"))
#res=0
#while True:
 #   rem=n%3
  #  n=n//10
   # res=res*10+rem
#if n==0:
 #   print(res)



#imid="saihema@gmail.com"
#ipwd="098765"
#for i in range(5):
 #   mid=input("enter mail id")
  #  pwd=input("enter password")
   # if imid==mid and ipwd==pwd:
    #    print("succesfully")
    #else:
     #   print("incorrect pas or mail id")



#n=int(input("enter a number"))
#res=0
#while True:
 #   r=n%3
  #  n=n//10
   # res=res*10+r
    #print(res)
    #if n==0:
     #   break



#a=[1,6,3,7,9,4]
#m=a[0]
#for i in a:
#    if m<i:
#        m=i
#print("max",m)






#a=[1,2,3,4,5]
#b=int(input("enter the element"))
#for i in a:
 #   print(i,"*",b,"=",i*b)









#a=[1,3,5,7,8]
#cnt=0
#for i in a:
    #cnt+=1
    #print(cnt)
    #print("index:",i,"value:",a)










#a=[1,3,5,6,7,8]
#b=int(input("enter a number"))
#for i in a:
 #print(i,"*",b,"=",i*b)




#n=int(input("enter a number"))
#res=0
#while n!=0:
 #rem=n%10
 #n=n//10
 #res=res*10+rem
 #print(res)
     


 #a=[4,6,7,8,9]
#for i in a:
   # print("maximum:",a)





#imid="saihema141999@gmail.com"
#ipwd="9542890066"
#mid=input("enter maid id")
#pwd=input("enter password")
# if imid==mid and ipwd==pwd:
 #   print("login succesfull")
  #else:
   #
#print("logout for 24 hours")




#n=int(input("enter a number"))
#res=0
#while True:
 #r=n%3
 #n=n//10
 #res=res*10+r
 #print(res)
 #if n==0:
     #break
     

from random import randrange
gw=[]
with open("/usr/share/dict/words")as f:
    for ii in f:
        ii=ii.strip()
        if ii.isalpha():
            gw.append(ii)


random_index=randrange(0,len(gw))
wfg= gw[random_index]
wfg=wfg.lower()
char=''
os=""
i=1
z=0
wfgl=list(wfg)
l=len(wfgl)
tl=[]
cl=[]
s="*"*l
slst=list(s)
print s.center(50)
print("Lengthe : {}".format(l))
while i < 4 :
    cl=[]
    char=raw_input(" Guess My Letters  : ")
    if char not in tl:
        tl.append(char)
    else:
        print (" {} Already Typed ".format(char))
        i=i-1
    for k in range(l):
        if wfgl[k]==char:
             z=1
             cl.append(k)
             slst[k]=char
             os="".join(slst)
           
            
    if z==1:        
       print(" WOW it contain  {} times".format(len(cl)))
       print os
       if os==wfg:
           print("YES I am {}\nYou Found me With {} Wrong attempts \n\n C O N G R A T U L A T I O N ".format(wfg,i-1))
           break
    else:
         print ("HEY... You are in W R O N G  ")
         rc=3-i
         i=i+1
         print (" you have only {} chances".format(rc))
    z=0
if os!=wfg:
    print ("  I am {}  \n\n  TRY AGAIN  ".format(wfg))
    


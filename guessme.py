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
print ("\033[1;31m")
print s.center(50)
print("Lengthe : {}".format(l))
print("\033[1;32m")
while i < 4 :
    cl=[]
    char=raw_input("\033[1;32m Guess My Letters  :\033[1;m ")
    if char not in tl:
        tl.append(char)
    else:
        print ("\033[1;30m {} Already Typed \033[m".format(char))
        i=i-1
    for k in range(l):
        if wfgl[k]==char:
             z=1
             cl.append(k)
             slst[k]=char
             os="".join(slst)
           
            
    if z==1:        
       print("\033[1;35m WOW it contain  {} times\033[m".format(len(cl)))
       print("\033[1;31m")
       print os
       print("\033[m")
       if os==wfg:
           print("\033[2;42mYES I am {}\nYou Found me With {} Wrong attempts \n\n C O N G R A T U L A T I O N \033[2;m".format(wfg,i-1))
           break
    else:
         print ("\033[1;34mHEY... You are in W R O N G \033[m ")
         rc=3-i
         i=i+1
         print ("\033[1;47m you have only {} chances\033[m".format(rc))
    z=0
if os!=wfg:
    print ("\033[1;43m  I am {}  \n\n  TRY AGAIN  \033[1;m".format(wfg))
    


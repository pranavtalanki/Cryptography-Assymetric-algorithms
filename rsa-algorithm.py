def getNum(text):
    k=0
    for i in range(len(text)):
        numbers[i]=ord(text[k])%65
        k+=1
    print("number format of plain text : ",numbers)

def rsa(text,e,n):
    getNum(text)
    for i in range(len(text)):
        cipherNum[i]=pow(numbers[i],e,n)
        print(numbers[i],"^",e,"mod",n,"=",cipherNum[i])
    print("cipher text : ",cipherNum)

def rsadec(text,d,n):
    for i in range(len(text)):
        plainNum[i]=pow(cipherNum[i],d,n)
        print(cipherNum[i],"^",d,"mod",n,"=",plainNum[i])
    print("plain text number : ",plainNum)
        
def decmod(e,n):
    for d in range(1000):
        k=pow(e*d,1,n)
        print(e,"*",d,"mod",n,"=",k)
        if(k==1):
            break
    return d

p=int(input("Enter p : "))
q=int(input("Enter q : "))
e=int(input("Enter e : "))
plaintext=input("enter plaintext : ")
l=len(plaintext)
numbers=[0 for i in range(l)]
cipherNum=[0 for i in range(l)]
n=p*q
print("encryption : ")
print("-------------")
rsa(plaintext,e,n)
print("Decryption : ")
print("-------------")
print("n = p*q = ",p,"*",q,"=",n)
phi=(p-1)*(q-1)
print("phi = (p-1)(q-1) = (",p,"-1)(",q,"-1)=",phi)
print("e = ",e)
d=decmod(e,phi)
print("d = ",d)
plainNum=[0 for i in range(l)]
rsadec(plaintext,d,n)
plaintext=[]
for i in range(l):
    plaintext.append(chr(plainNum[i] + 65))
print("ciphertext : ","".join(plaintext))
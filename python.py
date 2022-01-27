#lex_auth_01269445968039936095

def validate_credit_card_number(card_number):
    #start writing your code here
    a=str(card_number)
    if len(a)==16:
        sum2=0
        sum1=0
        for i in range(len(a)):
            if i%2==0:
                b=int(a[i])
                c=2*b
                if c>9:
                    sum=0
                    while(c>0):
                        sum+=c%10
                        c=c//10
                else:
                    sum=c
                sum1=sum1+sum
            else:
                sum2=sum2+int(a[i])
        if (sum1+sum2)%10==0:
            return True
        else:
            return False
    else:
        return False

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")

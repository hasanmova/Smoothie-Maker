d={}
d['Classic']=["strawberry","banana","pineapple","mango","peach","honey","ice","yogurt"]
d['Forest Berry']=["strawberry","raspberry","blueberry","honey","ice","yogurt"]
d['Freezie']=["blackberry","blueberry", "black currant", "grape juice","frozen yogurt"]
d['Greenie']=["green apple","kiwi","lime","avocado","spinach","ice","apple juice"]
d['Vegan Delite']=["strawberry", "passion fruit", "pineapple", "mango","peach","ice","soy milk"]
d['Just Desserts']=["banana","ice cream","chocolate","peanut","cherry"]
def plus_minus(a,o):
    if '-' == o[0]:
        a.remove(o.lstrip("-"));
    elif '+' == o[0]:
        a.append(o.lstrip("+"));
    return a
def loop(a,f):
    a.pop(0)
    if len(a)==0 :
       return ','.join(f)
    else:
       for x in a:
           x=plus_minus(f , x)
       return ','.join(x)
str=input('').split(',')
print(loop(str,d[str[0]] ))
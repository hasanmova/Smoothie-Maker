
# Online Python - IDE, Editor, Compiler, Interpreter

Classic = ["strawberry","banana","pineapple","mango","peach","honey","ice","yogurt"]
Forest_Berry = ["strawberry", "raspberry", "blueberry", "honey", "ice", "yogurt"]
Freezie = ["blackberry", "blueberry", "black currant", "grape juice", "frozen yogurt"]
Greenie = ["green apple", "kiwi", "lime", "avocado", "spinach", "ice"," apple juice"]
Vegan_Delite = ["strawberry", "passion fruit", "pineapple", "mango", "peach", "ice", "soy milk"]
Just_Desserts = ["banana", "ice cream", "chocolate", "peanut", "cherry"]

def plus_minus(array,operator):
    if '-' in operator:
        item = operator.replace("-", "")
        array.remove(item);
        return array
    elif '+' in operator:
        item = operator.replace("+", "")
        array.append(item);
        return array
    
def loop(array , fur ):
    if len(array) == 0 : 
       return fur
    else:    
       for x in array:
           x = plus_minus(fur , x)
       return ','.join(x)  
    
    
str = input('')
str = str.split(',')

if str[0] == 'Classic':
    str.pop(0)
    print(loop(str , Classic))
    
elif str[0] == 'Forest Berry':
    str.pop(0)
    print(loop(str , Forest_Berry))
elif str[0] == 'Freezie':
    str.pop(0)
    print(loop(str , Freezie))
elif str[0] == 'Greenie':
    str.pop(0)
    print(loop(str , Greenie))
elif str[0] == 'Vegan Delite':
    str.pop(0)
    print(loop(str , Vegan_Delite))
elif str[0] == 'Just Desserts':
    str.pop(0)
    print(loop(str , Just_Desserts))

#namearray = str[0] 
#exec("%s = %d" % (namearray,2))


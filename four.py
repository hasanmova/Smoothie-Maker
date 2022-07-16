my_data = {}
my_data['Classic'] = ["strawberry","banana","pineapple","mango","peach","honey","ice","yogurt"]
my_data['Forest Berry'] = ["strawberry","raspberry","blueberry","honey","ice","yogurt"]
my_data['Freezie'] = ["blackberry","blueberry", "black currant", "grape juice","frozen yogurt"]
my_data['Greenie'] = ["green apple","kiwi","lime","avocado","spinach","ice","apple juice"]
my_data['Vegan Delite'] = ["strawberry", "passion fruit", "pineapple", "mango","peach","ice","soy milk"]
my_data['Just Desserts'] = ["banana","ice cream","chocolate","peanut","cherry"]

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
    array.pop(0)
    if len(array) == 0 :
       return ','.join(fur)
    else:
       for x in array:
           x = plus_minus(fur , x)
       return ','.join(x)

str = input('')
str = str.split(',')
print(loop(str, my_data[str[0]] ))




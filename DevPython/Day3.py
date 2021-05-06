names=["john", "jake", "jack", "george", "jenny", "jason"]
dict={"name": "python", "ext": "py", "creator": "guido"}
print("Printing names :")
for name in names:

    if len(name)<5 and 'e' not in name:
        print(name)
        
        
        
        
print("Printing dictionary values")
for k,v in dict.items():   
    print(f'{k} : {v}')



fizzbuzz=int(input("Enter any integer to check FizzBuzz: "))
if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print("fizzbuzz")
elif fizzbuzz % 3 == 0:
    print("fizz")
elif fizzbuzz % 5 == 0:
    print("buzz")
print(fizzbuzz)
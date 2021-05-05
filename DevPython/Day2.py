firstName = input("Enter your First name : ")
lastName = input("Enter your Last name : ")

print(firstName.capitalize(),lastName.capitalize())


numList=input("Enter List of numbers :")

numList = [int(num) for num in numList.split(" ")]

print("Minimum :" , min(numList))
print("sum :" , sum(numList))
print("UniqueValies :" , list(set(numList)))
numList.sort()
print("Ascending :" ,numList )
numList.sort(reverse=True)
print("Descending :" , numList)

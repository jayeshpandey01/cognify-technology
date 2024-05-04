def kelvin(temp):
    print("The temperature in Kelvin is: ", temp + 273.15)
    
def faranite(temp):
    print("The temperature in feranite is: ", (temp * 9/5) + 32)


print('Welcome to the temperature converter')

temp = float(input("Enter temperature: "))
flag = True
while flag:
    print('convert in a) celcius to Kelvin b) celcius to feranite')
    choice = input('Enter Your choice: ')
    if choice == 1:
        kelvin(temp)
    elif choice == 2:
        faranite(temp)

    else:
        print('Invalid choice')

    print('Do you want to continue?')
    choice = input('Enter Y for yes and N for no: ')
    if choice == 'Y':
        flag = True
    elif choice == 'N':
        flag = False
    else:
        print('Invalid choice')
'''
Interactively convert temperatures between Celsius, Fahrenheit, and Kelvin with user-selected scales.

Ask which scale the user is converting from (C/F/K).
Ask which scale to convert to (cannot match the from-scale).
Prompt for the numeric temperature and apply the appropriate conversion formula.
Output both the original and converted values with units.
Examples

Input: from=C, to=F, value=100
Output: "100° Celsius is 212° Fahrenheit."
Demonstrates the boiling-point conversion.

'''

def celsius():
    while True:
        to_scale = input('Scale to convert to (F/K): ').strip().upper()

        num_convert = float(input('Enter Celsius to convert: '))

        if to_scale == 'F':
            cel_fa = int((num_convert*1.8) + 32)
            print(f'\n{num_convert}° Celsius is {cel_fa}° Fahrenheit.\n')
            break
        
        if to_scale == 'K':
            cel_ke = int((num_convert + 273.15))
            print(f'\n{num_convert}° Celsius is {cel_ke}° Kelvin\n')
            break

        else:
            print('\nPlease convert to Fahrenheit or Kelvin ')
    

def fahrenheit():
    while True:
        to_scale = input('Scale to convert to (C/K): ').strip().upper()

        num_convert = float(input('Enter Fahrenheit to convert: '))

        if to_scale == 'C':
            fa_cel = int((num_convert-32)*5/9)
            print(f'\n{num_convert}° Fahrenheit is {fa_cel}° Celsius.\n')
            break

        if to_scale == 'K':
            fa_ke = int((num_convert + 459.67)*5/9)
            print(f'\n{num_convert}° Fahrenheit is {fa_ke}° Kelvin.\n')
            break

        else:
            print('\nPlease convert to Fahrenheit or Kelvin ')
        
def kelvin():
    while True:
        to_scale = input('Scale to convert to (C/F): ').strip().upper()

        num_convert = float(input('Enter Kelvin to convert: '))

        if to_scale == 'C':
            ke_cel = int(num_convert-273.15)
            print(f'\n{num_convert}° Kelvin is {ke_cel}° Celsius.\n')
            break

        if to_scale == 'F':
            ke_fa = int((num_convert-273.15)*9/5 +32)
            print(f'\n{num_convert}° Kelvin is {ke_fa}° Fahrenheit.\n')
            break

        else:
                print('\nPlease convert to Fahrenheit or Kelvin ')

while True:
    from_scale = input('Temperature scale coverting from (C/F/K): ').strip().upper()

    if from_scale == 'C':
        celsius()
    
    if from_scale == 'F':
        fahrenheit()
    
    if from_scale == 'K':
        kelvin()

    else:
        print('Please type C, F, or K')
    
    

    

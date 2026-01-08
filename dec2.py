'''
---------------- BMI Calculator -------------------

Ask for weight (kg) and height (m), compute BMI, and print the category (Underweight/Normal/Overweight/Obese); validate numeric input.

Prompt for weight (kg) and height (m); validate as positive numbers.
Compute BMI = weight / (height^2); round sensibly for display.
Determine category using standard BMI ranges and print result.
Re-prompt on invalid input (non-numeric, zero/negative).
Examples

Input: weight = 70, height = 1.75
Output: "BMI: 22.86 → Category: Normal"
Correct formula and category mapping.

'''
while True:
    user_weight = float(input('Weight in kilograms: '))
    user_height = float(input('Height in meters: '))
    calc_bmi = float(user_weight/user_height**2)
    print(calc_bmi)

    def category():
        if 0 >= calc_bmi <= 18.5:
            print('Underweight')
        
        elif 18.5 >= calc_bmi <= 24.9:
            print('Normal')
        
        elif 25 >= calc_bmi <= 29.9:
            print('Overweight')

        elif 30 >= calc_bmi:
            print('Obese')
        
        else:
            print('none')

    category()
    user_bmi = print(f'BMI: {calc_bmi} -> Category: {category()}')



    


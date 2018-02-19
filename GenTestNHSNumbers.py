# Generate Test NHS Numbers #
# Developer : Michael Cross #

import itertools
    
# Perform basic validation on user input #
    
while True: 
    try:
        seed = int(input("Please enter the seed value for generated NHS Numbers (i.e. 9000000000) : "))

    except:
        print('Error: Seed value must be a 10 digit integer')
        continue
            
    if len(str(seed)) != 10:
        print('Error: Seed value must be a 10 digit integer  and cannot start with 0')
        continue     
    else:
        break 

quantity = int(input("Please enter the number of observations that will be generated : "))
    
# Begin generation of concurrent 10 digit integers from Seed value #
    
valid_NHS_numbers = []

for i in itertools.count():
    total = 0
    str_NHS_number = str(seed+i)
    
# Begin Mod11 validation to ensure value is valid NHS Number. If not chuck the result #
    
    for f in range (0,9):
        new_num = int(str_NHS_number[f])
        total = total + new_num*(11-(f+1))

    remainder = total % 11
    checkdigit = 11-remainder
    if checkdigit == 11:
        checkdigit = 0

    if int(str_NHS_number[8:]) == 10:
        validation_status = 'Invalid'
    elif checkdigit == 10:
        validation_status = 'Invalid'
    
    if checkdigit != int(str_NHS_number[9]):
        validation_status = 'Invalid'  
    else:
        validation_status = 'Valid'
    
    if validation_status == 'Valid':
        valid_NHS_numbers.append(str_NHS_number)
                   
    if len(valid_NHS_numbers) == quantity: 
        break
        
# Return list of valid NHS Numbers #  

print()
for elem in valid_NHS_numbers:
    print(elem)
print()
print (str(quantity) + ' Test NHS Numbers were successfully generated.')  
print()
input('Press ENTER to exit')

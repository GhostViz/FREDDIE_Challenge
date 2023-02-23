import re

cards = int(input())

for card in range(cards):
        
    card_number = input().strip()
    card_number_sans_hyphen = card_number.replace('-','')
    
    valid = True
    
    check_length_sans_hyphens = bool(re.match(r'^[4-6]\d{15}$',card_number))
    check_length_with_hyphens = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',card_number))  
    check_redundancy = bool(re.findall(r'(?=(\d)\1\1\1)',card_number_sans_hyphen))
    
    if check_length_sans_hyphens == True or check_length_with_hyphens == True:
        if check_redundancy == True:
            valid=False
    else:
        valid = False       
    if valid == True:
        print('Valid')
    else:
        print('Invalid')
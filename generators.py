import random


def generate_fake_phone_number():
    # Country code
    country_code = "234"
    
    # List of area codes
    area_codes = ["90", "80", "70", "81"]
    
    # Randomly select an area code
    area_code = random.choice(area_codes)
    
    # Randomly decide whether to include parentheses
    use_parentheses = random.choice([True, False])
    
    # Randomly decide whether to include a '+'
    use_plus = random.choice([True, False])
    
    # Randomly decide whether to put space or not
    use_space = random.choice([True, False])
    
    # Generate the rest of the phone number
    rest_of_number = "".join([str(random.randint(0, 9)) for _ in range(8)])
    
    # Construct the phone number based on the random choices
    if use_plus:
        phone_number = f"+{country_code}"
    else:
        phone_number = f"{country_code}"
        
    if use_space:
        phone_number += " "
    
    if use_parentheses:
        phone_number += f"({area_code})"
    else:
        phone_number += f"{area_code}"
        
    if use_space:
        phone_number += " "
    
    phone_number += f"{rest_of_number[:3]}" 
    if use_space:
        phone_number += " "
        
    phone_number += f"{rest_of_number[3:5]}" 
    
    if use_space:
        phone_number += " "
        
    phone_number += f"{rest_of_number[5:]}"

    return phone_number

def generate_fake_email(male_names, female_names, surnames, first_name=None, surname=None):
    # List of popular email domain names in Nigeria
    nigeria_domains = ["yahoo.com", "gmail.com", "hotmail.com", "ncc.gov.ng", "telecom.net.et", "intercellula.nc.com"]
    
    if not first_name:
        # Randomly select a gender and corresponding name list
        gender = random.choice(["male", "female"])
        if gender == "male":
            first_name = random.choice(male_names)
        else:
            first_name = random.choice(female_names)

    if not surname:
        # Randomly select a surname
        surname = random.choice(surnames)
        surname = random.choice([surname[0], surname])

    # Generate a random number
    random_number = ''.join([str(random.randint(0, 9)) for _ in range(random.randint(0, 3))])

    # Randomly choose between '.' and '_'
    separator = random.choice([".", "_", ""])

    # Randomly choose an email domain
    domain = random.choice(nigeria_domains)

    # Construct the fake email address
    fake_email_1 = f"{first_name.lower()}{separator}{surname.lower()}{random_number}@{domain}"
    fake_email_2 = f"{first_name.lower()}{separator}{surname.lower()}{separator}{random_number}@{domain}"
    fake_email_3 = f"{surname.lower()}{separator}{first_name.lower()}{separator}{random_number}@{domain}"
    fake_email_4 = f"{surname.lower()}{separator}{first_name.lower()}{random_number}@{domain}"
    
    fake_email = random.choice([fake_email_1, fake_email_2, fake_email_3, fake_email_4])
    
    fake_email = fake_email.replace("'", "")

    return fake_email

def generate_fake_national_id():
    # Generate 11 random digits
    national_id = ''.join([str(random.randint(0, 9)) for _ in range(11)])

    return national_id

def generate_fake_creditcard_number():
    # Generate 16 random digits
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(16)])

    # Randomly decide whether to include spaces after every 4th digit
    use_spaces = random.choice([True, False])

    # Construct the fake credit card number based on random choices
    if use_spaces:
        fake_creditcard_number = ' '.join([random_digits[i:i+4] for i in range(0, 16, 4)])
    else:
        fake_creditcard_number = random_digits

    return fake_creditcard_number

def generate_fake_passport_number():
    # Generate a random letter
    random_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # Generate 8 random digits
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(8)])

    # Randomly decide whether to include spaces
    use_spaces = random.choice([True, False])

    # Construct the fake passport number based on random choices
    if use_spaces:
        fake_passport_number = f"{random_letter} {random_digits[:3]} {random_digits[3:]}"
    else:
        fake_passport_number = f"{random_letter}{random_digits}"

    return fake_passport_number

def generate_fake_drivers_license_id():
    # Generate three random uppercase letters
    random_letters1 = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3))

    # Generate 5 random digits
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(5)])

    # Generate two random uppercase letters
    random_letters2 = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(2))

    # Generate 2 random digits
    random_digits2 = ''.join([str(random.randint(0, 9)) for _ in range(2)])

    # Construct the fake driver's license ID
    fake_drivers_license_id = f"{random_letters1}{random_digits}{random_letters2}{random_digits2}"

    return fake_drivers_license_id
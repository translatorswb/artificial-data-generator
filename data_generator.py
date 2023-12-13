import argparse
import re
from generators import *

LABEL_PATTERN = re.compile(r'\[([A-Z]+)\]')

def search_for_names(sentence, male_names, female_names, surnames):
    found_person = False
    first_name = None
    surname = None

    # Combine all names for searching
    all_names = male_names + female_names + surnames

    # Iterate through all names to check for matches
    for name in all_names:
        if name.lower() in sentence.lower():
            found_person = True

            # Identify whether the found name is a first name or surname
            if name in male_names or name in female_names:
                first_name = name
            else:
                surname = name

    return found_person, first_name, surname

def generate_fake_value(placeholder, male_names, female_names, surnames, placenames, first_name=None, surname=None):
    if placeholder == "[EMAIL]":
        return generate_fake_email(male_names, female_names, surnames, first_name, surname)
    elif placeholder == "[ID]":
        return generate_fake_national_id()
    elif placeholder == "[PHONE]":
        return generate_fake_phone_number()
    elif placeholder == "[DRIVER]":
        return generate_fake_drivers_license_id()
    elif placeholder == "[PASS]":
        return generate_fake_passport_number()
    elif placeholder == "[CC]":
        return generate_fake_creditcard_number()
    else:
        print("Unknown placeholder", placeholder)
        return placeholder  # Return the original placeholder if not recognized


def replace_placeholders(sentence, male_names, female_names, surnames, placenames):
    placeholders = ["[EMAIL]", "[ID]", "[PHONE]", "[DRIVER]", "[PASS]", "[CC]"]

    for placeholder in placeholders:
        while placeholder in sentence:
            if placeholder == "[EMAIL]":
                #Search if a name is mentioned
                found_person, first_name, surname = search_for_names(sentence, male_names, female_names, surnames)
                fake_value = generate_fake_value(placeholder, male_names, female_names, surnames, placenames, first_name, surname)
            else:
                fake_value = generate_fake_value(placeholder, male_names, female_names, surnames, placenames)
            sentence = sentence.replace(placeholder, fake_value, 1)

    return sentence

def process_data(source_data_file, modified_data_file, names_file, surnames_file, placenames_file):
    print(f"Processing data from {source_data_file}...")
    
    #read artificial labels
    male_names = []
    female_names = []
    with open(names_file, 'r') as file:
        for line in file:
            name, gender = line.strip().split()
            if gender == 'Male':
                male_names.append(name)
            elif gender == 'Female':
                female_names.append(name)
            else:
                print("Unknown gender", gender)
                
    surnames = [l.strip() for l in open(surnames_file, 'r')]
    placenames = [l.strip() for l in open(placenames_file, 'r')]

    #Remove duplicates
    male_names = list(set(male_names))
    female_names = list(set(female_names))
    surnames = list(set(surnames))
    placenames = list(set(placenames))

    with open(source_data_file, 'r') as file, open(modified_data_file, 'w') as fout:
        for line in file:
            line = line.strip()
            matches = LABEL_PATTERN.findall(line)
            if matches:
    #             print(line)
    #             print(replace_placeholders(line))
    #             print()
                modified = replace_placeholders(line, male_names, female_names, surnames, placenames)
                fout.write(modified + '\n')
            else:
                fout.write(line + '\n')

    print("Data processing completed.")

def main():
    parser = argparse.ArgumentParser(description="Process data files.")
    parser.add_argument('-source', '-s', help='Source data file', required=True)
    parser.add_argument('-output', '-o', help='Modified data file', required=True)
    parser.add_argument('-names', '-n', help='Names file', required=True)
    parser.add_argument('-surnames', '-r', help='Surnames file', required=True)
    parser.add_argument('-places', '-p', help='Placenames file', required=True)

    args = parser.parse_args()

    # Call the function to process the data with the provided parameters
    process_data(args.source, args.output, args.names, args.surnames, args.places)

if __name__ == "__main__":
    main()

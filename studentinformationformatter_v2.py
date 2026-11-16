# Student Information Formatter - Version 2

first_name = input(" Enter first name:  ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

# Format student information
full_name = (first_name + " " + last_name).strip().title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = favorite_subject.title()

# Display formatted output
print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Favorite Subject:", formatted_subject)
print("Character count:", len(full_name))
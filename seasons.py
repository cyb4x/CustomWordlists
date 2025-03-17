#Author: cyb4x
#Date: 15 March 2025

seasons = ['Winter', 'Spring', 'Summer', 'Fall']
years = range(2019, 2028)
special_chars = ['!', '@', '#', '^', '%', '&']

password_list = []

for season in seasons:
    for year in years:
        for char in special_chars:
            password_list.append(f"{season}{year}{char}")
            password_list.append(f"{season.lower()}{year}{char}")
            password_list.append(f"{season}{char}")
            password_list.append(f"{season.lower()}{char}")
            password_list.append(f"{season}{year}")
            password_list.append(f"{season.lower()}{year}")

output_path = "pnpt/wordlists/custom-wordlists/seasons_passwords.txt"
with open(output_path, "w") as f:
    for password in password_list:
        f.write(password + "\n")

print(f"Password list has been saved to '{output_path}'")

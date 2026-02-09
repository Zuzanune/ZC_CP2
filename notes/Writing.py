"""with open("notes//names.txt", "a") as file:
    file.write("Zane\n")
    file.write("Kingsley\n")
    file.write("Levi\n")
    file.write("Alex\n")
    file.write("Lucas\n")
    file.write("Alexander")"""
"""with open("notes//names.txt", 'r+') as file:
    content = []
    for line in file:
        content.append(line.strip())
    
    index = content.index('Alex')
    content[index] = "aleex"
    file.truncate(0)
    for i in content:
        file.write(i + "\n")
print (content)"""

import csv
with open("notes/test.csv", 'w', newline = '') as csvfile:
    fieldnames = ['username', 'favorite_color']
    writer = csv.writer(csvfile)

    writer.writerow(fieldnames)
    writer.writerow(["cosmic_voyager", "indigo"])
    writer.writerow(["tech_wizard", "turquoise"])
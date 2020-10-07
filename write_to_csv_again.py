from os import path

# write to file

line_list = [
    # ["ID", "NAME", "PRICE", "DESCRIPTION", "PHOTO_URL"],
    ["1003", "Meat Lovers", "39.99", "All the meats!!!", "http://www.example.com/photos/img_1001.png"],
    ["1004", "Veggie Delight", "39.99", "All the veg!!!", "http://www.example.com/photos/img_1002.png"],
]

if path.exists("csv_output.csv"):
    file = open("csv_output.csv", "a")
else:
    file = open("csv_output.csv", "w")

for line in line_list:
    file.write( f"{ ','.join(line) }\n" )



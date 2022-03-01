contacts = {
    "Ruxy": 456,
    "Matei": 123
}
# print(contacts)

employee_info = {
    "Name": "Andrei",
    "Last_Name": "Diaconu",
    "Job": "Salesperson",
    "Age": 19,
    "Favorite Color": "green"
}
# print(employee_info)

animal_names = dict(cat="Sebastian", dog="Togo")
# print(animal_names)

# print(employee_info["Name"])
# print(employee_info["Last_Name"])
employee_info["Job"] = "Web Developer"
employee_info["Hobbies"] = "Playing video games", "Reading"
# print(employee_info)

if "Favorite Color" in employee_info:
    print(employee_info["Favorite Color"])

print(employee_info.get("Favorite Color"))

employee_info_1 = {
    "Name": "Will",
    "Last Name": "Oldman",
    "Address": "New York, USA",
    "Job": {"Salesperson", "Developer"},
    "Age": 34,
    "Hobbies": ("Reading", "Wacthing Movies", "Walking"),
    1992: "Date of Birth",
    "Married": True,
    "Favorite Songs": ["Un Dia", "Blinding Lights", "Shallow"],
    "Best Friend": {"Name": "Gerald"},
    "Special One": None
}

employee_info_1.clear()
print(employee_info_1)

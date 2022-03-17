# Dictionaires allow data to be stored in key value pairs, when you want to access it you can use the key

# Jan is the key, January is the value. 
# Keys need to be unique, they can be numbers or strings

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    }

# Can obtain the info by referring to the key
print(month_conversions["Jan"])
print(month_conversions["Feb"])

# Can also use the get functiont to obtain a value from the dictionary
print(month_conversions.get("Mar"))
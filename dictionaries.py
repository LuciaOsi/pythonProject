# Dictionaries --> store info in key (uniques), value pairs
month_dictionary = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Pct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_dictionary["Dec"])
# Get can have a default if the key is not found
print(month_dictionary.get("Lu", "Not a valid key"))

# programming_dictionary = {
#     "one" : 1,
#     "two" : 2,
#     "three" : 3,
# }

# print(programming_dictionary)

# programming_dictionary["four"] = 4

# print(programming_dictionary)

# empty_dictionary = {}

# programming_dictionary = {}

# print(programming_dictionary)

#looping in dictionary

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#NESTING

capitals ={
    "France": "Paris",
    "Germany":"Berlin",
}

#NESTING DICTIONARY IN DICTIONARY AND LIST IN DICTIONARY
travel_log = {
    "France": {"cities_visted": ["Paris","Lille","Dijon"], "total_visits": 5},
    "Germany": {"cities_visited": ["Berlin","Hamburg","Stuttgart"], "total_visits": 6}
}

#NESTING DICTIONARY IN LIST

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visit": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin","Hamburg","Stuttgart"],
        "total_visits": 5,
    },
]
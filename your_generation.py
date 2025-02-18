born_year = int(input("please enter your birth year : ")) 

if 1927 < born_year <= 1946:
    generation = "silent generation"
elif 1945 < born_year <= 1965:
    generation = "baby boomer"
elif 1964 < born_year <= 1981:
    generation = "generation x"
elif 1980 < born_year <= 1997:
    generation = "millenials" 
elif 1996 < born_year <= 2013:
    generation = "generation z"
elif born_year > 2012:
    generation = "generation alpha"
else:
    generation = "you are not alive"

print(f"You belong to the {generation}.") 

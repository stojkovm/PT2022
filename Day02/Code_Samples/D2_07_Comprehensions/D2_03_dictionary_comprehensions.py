"""
 - A dict comprehension is a short-hand for a 'for' loop.
"""
def to_square_foot(area):
    return area * 1.07e+7


country_areas = {
    "united states": 9.834e+6,
    "switzerland": 41_285,
    "serbia": 88_499,
}

"""
 - The following example can be replaced with dict comprehension.
"""
my_dict = {}
for country, area in country_areas.items():
    if len(country) > 7:
        continue
    my_dict[country.title()] = to_square_foot(area)
print(my_dict)


"""
 - In one line! (unformatted :))
"""
my_dict = {
    country.title(): to_square_foot(area)
    for country, area in country_areas.items()
    if len(country) > 7
}
print(my_dict)

"""
 - Example why generators are good.
 - Preprocessing can take time and block other operations to work in 'parallel'.
 - Generators can yield data and forward it further for processing without waiting
    that preprocessing operation completely finishes first.
"""

# preprocessing
def parse_file(filename):
    with open(filename, 'r') as f:
        #lst = []
        for line in f:
            first_name, last_name = line.strip().split(" ")
            #lst.append((first_name, last_name))
            yield (first_name, last_name)
    # return lst


# actual analysis
for name in parse_file('full_names.txt'):
    print(f"{name[0]},{name[1]}")

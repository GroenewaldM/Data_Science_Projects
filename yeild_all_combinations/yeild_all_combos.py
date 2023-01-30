
def get_units(cow, cow_dict):
    return cow_dict[cow]

def max_val(to_consider, avail, cow_dict):
    if to_consider == [] or avail == 0:
        result = (0,())
    elif get_units(to_consider[0], cow_dict) > avail:
        result = max_val(to_consider[1:], avail, cow_dict)
    else:
        next_item = to_consider[0]
        with_val, with_to_take = max_val(to_consider[1:], avail - get_units(next_item, cow_dict), cow_dict)
        with_val += get_units(next_item, cow_dict)
        without_val, without_to_take = max_val(to_consider[1:], avail, cow_dict)
        if with_val > without_val:
            result = (with_val, with_to_take+(next_item,))
        else:
            result = (without_val, without_to_take)
    
    return result
def main(cow_dict, avail):
    to_consider = []
    transport = []
    for cow in cow_dict:
        to_consider.append(cow)
    
    while len(to_consider) != 0:
        trip = max_val(to_consider, avail, cow_dict)[1]
        transport.append(list(trip[:]))
        for cow in trip:
            to_consider.remove(cow)
    return transport

    
all_cows = {'Horns': 50, 'Muscles': 65, 'Milkshake': 75, 'Lotus': 10, 'Louis': 45, 'Miss Bella': 15, 'Polaris': 20, 'MooMoo': 85, 'Patches': 60, 'Clover': 5}
print(main(all_cows, 100))  
print(main({'Betsy': 39, 'Rose': 42, 'Willow': 59, 'Buttercup': 11, 'Coco': 59, 'Luna': 41, 'Abby': 28, 'Starlight': 54}, 120))    
        
    
    
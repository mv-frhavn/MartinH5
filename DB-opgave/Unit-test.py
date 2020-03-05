import Location

# Create Location, Test if its there, remove it again

location_id = 9999
position = 9999
unittest = Location.Location(location_id, position).new_item()
# test if the method new_item succeeds
assert unittest is True, 'unit test 1 failed'

locations = Location.Location(location_id, position).extract_store()
test_result = 0
for location in locations:
    if location[0] == location_id and location[1] == position:
        test_result += 1
assert test_result > 0, 'The create location method failed'

unittest = Location.Location(location_id, position).rem_item()

import Location

# Create an new location with the Location method, and use it for testing

location_id = 9999
position = 9999
unittest = Location.Location(location_id, position).new_item()
# First unittest checks the method Location.Location().new_item() if it returns true
# If it returns true, the method works and the location is true
assert unittest is True, 'unit test 1 failed'

# Uses the extract_store to pull the Location table from the DB
locations = Location.Location(location_id, position).extract_store()
test_result = 0
# The loop then goes through the list to see if it can find the test location that was created earlier
# If the Location is found in the DB, the unittest passes
for location in locations:
    if location[0] == location_id and location[1] == position:
        test_result += 1
assert test_result > 0, 'The create location method failed'

unittest = Location.Location(location_id, position).rem_item()

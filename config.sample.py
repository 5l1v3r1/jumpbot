# systems we don't want fuzzy matching to hit on in fleetping triggers
fuzzy_match_denylist = ['gate', 'serpentis', 'semi', 'time', 'promise', 'vale']

# when fuzzy matching chats to system names, ignore these chars
punctuation_to_strip = '[.,;:!\'"]'

# strings to trigger the output of a detailed path. important that none of these collide with systems!
path_terms = ['path', 'detail', 'full', 'hops']

# strings to trigger the output of a detailed path. important that none of these collide with systems!
safe_terms = ['safe', 'safer', 'lowsec', 'hisec']

# strings to trigger a search for the closest non-null system
non_null_terms = ['escape', 'evac', 'evacuate']

# strings to trigger a search for the closest ITC
itc_terms = ['itc', 'trade', 'market']

# strings to trigger the display of either closest station or hops with stations
station_terms = ['station', 'stations']

discord_token = ""
discord_ids = ['123123123123123123', '234234234234234234', '@jumpbot']
popular_systems = ['Jita', 'Alikara', 'Okagaiken']
trigger_roles = [('123123123123123123', 'testfleetping'), ('234234234234234234', 'otherfleetping')]
debug_logging = False

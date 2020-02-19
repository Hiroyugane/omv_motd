# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet

# ALL COMBINE: colorize for normal values
# all values in motd should be in colorized-section, with if-clause if config for that is present, if not -> default color
# pretty default but can be optimized with switchcases or oneline-ifs
if load['1min'] < 0.4: load['color'] = 'green'
elif load['1min'] < 0.8: load['color'] = 'yellow'
else: load['color'] = 'red'

if home['ratio'] < 0.4: home['color'] = 'green'
elif home['ratio'] < 0.8: home['color'] = 'yellow'
else: home['color'] = 'red'
    
if memory['ratio'] < 0.4: memory['color'] = 'green'
elif memory['ratio'] < 0.8: memory['color'] = 'yellow'
else: memory['color'] = 'red'

if swap['ratio'] < 0.4: swap['color'] = 'green'
elif swap['ratio'] < 0.8: swap['color'] = 'yellow'
else: swap['color'] = 'red'
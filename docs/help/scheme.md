# Naming-Schemes

## Variables

Module-internal variables: Object-oriented *camelCase*
Return-variables: Object-oriented *module_camelCase*
Main-/Baselib-Variables: *CAMELCASE*

Temp-/processingvariables: <precending-variable>_processingtype (f.e. recentLogins_split)

## Functions

Module-functions: Object-oriented *snake_case*
Main-functions: UPPERCASE_SNAKE_CASE

## temp-variables

"Loop"-indexer (+ ints for nested loops): n, m, l, o, p,
other indexers: i, j, k,

# Data Schemes

Raw data values are always in a dict. the dict consists of the value itself with its value-name-key and the ruleset to be applied to the value when it's colored by its value, the threshold. It's called by the value-key with an appended "-rs". 

Values are given to the main script with their raw value and their ruleset for interpreting the file. It might be that module developers wish to hand them the already-formatted value, but it still depends on the main process to decide what to finally do with the files (f.e. to implement other features later on, like design-overhauls (lightmode-designs etc.) or other color palettes for thresholds). The main process hands the value and the ruleset with (not yet implemented) optional flags to the threshold-processor, which colors the values in the desired color and hands them back to the main process for inserting them in the design and, later on, calculating the fluid design 
 
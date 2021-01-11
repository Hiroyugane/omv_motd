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
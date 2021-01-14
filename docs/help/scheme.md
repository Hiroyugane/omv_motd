# Naming-Schemes

## Packages
PEP8-compliant short, all-lowercase, no underscore

## Modules
PEP8-Compliant: short, all-lowercase
In addition: scrape-modules that belong to a bigger group of scrapers should be prefixed with the group-abbreviation and an underscore (example: hw_cpu.py)
The following abbreviations exist as of right now:
- hw (hardware)
- os (operating system)
- net (network) 
- custom (any custom modules for thirdparty-software)
- ext (extensions by third parties and addon-developers)

## Variables

Module-Variables: all-lowercase
Main-/Baselib-Variables: *CAMELCASE*

Temp-/processingvariables: <precending-variable>_processingtype (f.e. recentLogins_split)

## Functions

Module-functions: Object-oriented *snake_case*
Main-functions: UPPERCASE_SNAKE_CASE

## temp-variables

"Loop"-indexer (+ ints for nested loops): n, m, o, p,
other indexers: i, j, k,

# Data Schemes

Raw data values are always in a dict. the dict consists of the value itself with its value-name-key and the ruleset to be applied to the value when it's colored by its value, the threshold. It's called by the value-key with an appended "-rs". 

Values are given to the main script with their raw value and their ruleset for interpreting the file. It might be that module developers wish to hand them the already-formatted value, but it still depends on the main process to decide what to finally do with the files (f.e. to implement other features later on, like design-overhauls (lightmode-designs etc.) or other color palettes for thresholds). The main process hands the value and the ruleset with (not yet implemented) optional flags to the threshold-processor, which colors the values in the desired color and hands them back to the main process for inserting them in the design and, later on, calculating the fluid design 
 
For more information:
https://www.python.org/dev/peps/pep-0008/
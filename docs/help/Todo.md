# Order of refining-jobs

>since the preset code of the fork is in a bad shape, we have to clean it up a little

1. **Trying to understand the code and the purpose of the functions**
    - quite annoying since some variables and definitions are very cryptic
2. **comment the code and put in explanations // creating provisory documentations**
    - to understand the essential parts and what the definitions and variables are there for, a documentation of that is needed so we have a list of blackboxes and pipelines
3. **restructure blackboxes and resizing**
    - in some blackboxes code could/should be outsourced in another blackbox and some might have to be merged. Also organize blackboxes in a linear "based on each other"-manner inside the file
4. **polish up code**
    - redo the cryptic parts of codes (f.e. rename variables) and make the blackboxes cleaner inside
        - variable conventions have to be created (call all output keys XYZ, every value has a strict format etc) and should be documented for easier understanding and modularity
        I'd like object-oriented variable names (memory_free_key/memory_free_value_raw)
    - also (where it makes sense ofc) outsource variables into a "config"-section at the top of the file
    - everything like placeholders and other printouts should also be configurable. The complete design should be up to you, to the point where you'll just have a design.cfg-file which contains something along the lines of: "frame-left: '#', frame-right: '||' inner-border: (etc), content: {CPU.load}, {RAM.free}, {network}" (more refining on that idea when getting to that point)
5. **OS-Customization**
    - since the code was written for mandriva originally, the code doesn't really fit for f.e. debian-based distros. Mandriva-special parts should be put into their own thing, closed off behind an "only if mandriva"-clause, same goes to ubuntu-specific code and for other distros (modular for Distros)
6. **modularize and outsource**
    - since motd.d is designed to be made out of separate files for each section, this should be the case for motp, too.
    - Theoretical plan is:
        - have one global motp-file which will contain fluid-columns, colorization, etc. and which will server as an import-library for everything else. Global might print the logo or any other header you'd wish, that's up to choose when working on that step.
        - everything else (host-section, network-section etc.) will have its own file in which values are going to be gathered and calculated. *important for compatibility* (since even not calling it would throw an error, it'd have to either commented out or sth. but just removing the modular file is the easiest option for end-users)
        - configs and setups will be in a config-file (location: don't know if putting in motd.d will spit out errors) which will have common-parameters aswell as the user-defined layout (see 4.)
7. last polishing and writing documentations
    - to explain users how they can work on the project by themselves or for people who wanna fork this, them should be given plenty of resources to better let them understand the code and maybe the possibilities also. For complex variables like arrays some kind of graphical demonstration helps probably.
8. finishing
    - put the final 1.0.0 release onto the master branch and update the readme and other types of documentation, aswell as setup tutorial. license-type maybe? etc.

> To be continued and filled with more info as we go along



## Notes 
Add rulesets for formatting stuff (ruleset: cpu_error)
Add config for fallback-returnvalues (cpu_load: 9.99)
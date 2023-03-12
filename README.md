# websitemenucreator

Currently it sort of works as it is.

To do:
1. When clicking "Add Menu Option" - the webpage is ugly as shit.
2. When generating with ONE menu option and ONE variable like $target - Everything works GREAT!
3. When generating with NO variables at all, just normal commands like whoami (or even ls "/bin/") - Everything works GREAT!
4. When generating with TWO menu options and the SECOND menu option has the variable - Everything works GREAT!
5. When running with TWO different variables it does this (Wrong indentation, can't fix it ffs)

```
def set_websitevariable1():
            global websitevariable1
            websitevariable1 = input('Enter a new websitevariable1:')
            input('Press enter to return to menu...')
        
        
def set_websitevariable():
            global websitevariable
            websitevariable = input('Enter a new websitevariable:')
            input('Press enter to return to menu...')
```
6. Finally - the last problem/thing - The first menu option variable doesn't get updated to {website} from $website in this output:
But menu options 2+ do
```
```
def ping():
    print('You selected ping')
    echo = f"ping $websitevariable1"
    try:
        os.system(echo)
    except KeyboardInterrupt:
        print('echo interrupted by user')
    input('Press enter to return to menu...')
```





Example.py is included in this repository for understanding how the script should look in comparison.
The options used to generate example.py are as follows:


Variables all work.
Variables will automatically be identified if you use $ 
2. $target
1. $site

Whatever you want really.


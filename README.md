# websitemenucreator

Currently it sort of works as it is.

To do:
1. Make it check for if the user specified variables ($string) like $target in their command.
2. Strip menu options names for symbols and spaces to use as def menu_name()
3. Make sure if you have commands using quotes that we escape those correctly when parsing it into variable for os.system.
4. Look for identical menu options and alert the person they can't have identical menu names.


Example.py is included in this repository for understanding how the script should look in comparison.
The options used to generate example.py are as follows:


## Title: Scanner Script!
## 2 menu options
1. nmap -sV -sC $target
2. ping $target2


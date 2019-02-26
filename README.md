Project Name : SHA1 Hash Program in Python 2.7
This project is to illustrate SHA1 hashes using Brute Force manner in Python 2.7. 

Prerquisites: 
Python 2.7 installed, along with PyCharm editor (optional). 

Installation: 

Below steps are required to install Python 2.7.15 :

a. From https://www.python.org/downloads/release/python-2715/ download appropriate Python 2.7.15 Windows Installer. 
b. Run the file
c. Select install for all users or install just for me, click Next
d. You'll see it installs under the C:\Python27 folder, click Next
e. Click Next again for the 'Customize Python' step
f. Click Finish
g. Open Control Panel, then System
h. Click 'Advanced system settings' on the left
i. Click the 'Environment Variables' button
j. Under 'System variables' click the variable called 'Path' then the 'Edit...' button. (This will set it for all users, you could instead choose to edit the User variables to just set python as a command prompt command for the current user)
k. Without deleting any other text, add C:\Python27; (include the semi-colon) to the beginning of the 'Variable value' and click OK.
l. Click OK on the 'Environment Variables' window.
m. Open a new command prompt window type python, you will have python running in the command prompt. 

Note: command prompt windows open prior to setting the Environment Variable will not have the python command available. 

Details about Project Files: 

There are two python files attached in this assignment
a. SHA1PythonAlgorithm.py : 
		This python script is to be used for solving problems a, b and c.
		The User will be prompted for 2 inputs, Hash Value (mandatory) and Salt Hash (optional)
		Based on the values entered by the user, the program will produce the appropriate clear text password for the hash function, time taken for execution, and number of tries to find a match. 
		I have used SHA1 Function, which will take a SHA1 hash, and compare it to SHA1 hashes of the top 10000000 worst known user passwords (provided by Professor)
		If no match is found, it displays the message that No Match Found. 
b. SHA1PythonAlgorithmCombination.py
		This python script is to be used for solving only problem d
		The user will be prompted to enter Hash Value
		Based on the value entered, I have designed a nested for loop to concat two terms with space and find the hash function for it, which will then be compared with user inputted Hash value. 
Note: The SHA1PythonAlgorithmCombination.py uses nested for loops, so the performance is not optimized for 10 million input file. Please allow it to run for an hour or so to return the value. 

Example Input/Output from Python command line : 
Ex: 1) SHA1PythonAlgorithm Script output for Problem a)testing program hash 

Please enter the hash value.
>b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Please enter the salt value of hash (leave empty if not required).
>
Selected Regular/Medium Hash as User Input
The password is letmein
Number of tries before Found a Match : 15
Total Elapsed time to run program for Successful Match : 4.37900018692

Ex: 2) SHA1PythonAlgorithm Script output for Problem a)medium hacker hash 

Please enter the hash value.
>801cdea58224c921c21fd2b183ff28ffa910ce31
Please enter the salt value of hash (leave empty if not required).
>
Selected Regular/Medium Hash as User Input
The password is vjhtrhsvdctcegth
Number of tries before Found a Match : 999967
Total Elapsed time to run program for Successful Match : 8.61000013351

Ex: 3) SHA1PythonAlgorithm Script output for Problem a)Leet hacker hash

Please enter the hash value.
>ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
Please enter the salt value of hash (leave empty if not required).
>f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
Selected Leet Hacker Hash with an associated Salt hash
The salt key is slayer
The password is harib
Number of tries before Found a Match for Leet Hacker Hash : 1546153
Total Elapsed time to run program for Successful Leet Hacker Hash Match : 5.13000011444

Ex: 4) SHA1PythonAlgorithm Script output for Non existing SHA1 Hash

Please enter the hash value.
>ansfanksfmopamfajnjansfjnfj
Please enter the salt value of hash (leave empty if not required).
>
Selected Regular/Medium Hash as User Input
Reached the end of file with No Match found after 1000000 tries
Total Elapsed time to run program for Unsuccessful Match : 4.16499996185
 
Ex: 5) Best case scenario for SHA1PythonAlgorithmCombination script output: 

Please enter the hash value.
>791bde021b8ac0b31f7e9b7236e6be4809f67cf0
Combinations of Passwords scanned until now : 123456 123456
Combinations of Passwords scanned until now : 123456 password
The password is 123456 password		


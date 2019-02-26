import hashlib, urllib, time
UserSHA1input = raw_input("Please enter the hash value.\n>")
UserSaltInput = str(raw_input("Please enter the salt value of hash (leave empty if not required).\n>") or "No")
cnt=0
start=time.time()
PasswordsInput = urllib.urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt").read()
saltkey=''
combinationkey=''
if UserSaltInput != 'No':
    print "Selected Leet Hacker Hash with an associated Salt hash"
    for saltpasstry in PasswordsInput.split('\n'):
        SaltPasswordSHA1 = hashlib.sha1(saltpasstry).hexdigest()
        if SaltPasswordSHA1 == UserSaltInput:
            saltkey=saltpasstry
            print "The salt key is " + str(saltpasstry)
        elif SaltPasswordSHA1 != UserSaltInput:
            cnt=cnt+1
elif UserSaltInput == 'No':
    print "Selected Regular/Medium Hash as User Input"

if UserSaltInput == 'No':

    for passtry in PasswordsInput.split('\n'):
        PasswordSHA1 = hashlib.sha1(passtry).hexdigest()
        if PasswordSHA1 == UserSHA1input:
            print "The password is " + str(passtry)
            print "Number of tries before Found a Match : " + str(cnt)
            TimeForMatchFound = str(time.time() - start)
            print "Total Elapsed time to run program for Successful Match : " + (TimeForMatchFound)
            quit()
        elif PasswordSHA1 != UserSHA1input:
                 cnt = cnt + 1
    print "Reached the end of file with No Match found after " + str(cnt) + " tries"
    TimeForNoMatchFound = str(time.time() - start)
    print "Total Elapsed time to run program for Unsuccessful Match : " + (TimeForNoMatchFound)
    quit()

elif UserSaltInput != 'No':

    for saltpasstryin in PasswordsInput.split('\n'):
        SaltPasswordSHA2 = hashlib.sha1(saltkey + saltpasstryin).hexdigest()
        if SaltPasswordSHA2 == UserSHA1input:
            print "The password is " + str(saltpasstryin)
            print "Number of tries before Found a Match for Leet Hacker Hash : " + str(cnt)
            TimeForMatchFound = str(time.time() - start)
            print "Total Elapsed time to run program for Successful Leet Hacker Hash Match : " + (TimeForMatchFound)
            quit()
        elif SaltPasswordSHA2 != UserSHA1input:
            cnt = cnt + 1
    print "Reached the end of file with No Match found after " + str(cnt) + " tries"
    TimeForNoMatchFound = str(time.time() - start)
    print "Total Elapsed time to run program for Unsuccessful Salt Key find : " + (TimeForNoMatchFound)
    quit()

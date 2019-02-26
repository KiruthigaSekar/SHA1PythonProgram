import hashlib, urllib, time
UserSHA1input = raw_input("Please enter the hash value.\n>")
cnt = 0
start = time.time()
PasswordsInput = urllib.urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt").read()
for passtry in PasswordsInput.split('\n'):
    for passtryin in PasswordsInput.split('\n'):
        PasswordSHA1 = hashlib.sha1(passtry+" "+passtryin).hexdigest()
        print "Combinations of Passwords scanned until now : " + str(passtry+" "+passtryin)
        if PasswordSHA1 == UserSHA1input:
            print "The password is " + str(passtry+" "+passtryin)
            quit()
        elif PasswordSHA1 != UserSHA1input:
            cnt = cnt + 1
print "Reached the end of file with No Match found after " + str(cnt) + " tries"
TimeForNoMatchFound = str(time.time() - start)
print "Total Elapsed time to run program for Unsuccessful Match : " + (TimeForNoMatchFound)

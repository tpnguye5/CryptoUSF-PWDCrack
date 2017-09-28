#Program should operate on one or more lines from shadow password files
#For validation of operation of your program, a single line of the shadow file will be provided
#with a three character password to crack


#test program and see how many passwords are tried per second

from passlib import hash
import time

def test(cryptpass):
    salt = cryptpass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        # cryptWord = crypt.crypt(word.salt)
        cryptWord = hash.des_crypt.encrypt(word,salt=salt)
        if (cryptWord == cryptpass):
            print('[+] FOUND PASSWORD: '+ word + '\n')
            return
    print('[-] PASSWORD NOT FOUND. \n')
    return

def main():
    passFile = open('password.txt')
    for line in passFile.readlines():
        # a = datetime.datetime.now().replace(microsecond=0)
        a=time.time()
        if ':' in line:
            user = line.split(':')[0]
            cryptpass = line.split(':')[1].strip(' ')
            print('[*] Cracking Password for: ' + user)
            test(cryptpass)
        # b=datetime.datetime.now().replace(microsecond=0)
        b = time.time()
        result = b-a
        # print("Time took:", result)
        numPassWD= result/60
        print("#of passwords tried: %f", numPassWD)

if __name__=="__main__":
    main()



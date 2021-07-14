import os.path
# this variable stores the folder you'll save the textfiles with the emails
g_path = r'C:/example/example'

def at_encryption(text):

    '''
    this function takes a text and returns it
    encrypted in atbash cypher
    '''

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rev_alphabet = alphabet[::-1]

    number_line = "0123456789"
    rev_number_line = number_line[::-1]
    text = text.upper() #text that will be encrypted
    en_text = ""  #will storage the encrypted text

    for i in range(len(text)):
        if text[i] == chr(32):
            en_text += " "
        elif text[i] == chr(46):
            en_text += "."
        elif text[i] == chr(64):
            en_text += "@"
        elif text[i] == chr(45):
            en_text += "-"
        elif text[i] == chr(95):
            en_text += "_"
        elif text[i] == chr(42):
            en_text += "_"
        else:
            for j in range(len(alphabet)):
                if text[i] == alphabet[j]:
                    en_text += rev_alphabet[j]
            for k in range(len(number_line)):
                if text[i] == number_line[k]:
                    en_text += rev_number_line[k]



    en_text = en_text.lower()


    return en_text



def at_decryption(en_text):

    '''
    this function takes a text and returns it
    encrypted in atbash cypher
    '''

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rev_alphabet = alphabet[::-1]

    number_line = "0123456789"
    rev_number_line = number_line[::-1]

    en_text = en_text.upper() #text that will be encrypted
    de_text = ""  #will storage the encrypted text

    for i in range(len(en_text)):
        if en_text[i] == chr(32):
            de_text += " "
        elif en_text[i] == chr(46):
            de_text += "."
        elif en_text[i] == chr(64):
            de_text += "@"
        elif en_text[i] == chr(45):
            de_text += "-"
        elif en_text[i] == chr(95):
            de_text += "_"
        elif en_text[i] == chr(42):
            de_text += "*"
        else:
            for j in range(len(rev_alphabet)):
                if en_text[i] == rev_alphabet[j]:
                    de_text += alphabet[j]
            for k in range(len(rev_number_line)):
                if en_text[i] == rev_number_line[k]:
                    de_text += number_line[k]


    de_text = de_text.lower()


    return de_text


def erase_text(txtErase,filename_dir):

    '''
    this function erases a line from a textfile
    it does so by re-writing everything but the line you want erased
    '''

    worked = False
    try:

        with open(filename_dir,'r+') as file:
            d = file.readlines()
            file.seek(0)
            for i in d:
                if i != txtErase + "\n":
                    file.write(i)
                    file.truncate()
        worked == True

    except:
        print("An error occurred,please check the email or password you just wrote and try again")

    return worked

def create_safeword(safeword):

    completeName = os.path.join(g_path,at_encryption(safeword)+".txt")
    file = open(completeName,"w")
    file.write("**********vnzro orhg*********\n\n")
    file.close()

def main():
    print("Welcome! if you want to create an account,type 1:")
    print("If you already have an account,type 2:")
    condition = int(input())
    if condition == 1:

        safeword = str(input("Type the safeword you want to use: "))
        create_safeword(safeword)
        print("your account has been created!")

    else:
        safeword = str(input("Type in your safeword:"))
        print()

    enc_safeword = at_encryption(safeword)
    direc_safeword = f'\{enc_safeword}.txt'
    path = g_path + direc_safeword
    wantToAdd = False
    wantToRemove = False
    with open(path, 'r+') as f:
        f_allcontent = f.readlines()
        f_content = f.readline()

        if f_allcontent  == []:
            wantToAdd = True
        else:
            for line in f_allcontent:
                print(at_decryption(line),end='\n')
            print("\nWant to add or remove an email?")
            userAns = int(input("0 for add, 1 for remove,2 for none:"))
            if userAns == 0:
                wantToAdd = True
            elif userAns == 1:
                wantToRemove = True
            else:
                print("Program terminated.")

        while wantToRemove == True:
            removed = True
            while removed == True:

                emailToRemove = str(input("Type the email or password you want to remove:"))
                en_erase = at_encryption(emailToRemove)
                removed = erase_text(en_erase,path)
#                passwordToRemove = str(input("type the password associate to the email:"))
#                en_password = at_encryption(passwordToRemove)
#                removed = erase_text(en_password,path)
                removed = False

            if not removed:
                print("Want to remove something else?")
                userAns2 = int(input("0 for no,1 for yes:"))

                if userAns2 == 0:
                    wantToRemove = False



        while wantToAdd == True:
            email = str(input("\nType the email you want to store:"))
            password = str(input("\ntype the password to that email:"))
            f.write(at_encryption(email))
            f.write("\n")
            f.write(at_encryption(password))
            f.write("\n")
            print("\nWant to add another email?")
            wntToAdd = int(input("0 for no, 1 for yes\n"))
            if wntToAdd == 0:
                wantToAdd = False
                print("Program terminated.")

if __name__ == "__main__":
    main()

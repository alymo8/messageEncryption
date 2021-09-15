from cryptography.fernet import Fernet
  

question = input("type e for encryption or d for decryption: ")

while question != 'd' and question != 'e':
    question = input("Please type letter d or letter e: ")

# input file name
filename = input("please enter the path to the file you want to read from: ")
#file to write to (name)
outputname = input("please enter the name of the output file: ")

#read the input file
inputfile = open(filename, 'r')
message = inputfile.read()
inputfile.close()




# generate a key for encryption and decryption
# You can use fernet to generate 
# the key or use random key generator
# here I'm using fernet to generate key
if question == 'e':
    key = Fernet.generate_key()
    # Instance the Fernet class with the key
    
    fernet = Fernet(key)
    
    # then use the Fernet class instance 
    # to encrypt the string string must must 
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())
    
    # this is the key the sender should provide to the receiver
    # so that they can decrypt the message
    print("key: ", key.decode())
    # write to the output file
    text_file = open(outputname, "w")
    write = text_file.write(encMessage.decode())
    text_file.close()
  
if question == 'd':

    # decrypt the encrypted string with the 
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methos
    key = input("please enter the key: ")
    fernet = Fernet(key)
    decMessage = fernet.decrypt(message.encode()).decode()
    
     # write to the output file
    text_file = open(outputname, "w")
    write = text_file.write(decMessage)
    text_file.close()
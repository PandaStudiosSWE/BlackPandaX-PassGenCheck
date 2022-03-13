import random, string, os, hashlib, requests
#Made By ★ 𝘗𝘢𝘯𝘥𝘢𝘚𝘵𝘶𝘥𝘪𝘰𝘴 ★#0001 (BlackPandaX on THM)
def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(" [1] Generate Password [2] Generate Password List [3] Check Password\n")
    print(" Passwords generated are safe as they're checked so that they're not in any data breach\n\n")
    
    option = input("\n Enter Option: ")
    
    if option == "1":
        
        characters = list(string.ascii_letters + string.digits + "ඞ!@#$%^&*()" + "ඞåäöÅÄÖ")
        length = int(input(" \n Enter password length: "))
        input(f"\n Your Password: {pass_gen(length, characters)}")
    
    elif option == "2":
        
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()" + "åäöÅÄÖ")
        ammount = int(input("\n Enter ammount of passwords to generate: "))
        
        with open(f"[{ammount}] Secure-Passwords.txt", 'w') as f:
            for i in range(ammount):
                    b = pass_gen(50, characters)
                    f.write(f"{b}\n\n")
                    
        print("\n Done!")
        input("\n Press enter to return to menu")
    
    elif option == "3":
        
        passwd = input(" \n Enter your password: ")
        pass_check(passwd)
        
    else:
        main()
    
    main()
        
def pass_gen(a, b):
    
    random.shuffle(b)
    
    password = []
    for i in range(a):
    
        password.append(random.choice(b))
        
    random.shuffle(password)
    
    factory_pass = "".join(password)
    
    if leak_check(factory_pass) is "Cracked":
    
        pass_gen(a)
        
    elif leak_check(factory_pass) is "Safe":
    
        return factory_pass
    
        
def pass_check(a):
    
    if leak_check(a) is "Cracked":
    
        print(f"\n {a} has Been Cracked!")
        input("\n Press enter to return to menu")
        main()
        
    elif leak_check(a) is "Safe":
    
        print("\n {a} Has Not Been Cracked!")
        input("\n Press enter to return to menu")
        main()
        
def leak_check(a):
    
    SHA1 = hashlib.sha1(a.encode('utf-8'))
    hash_string = SHA1.hexdigest().upper()
    prefix = hash_string[0:5]
    
    header = {'User-Agent':'password checker'}
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    req = requests.get(url, headers=header).content.decode('utf-8')
    hashes = dict(t.split(":") for t in req.split('\r\n'))
    hashes = dict((prefix + key, value) for (key, value) in hashes.items())
    

    if hash_string in hashes:
        return "Cracked"
            
    elif hash_string not in hashes:
        return "Safe"
            
    
    
if __name__ == "__main__":
    main()
    
#Made By ★ 𝘗𝘢𝘯𝘥𝘢𝘚𝘵𝘶𝘥𝘪𝘰𝘴 ★#0001
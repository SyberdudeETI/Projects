
print("Passwort muss genau 8 Buchstaben, 2 Zahlen und 3 Sonderzeichen (!$%&?*#) enthalten und insgesamt 13 Zeichen lang sein.")

while True:  
    password = input("Bitte Passwort eingeben: ")

    
    buchstaben = sum(1 for z in password if z.isalpha())
    zahlen = sum(1 for z in password if z.isdigit())
    sonderzeichen = sum(1 for z in password if z in "!$%&?*#")

    
    if len(password) != 13:
        print(f"❌ Passwort muss genau 13 Zeichen lang sein. Dein Passwort hat {len(password)} Zeichen.")
        continue

    
    if buchstaben != 8:
        print(f"❌ Passwort muss genau 8 Buchstaben enthalten. Dein Passwort hat {buchstaben}.")
        continue

    
    if zahlen != 2:
        print(f"❌ Passwort muss genau 2 Zahlen enthalten. Dein Passwort hat {zahlen}.")
        continue

    
    if sonderzeichen != 3:
        print(f"❌ Passwort muss genau 3 Sonderzeichen enthalten. Dein Passwort hat {sonderzeichen}.")
        continue

    
    print("✅ Passwort ist gültig! Vorgang abgeschlossen!")
    print(f"Dein Passwort: {password}")
    break  

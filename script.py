dictOriginal = "rockyou.txt"
dictMod = "rockyou_mod.dic"

def numStart(s):
    return s[0].isdigit()

def capitalize(password):
    return password[0].upper() + password[1:] + "0"

with open(dictOriginal, "r", encoding="latin-1") as f_orig, open(dictMod, "w") as f_mod:
    for linea in f_orig:
        linea = linea.strip()
        if linea and not numStart(linea):
            passMod = capitalize(linea)
            f_mod.write(passMod + "\n")

with open(dictMod, "r") as f_mod:
    numPass = sum(1 for _ in f_mod)
    
print("Cantidad de contraseñas modificadas en el diccionario:", numPass)

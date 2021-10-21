def run():
    pass


welcome = """
----------------------------
Ingresa la cadena inicial: 
----------------------------
"""
string = str(input(welcome))
print("")

# ascii 78 N ascii 83 S

flag_to_continue = 0

strings_total = []
string_lengths = []
string_greater = []

strings_total.append(string)
string_lengths.append(len(string))

to_continue = input("Deseas ingresar una nueva cadena? (S/N): ")
print("")

while flag_to_continue == 0:
    if str(to_continue) == "":
        print("Ingresa una respuesta válida. Recuerda, solo puedes ingresar S o N")
        to_continue = input("Deseas ingresar una nueva cadena? (S/N): ")
        print("")
    elif len(to_continue) > 1:
        print("Ingresa una respuesta válida. Recuerda, solo puedes ingresar S o N")
        to_continue = input("Deseas ingresar una nueva cadena? (S/N): ")
        print("")
    elif ord(str(to_continue)) > 4 and ord(str(to_continue)) < 58:
        print("Ingresa una respuesta válida. Recuerda, solo puedes ingresar S o N")
        to_continue = input("Deseas ingresar una nueva cadena? (S/N): ")
        print("")
        str(to_continue) == ""
    elif str(to_continue.upper()) == "S":
        string = input("Ingresa la nueva cadena: ")
        print("")
        strings_total.append(string)
        string_lengths.append(len(string))
        to_continue = input("Deseas ingresar una nueva cadena? (S/N): ")
        print("")
        pass
    elif str(to_continue.upper()) == "N":
        pass
        flag_to_continue = 1

string_lengths.sort(reverse=True)

max_lenght = string_lengths[0]

print("La(s) cadena(s) más larga(s) fue(ron):")
print("")

for i in range(len(strings_total)):
    if len(strings_total[i]) == int(max_lenght):
        print("Cadena No " + str(i+1) +
              " ('"+str(strings_total[i])+"') con "+str(max_lenght)+" caracteres")
        string_greater.append(strings_total[i])

print("")
print("La(s) cadena(s) ingresada(s) fue(ron):")
print("")

cont = 1
for i in strings_total:
    print(str(cont)+". "+i)
    cont += 1


if __name__ == "__main__":
    run()

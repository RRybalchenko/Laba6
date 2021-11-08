def rot(Nummer):
    Nummer = str(Nummer)
    Nummer = Nummer.replace('6', '9', 1)
    return int(Nummer)

Diegostezahlrot = rot(96966669996969696)
print(Diegostezahlrot)

#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

koko = float(input("Anna kuhan pituus senttimetreinä: "))
erotus = 37 - koko
if koko < 37:
    print("Laske kuha takaisin järveen. Kuha alimmast sallitusta pyyntimitasta puuttuu: " + str(erotus) + "cm")
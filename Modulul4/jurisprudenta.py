from termcolor import colored


def checkhome():
    home_secure = True
    if not home_secure:
        safe_house = ("""Drept penal. Partea specială I, ediţia 2 ,
            Infracţiunea de hărţuire nu are corespondent în legislaţia penală anterioară. /
            Introducerea în acest capitol a unei incriminări noi, hărţuirea, are menirea de a răspunde unor cazuri apărute în practică,/
            Este vorba despre o faptă îndreptată contra libertăţii psihice a persoanei, o specie insidioasă de ameninţare,/
            Şi în acest caz, este vorba despre adaptarea legislaţiei penale la realităţile sociale, ştiut fiind faptul că, /
            în ultimii ani, tot mai multe persoane sunt agresate prin apeluri sau mesaje telefonice, /
            ori electronice, sunt urmărite sau pândite, uneori în mod ostentativ, în apropierea locuinţei, /
            a locului de muncă ori în alte locuri pe care le frecventează, toate aceste acţiuni la care sunt supuse,/
            fiind de natură a le crea o stare de temere399. Cred că şi această incriminare este binevenită,/
            cu ajutorul ei legiuitorul reuşind să acopere un alt vid legislativ. [ Mai mult... ] """)
    else:
        print(colored("I ll go on vacation, on Transfagarasan!", 'magenta'))


checkhome()

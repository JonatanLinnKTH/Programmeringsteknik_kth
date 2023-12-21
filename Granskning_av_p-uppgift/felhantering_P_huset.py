
def felBiltyp(utskrift):
    """Kollar om användaren matat in biltypen rätt"""

    biltyp = input(utskrift)
    while True:
        try:
            biltyp = int(biltyp)
        except:
            print("Vänligen ange 1 för liten bil, 2 för mellanbil eller 3 för storbil")
            biltyp = input(utskrift)

        if biltyp == 1 or biltyp == 2 or biltyp == 3:

            return biltyp
            break
        else:
            print("Vänligen ange 1 för liten bil, 2 för mellanbil eller 3 för storbil")
            biltyp = input(utskrift)


def felTid(utskrift):
    """Ser till att användaren matat in tiden rätt"""

    tid = input(utskrift)
    while True:
        checkInt = 0
        checkLängd = 0
        try:
            if len(tid) == 5:
                test = int(tid[0:1])
                test1 = int(tid[3:5])
        except:
            checkInt += 1

        if len(tid) == 5:
            if tid[2] == ":":
                checkLängd += 1

        if checkLängd == 1 and checkInt == 0:
            return tid
            break
        else:
            print("Fel")
            tid = input(utskrift)


def felReg_nr(utskrift):
    """Kollar om formatet på regnr är rätt"""
    reg_nr = input(utskrift)
    while True:
        if len(reg_nr) == 6 and reg_nr[0:3].isalpha() and reg_nr[3:5].isnumeric() and (reg_nr[5:6].isnumeric() or reg_nr[5:6].isalpha()):
            return reg_nr
            break
        else:
            print("Fel format")
            reg_nr = input(utskrift)


def felDatum():
    """Kollar om formatet på datumet är rätt"""

    print("Ange datum (åå-mm-dd) ")
    datum = input(">>> ")
    while True:
        if len(datum) == 8 and datum[2] == "-" and datum[5] == "-" and datum[0:2].isnumeric() and datum[3:5].isnumeric() and datum[6:8].isnumeric() and int(datum[3:5]) <= 12 and int(datum[6:8]) <= 31:
            break
        else:
            print("Fel format")
            datum = input("Ange datum (åå-mm-dd) ")

    return datum


def felInläsningInUtPassage(rad):
    """Kollar om datan från den inlästa filen är i korrekt format"""
    checkRegnr=0
    checkStartid=0
    checkSluttid=0
    checkDatum=0

    reg_nr = rad[0:6]
    if len(reg_nr) == 6 and reg_nr[0:3].isalpha() and reg_nr[3:5].isnumeric() and (reg_nr[5:6].isnumeric() or reg_nr[5:6].isalpha()):
        checkRegnr+=1

    starttid = rad[7:12]
    if felTidInläsning(starttid):
        checkStartid+=1

    sluttid = rad[13:18]
    if felTidInläsning(sluttid):
        checkSluttid+=1

    datum = rad[19:27]
    if len(datum) == 8 and datum[2] == "-" and datum[5] == "-" and datum[0:2].isnumeric() and datum[3:5].isnumeric() and datum[6:8].isnumeric() and int(datum[3:5]) <= 12 and int(datum[6:8]) <= 31:
        checkDatum+=1

    if checkRegnr==1 and checkStartid==1 and checkSluttid==1 and checkDatum==1:
        return True
    else:
        return False


def felInläsningBilar(rad):
    """Kollar om datan från den inlästa filen är i korrekt format"""
    checkRegnr=0
    checkStorlek = 0

    reg_nr = rad[0:6]
    if len(reg_nr) == 6 and reg_nr[0:3].isalpha() and reg_nr[3:5].isnumeric() and (reg_nr[5:6].isnumeric() or reg_nr[5:6].isalpha()):
        checkRegnr+=1

    storlek = rad[7:8]
    try:
        storlekInt = int(storlek)
        if storlekInt == 1 or storlekInt == 2 or storlekInt == 3:
            checkStorlek += 1
    except:
        print("Hello")
        return False

    if checkRegnr==1 and checkStorlek==1:
        return True
    else:
        return False

def felTidInläsning(tid):
    """Kollar om formatet av tiden är rätt"""
    checkInt=0
    checkLängd=0
    try:
        if len(tid) == 5:
            test = int(tid[0:1])
            test1 = int(tid[3:5])
    except:
        checkInt += 1

    if len(tid) == 5:
        if tid[2] == ":":
            checkLängd += 1

    if checkLängd == 1 and checkInt == 0:
        return True
    else:
        return False
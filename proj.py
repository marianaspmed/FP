def artigo_def(x, pos, qtd):
    if x[pos:pos + qtd] in ("A", "O"):
        return True
    return False


def vogal_palavra(x, pos, qtd):
    if artigo_def(x, pos, qtd):
        return True
    if x[pos:pos + qtd] == "E":
        return True
    return False


def vogal(x, pos, qtd):
    if x[pos:pos + qtd] in ("I", "U"):
        return True
    if vogal_palavra(x, pos, qtd):
        return True
    return False


def ditongo_palavra(x, pos, qtd):
    if x[pos:pos + qtd] in ("AI", "AO", "EU", "OU"):
        return True
    return False


def ditongo(x, pos, qtd):
    if x[pos:pos + qtd] in ("AE", "AU", "EI", "OE", "OI", "IU"):
        return True
    if ditongo_palavra(x, pos, qtd):
        return True
    return False


def par_vogais(x, pos, qtd):
    if ditongo(x, pos, qtd):
        return True
    if x[pos:pos + qtd] in ("IA", "IO"):
        return True
    return False


def consoante_freq(x, pos, qtd):
    if x[pos:pos + qtd] in ("D", "L", "M", "N", "P", "R", "S", "T", "V"):
        return True
    return False


def consoante_terminal(x, pos, qtd):
    if x[pos:pos + qtd] in ("L", "M", "R", "S", "X", "Z"):
        return True
    return False


def consoante_final(x, pos, qtd):
    if x[pos:pos + qtd] in ("N", "P"):
        return True
    if consoante_terminal(x, pos, qtd):
        return True
    return False


def consoante(x, pos, qtd):
    if qtd == 1:
        if x[pos:pos + 1] in ("B", "C", "D", "F", "G", "H", "J", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z"):
            return True
    return False


def par_consoantes(x, pos, qtd):
    if qtd == 2:
        if x[pos:pos + 2] in ("BR", "CR", "FR", "GR", "PR", "TR", "VR", "BL", "CL", "FL", "GL", "PL"):
            return True
    return False


def monossilabo_2(x, pos, qtd):
    if qtd == 2:
        if x[pos:pos + 2] in ("AR", "IR", "EM", "UM"):
            return True
        if vogal_palavra(x, pos, 1) and x[pos + 1:pos + 2] == "S":
            return True
        if ditongo_palavra(x, pos, 2):
            return True
        if consoante_freq(x, pos, 1) and vogal(x, pos + 1, 1):
            return True
    return False


def monossilabo_3(x, pos, qtd):
    if qtd == 3:
        if consoante(x, pos, 1) and vogal(x, pos + 1, 1) and consoante_terminal(x, pos + 2, 1):
            return True
        if consoante(x, pos, 1) and ditongo(x, pos + 1, 2):
            return True
        if par_vogais(x, pos, 2) and consoante_terminal(x, pos + 2, 1):
            return True
    return False


def monossilabo(x):
    if vogal_palavra(x, 0, len(x)):
        return True,
    if monossilabo_2(x, 0, len(x)):
        return True,
    if monossilabo_3(x, 0, len(x)):
        return True
    return False


def silaba_2(x, pos, qtd):
    if qtd == 2:
        if par_vogais(x, pos, 2):
            return True
        if consoante(x, pos, 1) and vogal(x, pos + 1, 1):
            return True,
        if vogal(x, pos, 1) and consoante_final(x, pos + 1, 1):
            return True
    return False


def silaba_3(x, pos, qtd):
    if qtd == 3:
        if x[pos:pos + 3] in ("QUA", "QUE", "QUI", "GUE", "GUI"):
            return True
        if vogal(x, pos, 1) and x[pos + 1:pos + 3] == "NS":
            return True
        if consoante(x, pos, 1) and par_vogais(x, pos + 1, 2):
            return True
        if consoante(x, pos, 1) and vogal(x, pos + 1, 1) and consoante_final(x, pos + 2, 1):
            return True
        if par_vogais(x, pos, 2) and consoante_final(x, pos + 2, 1):
            return True
        if par_consoantes(x, pos, 2) and vogal(x, pos + 2, 1):
            return True
    return False


def silaba_4(x, pos, qtd):
    if qtd == 4:
        if par_vogais(x, pos, 2) and x[pos + 2:pos + 4] == "NS":
            return True
        if consoante(x, pos, 1) and vogal(x, pos + 1, 1) and x[pos + 2:pos + 4] == "NS":
            return True
        if consoante(x, pos, 1) and vogal(x, pos + 1, 1) and x[pos + 2:pos + 4] == "IS":
            return True
        if par_consoantes(x, pos, 2) and par_vogais(x, pos + 2, 2):
            return True
        if consoante(x, pos, 1) and par_vogais(x, pos + 1, 2) and consoante_final(x, pos + 3, 1):
            return True
    return False


def silaba_5(x, pos, qtd):
    if qtd == 5:
        if par_consoantes(x, pos, 2) and vogal(x, pos + 2, 1) and x[pos + 3:pos + 5] == "NS":
            return True
    return False


def silaba_final(x):
    if monossilabo_2(x[-2:], 0, 2):
        return True, x[:-2]
    if monossilabo_3(x[-3:], 0, 3):
        return True, x[:-3]
    if silaba_4(x[-4:], 0, 4):
        return True, x[:-4]
    if silaba_5(x[-5:], 0, 5):
        return True, x[:-5]
    return False, 0


def silaba(x):
    if vogal(x, 0, len(x)):
        return True
    if silaba_2(x, 0, len(x)):
        return True
    if silaba_3(x, 0, len(x)):
        return True
    if silaba_4(x, 0, len(x)):
        return True
    if silaba_5(x, 0, len(x)):
        return True
    return False


def palavra(x):
    if monossilabo(x):
        return True
    silaba_final_ok, subpalavra = silaba_final(x)
    if silaba_final_ok:
        if not monossilabo(subpalavra):
            return True
    return False


def e_silaba(x):
    if not isinstance(x, str):
        raise ValueError('e_silaba:argumento invalido')
    else:
        if silaba(x):
            return True
        else:
            return False


def e_monossilabo(x):
    if not isinstance(x, str):
        raise ValueError('e_monossilabo:argumento invalido')
    else:
        if monossilabo(x):
            return True
        else:
            return False


def e_palavra(x):
    if not isinstance(x, str):
        raise ValueError('e_palavra:argumento invalido')
    else:
        if palavra(x):
            return True
        else:
            return False

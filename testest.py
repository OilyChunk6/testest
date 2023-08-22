def xmove(grille, casesprisesx, casespriseso):
    xmove = input("X, choisissez une case: ")
    if xmove in casesprisesx or xmove in casespriseso:
        print("Case déjà prise")
        xmove = input("X, choisissez une case: ")
    elif xmove == "" or xmove not in "123456789":
        print("veulliez choisir une case valide")
        xmove = input("X, choisissez une case: ")
    else:
        casesprisesx.append(xmove)
        grille = grille.replace(xmove, "X")
        return grille, casesprisesx


def omove(grille, casesprisesx, casespriseso):
    omove = input("O, choisissez une case: ")
    if omove in casesprisesx or omove in casespriseso:
        print("Case déjà prise")
        omove = input("O, choisissez une case: ")
    elif omove == "" or omove not in "123456789":
        print("veulliez choisir une case valide")
        omove = input("O, choisissez une case: ")
    else:
        casespriseso.append(omove)
        grille = grille.replace(omove, "O")
    return grille, casespriseso


def main():
    grille: str = "1|2|3\n4|5|6\n7|8|9"
    listewin: list = [["1","2","3"], ["4","5","6"], ["7","8","9"], ["1","4","7"], ["2","5","8"], ["3","6","9"], ["1","5","9"], ["3","5","7"]]
    casesprisesx: list = []
    casespriseso: list = []
    print(grille)
    while len(casesprisesx + casespriseso) < 9:
        grille, casesprisesx = xmove(grille, casesprisesx, casespriseso)
        print(grille)
        for i in range(0, 7):
            if casesprisesx == listewin[i]:
                print("X a gagné")
                break
        grille, casespriseso = omove(grille, casesprisesx, casespriseso)
        print(grille)
        for i in range(0, 7):
            if casespriseso == listewin[i]:
                print("O a gagné")
                break
    print("Match nul")


main()

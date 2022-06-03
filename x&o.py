
def numar_pozitii_completate(board):
    """ Numara cate pozitii sunt completate """
    nr_elemente = 9
    for linie in board:
        for element in linie:
            if element is None:
                nr_elemente -= 1
    return nr_elemente


def elemente_in_board(board):
    """ Completeaza o lista cu toate elementele diferite din board (Ex: X, O) """
    elemente = []
    x = 0
    o = 0
    for line in board:
        for element in line:
            if element == "X":
                x += 1
            elif element == "O":
                o += 1
    if x >= 2:
        elemente.append("X")
    if o >= 2:
        elemente.append("O")
    return elemente


def doi_din_trei(board, marker):
    """ Verifica daca pe o linie/ coloana/ diagonala exista markeri consecutivi, de aceeasi valoare, si un spatiu liber
    care ar putea fi completat. Returneaza coordonatele spatiului liber."""
    coord_x = ""
    coord_y = ""
    lista_markeri = elemente_in_board(board)
    # pun in lista pe prima pozitie markerul meu
    if len(lista_markeri) > 1:
        if lista_markeri.index(marker) == 1:
            lista_markeri.reverse()
    orizontal = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]
    vertical = [[(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
    diavonale = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    while lista_markeri:
        marker = lista_markeri.pop(0)
        for linie in orizontal:
            nr_markei = 0
            none = False
            for pozitie in linie:
                if board[pozitie[0]][pozitie[1]] == marker:
                    nr_markei += 1
                if board[pozitie[0]][pozitie[1]] is None:
                    none = True
                if nr_markei == 2 and none:
                    coord_x = pozitie[0]
                    coord_y = board[pozitie[0]].index(None)
                    return coord_x, coord_y
        for coloana in vertical:
            nr_markei = 0
            none = False
            for pozitie in coloana:
                if board[pozitie[0]][pozitie[1]] == marker:
                    nr_markei += 1
                if board[pozitie[0]][pozitie[1]] is None:
                    coord_x = pozitie[0]
                    coord_y = pozitie[1]
                    none = True
                if nr_markei == 2 and none:
                    return coord_x, coord_y
        for diavonala in diavonale:
            nr_markei = 0
            none = False
            for pozitie in diavonala:
                if board[pozitie[0]][pozitie[1]] == marker:
                    nr_markei += 1
                if board[pozitie[0]][pozitie[1]] is None:
                    coord_x = pozitie[0]
                    coord_y = pozitie[1]
                    none = True
                if nr_markei == 2 and none:
                    return coord_x, coord_y
    return -1, -1


def pozitie_ocupata(board, marker):
    """ Returneaza coordonatele primului marker din board """
    for coord_x, linie in enumerate(board):
        for coord_y, element in enumerate(linie):
            if element == marker:
                return coord_x, coord_y
    return -1, -1


def pozitii_ocupate(board, marker):
    """ Returneaza coordonatele a doi markeri din board """
    pozitii_gasite = 0
    coord_marker_1 = ()
    coord_marker_2 = ()
    for coord_x, linie in enumerate(board):
        for coord_y, element in enumerate(linie):
            if element == marker:
                if pozitii_gasite == 0:
                    coord_marker_1 = coord_x, coord_y
                    pozitii_gasite += 1
                else:
                    coord_marker_2 = coord_x, coord_y
                    pozitii_gasite += 1
                if pozitii_gasite == 2:
                    return coord_marker_1, coord_marker_2
    return (-1, -1), (-1, -1)


def intrusi(board, lista, marker):
    """ Verifica daca intr-o lista de linii/ coloane/ diagonale se afla markerul oponentului """
    for element in lista:
        if board[element[0]][element[1]] != marker:
            if board[element[0]][element[1]] is not None:
                return True
    return False


def exist_in_lista(board, lista, marker):
    """ Verifica daca intr-o lista de linii/ coloane/ diagonale se afla markerul meu """
    for element in lista:
        if board[element[0]][element[1]] == marker:
            return True
    return False


def marker_oponent(marker):
    """ Returneaza valoarea markerului oponentului """
    if marker == "X":
        oponent = "O"
    else:
        oponent = "X"
    return oponent


def inversa():
    """ Returneaza o matrice care are valorile de pe linii inversate si liniile inversate """
    matrice = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)]
    ]
    inversata = matrice
    for linie in inversata:
        linie.reverse()
    inversata.reverse()
    return inversata


def doua_spatii_goale(board, linie):
    """ Verifica daca pe o linie se afla doua spatii necompletate """
    none = 0
    for element in linie:
        pozitie = board[element[0]][element[1]]
        if pozitie is None:
            none += 1
    if none == 2:
        return True
    return False


def pct_intersectie(board, linii_si_diagonale, marker, punct):
    """ Returneaza True daca un punct dat reprezinta punctul de intersectie a doi markeri de aceeasi valoare"""
    conditie = 0
    for linie in linii_si_diagonale:
        none = 0
        marker_found = False
        if punct in linie:
            for element in linie:
                if board[element[0]][element[1]] is None:
                    none += 1
                if board[element[0]][element[1]] == marker:
                    marker_found = True
            if none == 2 and marker_found:
                conditie += 1
    return conditie >= 2


def intersectie(board, marker, linii_si_diagonale):
    """ Verifica daca exista doi markeri de aceeasi valoare, si daca se poate gasi o linie cu doua spatii necompletate
    pentru fiecare dintre ei. Daca aceste linii se intersecteaza returneaza coordonatele punctului de intersectie """
    linie_marker_1 = []
    linie_marker_2 = []
    coord_marker_1, coord_marker_2 = pozitii_ocupate(board, marker)
    if coord_marker_1[0] > -1:
        for linie in linii_si_diagonale:
            if doua_spatii_goale(board, linie):
                for pozitie in linie:
                    if coord_marker_1 == pozitie:
                        linie_marker_1 = linie
                    if coord_marker_2 == pozitie:
                        linie_marker_2 = linie
            if linie_marker_1 and linie_marker_2:
                for pozitie_1 in linie_marker_1:
                    for pozitie_2 in linie_marker_2:
                        if pozitie_1 == pozitie_2:
                            coord_x = pozitie_1[0]
                            coord_y = pozitie_1[1]
                            return coord_x, coord_y
    return -1, -1


def saboteaza(board, oponent, linii_si_diagonale):
    """ Verifica daca exista un punct de intersectie pentru markerul oponentului si returneaza coordonatele acestuia """
    coord_x, coord_y = intersectie(board, oponent, linii_si_diagonale)
    if coord_x > -1:
        return coord_x, coord_y
    return -1, -1


def give_up(board):
    for index_x, linie in enumerate(board):
        for index_y, element in enumerate(linie):
            if element is None:
                coord_x = index_x
                coord_y = index_y
                return coord_x, coord_y
    return -1, -1


def semi_strategy(board, linii_si_diagonale):
    """ Daca exista doua linii libere si acestea se intersecteaza, voi returna coordonatele punctului de intersectie"""
    linii_goale = []
    for linie in linii_si_diagonale:
        none = 0
        for element in linie:
            if board[element[0]][element[1]] is None:
                none += 1
        if none == 3:
            linii_goale.append(linie)
    if len(linii_goale) == 2:
        linie1 = linii_goale[0]
        linie2 = linii_goale[1]
        for pozitie1 in linie1:
            for pozitie2 in linie2:
                if pozitie1 == pozitie2:
                    coord_x = pozitie1[0]
                    coord_y = pozitie1[1]
                    return coord_x, coord_y
    return -1, -1


def no_strategy(board, linii_si_diagonale, marker):
    """ Cauta o linie care are doua pozitii necompletate si una ocupata de markerul meu, respectiv o linie cu trei
    spatii necompletate """
    for linie in linii_si_diagonale:
        if doua_spatii_goale(board, linie):
            if exist_in_lista(board, linie, marker):
                for pozitie in linie:
                    element = board[pozitie[0]][pozitie[1]]
                    if element is None:
                        coord_x = pozitie[0]
                        coord_y = pozitie[1]
                        return coord_x, coord_y
    for linie in linii_si_diagonale:
        none = 0
        for pozitie in linie:
            element = board[pozitie[0]][pozitie[1]]
            if element is None:
                none += 1
            if none == 3:
                coord_x = pozitie[0]
                coord_y = pozitie[1]
                return coord_x, coord_y
    return -1, -1


def start_first(board, nr_poz_completate, linii, colturi, linii_si_diagonale, centru, mijloace, oponent, marker):
    """ Mutari posibile pentru jucatorul care incepe primul"""
    coord_x_op, coord_y_op = -1, -1
    if nr_poz_completate == 0:
        coord_x = 2
        coord_y = 1
        return coord_x, coord_y
    if nr_poz_completate == 2:
        # Strategie colt
        if exist_in_lista(board, colturi, marker):
            # Daca oponentul nu a completat in centru, aleg cel mai apropiat colt
            if not intrusi(board, centru, marker):
                coord_x, coord_y = pozitie_ocupata(board, marker)
                if coord_x > -1:
                    for linie in linii:
                        for index, pozitie in enumerate(linie):
                            if pozitie[0] == coord_x and pozitie[1] == coord_y:
                                if not intrusi(board, linie, marker):
                                    linie.reverse()
                                    coord_x = linie[index][0]
                                    coord_y = linie[index][1]
                                    return coord_x, coord_y
            # Daca oponentul a completat in centru, caut pozitia opousa de pe diagonala markerului meu
            else:
                coord_x, coord_y = pozitie_ocupata(board, marker)
                if coord_x > -1:
                    inversata = inversa()
                    coord_x = inversata[coord_x][coord_y][0]
                    coord_y = inversata[coord_x][coord_y][1]
                    return coord_x, coord_y
        # Strategie centru
        if exist_in_lista(board, centru, marker):
            # Daca oponentul a completat o pozitie laterala, de pe linia respectiva, voi alege un colt
            if intrusi(board, mijloace, marker):
                for linie in linii:
                    if intrusi(board, linie, marker):
                        for colt in colturi:
                            for element in linie:
                                if colt == element:
                                    coord_x = colt[0]
                                    coord_y = colt[1]
                                    return coord_x, coord_y
            # Daca oponentul a completat un colt, completez poztita opusa de pe diagonala cu markerul oponentului
            else:
                coord_x, coord_y = pozitie_ocupata(board, oponent)
                if coord_x > -1:
                    inversata = inversa()
                    coord_x = inversata[coord_x][coord_y][0]
                    coord_y = inversata[coord_x][coord_y][1]
                    return coord_x, coord_y
        # Strategie pozitii laterale
        if exist_in_lista(board, mijloace, marker):
            coord_x, coord_y = pozitie_ocupata(board, marker)
            if coord_x > -1:
                coord_x_op, coord_y_op = pozitie_ocupata(board, oponent)
                if coord_x_op > -1:
                    coord_op = coord_x_op, coord_y_op
                    # caut colturile veciune posibile pentru markerul meu
                    if coord_x % 2 == 0:
                        posibilitati_colturi = [(coord_x, coord_y - 1), (coord_x, coord_y + 1)]
                    else:
                        posibilitati_colturi = [(coord_x - 1, coord_y), (coord_x + 1, coord_y)]
                    # Verific daca markerul oponentului se alfa intr-unul din colturile vecine ale markerului meu
                    for element in posibilitati_colturi:
                        if coord_op == element:
                            # Caut o linia pe care se afla doar markerul oponentului, si completez coltul liber
                            # (fara diagonale)
                            for linie in linii:
                                if not exist_in_lista(board, linie, marker) and intrusi(board, linie, marker):
                                    if linie[0] == coord_op:
                                        linie.reverse()
                                    coord_x = linie[0][0]
                                    coord_y = linie[0][1]
                                    return coord_x, coord_y
            # Dacaoponentul a ales o pozitie din centru sau o pozitie laterala opusa markerului meu, caut un colt
            # care nu este vecin cu markerul meu
            for linie in linii:
                # Caut o linie care sa aiba si markerul meu si markerul oponentului
                if exist_in_lista(board, linie, marker) and intrusi(board, linie, marker):
                    # Caut o linie care are doar markerul meu
                    for varianta in linii:
                        if exist_in_lista(board, varianta, marker) and not intrusi(board, varianta, marker):
                            # Salvez coordonatele colturilor vecine markerului meu
                            colturi_vecine = [varianta[0], varianta[2]]
                            # Trec prin coordonatele colturilor din board
                            for colt in colturi:
                                # Aleg un colt din board care nu este vecin cu markerul meu
                                for colt_vecin in colturi_vecine:
                                    if colt != colt_vecin:
                                        coord_x = colt[0]
                                        coord_y = colt[1]
                                        return coord_x, coord_y
            # Pentru orice alta varianta aleg coltul vecin markerului meu
            if coord_x % 2 == 0:
                coord_y = coord_y_op
                return coord_x, coord_y
            else:
                coord_x = coord_x_op
                return coord_x, coord_y
    if nr_poz_completate == 4:
        coord_x, coord_y = intersectie(board, marker, linii_si_diagonale)
        if coord_x > -1:
            return coord_x, coord_y
        coord_x, coord_y = saboteaza(board, oponent, linii_si_diagonale)
        if coord_x > -1:
            return coord_x, coord_y
        coord_x, coord_y = semi_strategy(board, linii_si_diagonale)
        if coord_x > -1:
            return coord_x, coord_y
        coord_x, coord_y = no_strategy(board, linii_si_diagonale, marker)
        if coord_x > -1:
            return coord_x, coord_y
    if nr_poz_completate == 6:
        coord_x, coord_y = no_strategy(board, linii_si_diagonale, marker)
        if coord_x > -1:
            return coord_x, coord_y
        coord_x, coord_y = give_up(board)
        if coord_x > -1:
            return coord_x, coord_y
    if nr_poz_completate == 8:
        # Daca nu sunt doi markeri de aceeasi valoare consecutivi si o pozitie libera pe acea linie care ar putea
        # fi completata, aleg orice pozitie libera de pe board
        coord_x, coord_y = give_up(board)
        if coord_x > -1:
            return coord_x, coord_y
    return -1, -1


def start_second(board, nr_poz_completate, mijloace, centru, colturi, linii_si_diagonale, oponent, marker):
    """ Mutari posibile pentru jucatorul care incepe al doilea """
    if nr_poz_completate == 1:
        # Daca primul jucator a ales un colt, voi completa centrul
        if intrusi(board, colturi, marker):
            coodr_x = centru[0][0]
            coodr_y = centru[0][1]
            return coodr_x, coodr_y
        # Daca primul jucator a ales centrul, voi completa un colt
        if intrusi(board, centru, marker):
            coord_x = colturi[2][0]
            coord_y = colturi[2][1]
            return coord_x, coord_y
        # Daca primul jucator a ales o pozitie laterala, voi completa coltul vecin oponentului
        if intrusi(board, mijloace, marker):
            coord_op_x, coord_op_y = pozitie_ocupata(board, oponent)
            if coord_op_x > -1:
                if coord_op_x % 2 == 0:
                    coord_x = coord_op_x
                    coord_y = coord_op_y + 1
                    return coord_x, coord_y
                coord_x = coord_op_x + 1
                coord_y = coord_op_y
                return coord_x, coord_y
    if nr_poz_completate == 3:
        # Daca si eu si oponentul au jucat optim pana acum
        # Daca oponentul are o posibila intersectie incerc sa il fortez sa completeze in alta parte
        coord_sab = saboteaza(board, oponent, linii_si_diagonale)
        if coord_sab[0] > -1:
            coord_marker = pozitie_ocupata(board, marker)
            # Caut o linie cu doua spatii goale care sa contina si markerul meu
            for linie in linii_si_diagonale:
                pozitii_posibile = []
                intersectii_oponent = 0
                if doua_spatii_goale(board, linie):
                    if coord_marker in linie:
                        # Salvez intr-o lista coordonatele pozitiilor necompletate
                        for pozitie in linie:
                            if pozitie != coord_marker:
                                pozitii_posibile.append(pozitie)
                # Daca am pozitii care ar putea fi completate verific sa nu fie amandoua intersectii pentru oponent
                if pozitii_posibile:
                    coordonate = [-1, -1]
                    for element in pozitii_posibile:
                        if pct_intersectie(board, linii_si_diagonale, oponent, element):
                            intersectii_oponent += 1
                            coordonate = element
                    if intersectii_oponent == 2:
                        continue
                    # Daca doar una dintre pozitii reprezinta o intersectie voi completa acolo
                    elif intersectii_oponent == 1:
                        coord_x = coordonate[0]
                        coord_y = coordonate[1]
                        return coord_x, coord_y
                    # Daca nici unul din elemente nu reprezinta o intersectie pentru oponent, caut elementul
                    # care se afla pe o linie libera
                    elif intersectii_oponent == 0:
                        for element in pozitii_posibile:
                            for line in linii_si_diagonale:
                                if element in line:
                                    if doua_spatii_goale(board, linie):
                                        coord_x = element[0]
                                        coord_y = element[1]
                                        return coord_x, coord_y
                        # Altfel aleg orice element
                        coord_x = pozitii_posibile[0][0]
                        coord_y = pozitii_posibile[0][1]
                        return coord_x, coord_y
            # Daca nu am cum sa fortez o miscare, ii iau intersectia
            coord_x = coord_sab[0]
            coord_y = coord_sab[1]
            return coord_x, coord_y
        coord_x, coord_y = no_strategy(board, linii_si_diagonale, marker)
        return coord_x, coord_y
    if nr_poz_completate == 5:
        coord_x, coord_y = intersectie(board, marker, linii_si_diagonale)
        if coord_x > -1:
            return coord_x, coord_y
        coord_x, coord_y = saboteaza(board, oponent, linii_si_diagonale)
        if coord_x > -1:
            return coord_x, coord_y
        coord_x, coord_y = no_strategy(board, linii_si_diagonale, marker)
        if coord_x > -1:
            return coord_x, coord_y
        coord_x, coord_y = give_up(board)
        if coord_x > -1:
            return coord_x, coord_y
    if nr_poz_completate == 7:
        coord_x, coord_y = give_up(board)
        if coord_x > -1:
            return coord_x, coord_y
    return -1, -1


def movema(board, marker="X"):
    """Returneaza coordonatele pozitiei pe care am sa o completez"""
    linii = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
             [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
    linii_si_diagonale = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                          [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                          [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
                          ]
    colturi = [(0, 0), (0, 2), (2, 0), (2, 2)]
    mijloace = [(0, 1), (1, 0), (1, 2), (2, 1)]
    centru = [(1, 1)]
    oponent = marker_oponent(marker)
    coord_x, coord_y = doi_din_trei(board, marker)
    if coord_x > -1:
        return coord_x, coord_y
    nr_poz_completate = numar_pozitii_completate(board)
    # murati posibile pentru jucatorul care incepe
    if nr_poz_completate % 2 == 0:
        coord_x, coord_y = start_first(board, nr_poz_completate, linii, colturi, linii_si_diagonale,
                                       centru, mijloace, oponent, marker)
        if coord_x > -1:
            return coord_x, coord_y
    if nr_poz_completate % 2 != 0:
        coord_x, coord_y = start_second(board, nr_poz_completate, mijloace, centru, colturi,
                                        linii_si_diagonale, oponent, marker)
        if coord_x > -1:
            return coord_x, coord_y
    return -1, -1


def main():
    board = [
        [None, None, "X"],
        ["X", "X", "O"],
        ["O", "X", "O"]
    ]
    coord_x, coord_y = movema(board, marker="X")
    print(coord_x, coord_y)


if __name__ == '__main__':
    main()

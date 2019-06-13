from qm.qm import QM


if __name__ == '__main__':
    terms = [0, 2, 5, 6, 7, 8, 10, 12, 13, 14, 15]

    c = QM(terms)
    print(c.pis())
    print(c.epis())
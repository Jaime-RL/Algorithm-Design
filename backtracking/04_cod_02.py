import importlib

pcl = importlib.import_module("04_cod_07")


def voraz(p):
    if p.es_completa():
        return p
    else:
        p.amplía_voraz()
        return voraz(p)


if __name__ == "__main__":
    import sys

    fich = sys.argv[1] if len(sys.argv) > 1 else "04_dat_01.txt"
    p = pcl.Parcial_vrz(fich)
    aux = voraz(p)
    print(aux)
    print(aux.coste())

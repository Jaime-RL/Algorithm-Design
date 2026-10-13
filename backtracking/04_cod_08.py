import importlib
import sys

pcl = importlib.import_module("04_cod_11")

infinito = float("inf")


def lanza(p, mj=None, t_mj=infinito):
    fondo = p.es_completa()
    if fondo or t_mj < infinito:
        ct = p.cota()
        mejora = ct < t_mj
    else:
        # Es innecesario calcular la cota.
        ct = "—"
        mejora = True
    if mejora:
        if fondo:
            mj = p
            t_mj = ct
        else:
            for ap in p.amplía():
                mj, t_mj = lanza(ap, mj, t_mj)
    return mj, t_mj


if __name__ == "__main__":
    fich = sys.argv[1] if len(sys.argv) > 1 else "04_dat_01.txt"
    print(lanza(pcl.Parcial_ct(fich)))

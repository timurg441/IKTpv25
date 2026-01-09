import os
import glob

def leia_projektifailid(laiend):
    if not laiend.startswith("."):
        laiend = "." + laiend

        failid = []
    for fail in os.listdir("."):
        if os.path.isfile(fail) and fail.endswith(laiend):
            failid.append(fail)

    return failid

def analyysi_faili_sisu(failitee):
    try:
        with open(failitee, 'r', encoding='utf-8') as f:
            read = f.readlines()

            tulem = {
            "fail": failitee,
            "ridu_kokku": len(read),
            "tyhjad_read": 0,
            "TODO_loendur": 0,
            "FIXME_loendur": 0
        }
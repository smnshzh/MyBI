from django.shortcuts import render
import pandas as pd
from .models import *
def importSalers(requets):
    path = "Book4.csv"
    df = pd.read_csv(path)
    dfList = df.values.tolist()
    for item in dfList :
        Saler.objects.create(
            pcode = item[0],
            scode = item[1],
            name = item[2],
            superviseur = Superviseur.objects.get(id=int(item[3])),
            activity = SalerActivity.objects.get(id = int(item[4])),
            branch= Barache.objects.get(id=int(item[5]))
        )

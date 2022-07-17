from django.shortcuts import render

# Create your views here.


import joblib
import warnings
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import RobustScaler
warnings.filterwarnings("ignore")

# Create your views here.

def paginaprincipal(request):
    
    modelo = joblib.load('.\modelo\modelo_completo.joblib')
    if request.method == "GET":
        return render(
        request,
        'pagbase/index.html',
    )
    elif request.method == 'POST':
        MinTemp = request.POST['MinTemp'] 
        MaxTemp = request.POST['MaxTemp'] 
        Evaporation = request.POST['Evaporation'] 
        Sunshine = request.POST['Sunshine'] 
        WindGustSpeed = request.POST['WindGustSpeed'] 
        Hum9am = request.POST['Hum9am'] 
        Hum3pm = request.POST['Hum3pm'] 
        Pres9am = request.POST['Pres9am'] 
        Pres3pm = request.POST['Pres3pm'] 
        Cloud9am = request.POST['Cloud9am'] 
        Cloud3pm = request.POST['Cloud3pm']

        datos = [[MinTemp, MaxTemp, Evaporation, Sunshine, WindGustSpeed, Hum9am, Hum3pm, Pres9am, Pres3pm, Cloud9am, Cloud3pm]]

        scaled = preprocessing.RobustScaler()
        x_scaled = scaled.fit_transform(datos)
    
    salida = { 
        'predict': int(modelo.predict((datos)))
    }
    print(salida)
    print(x_scaled)
    print(datos)
    context={
        'titulo':'Weather prediction',
        'salida':salida

    }

    return render(
        request,
        'pagbase/index.html',
        context
    )
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 20:30:04 2018

@author: leali
"""

"""
programa para analisis de creditos
"""

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sea
# print ("el proceso de sejecuto correctamente")

"""
abrimos el archivo de credito de Alemania
"""

# url = 'C:\\Users\\leali\\Desktop\\EDX\\Principles\\Principles-of-Machine-Learning-Python-master\\Module2\\'
# archivo = 'German_credit.csv'

# datos = pd.read_csv(url + archivo, header= None)

# print(datos.head(20))

'''
Creamos un string con las columns y un diccionario con los valores de los indices para luego agregarlos al data frame
'''

columnas = ['customer_id',
                  'checking_account_status', 'loan_duration_mo', 'credit_history', 
                  'purpose', 'loan_amount', 'savings_account_balance', 
                  'time_employed_yrs', 'payment_pcnt_income','gender_status', 
                  'other_signators', 'time_in_residence', 'property', 'age_yrs',
                  'other_credit_outstanding', 'home_ownership', 'number_loans', 
                  'job_category', 'dependents', 'telephone', 'foreign_worker', 
                  'bad_credit']

datos.columns = columnas
valores_indice = [['checking_account_status', 
              {'A11' : '< 0 DM', 
               'A12' : '0 - 200 DM', 
               'A13' : '> 200 DM or salary assignment', 
               'A14' : 'none'}],
            ['credit_history',
            {'A30' : 'no credit - paid', 
             'A31' : 'all loans at bank paid', 
             'A32' : 'current loans paid', 
             'A33' : 'past payment delays', 
             'A34' : 'critical account - other non-bank loans'}],
            ['purpose',
            {'A40' : 'car (new)', 
             'A41' : 'car (used)',
             'A42' : 'furniture/equipment',
             'A43' : 'radio/television', 
             'A44' : 'domestic appliances', 
             'A45' : 'repairs', 
             'A46' : 'education', 
             'A47' : 'vacation',
             'A48' : 'retraining',
             'A49' : 'business', 
             'A410' : 'other' }],
            ['savings_account_balance',
            {'A61' : '< 100 DM', 
             'A62' : '100 - 500 DM', 
             'A63' : '500 - 1000 DM', 
             'A64' : '>= 1000 DM',
             'A65' : 'unknown/none' }],
            ['time_employed_yrs',
            {'A71' : 'unemployed',
             'A72' : '< 1 year', 
             'A73' : '1 - 4 years', 
             'A74' : '4 - 7 years', 
             'A75' : '>= 7 years'}],
            ['gender_status',
            {'A91' : 'male-divorced/separated', 
             'A92' : 'female-divorced/separated/married',
             'A93' : 'male-single', 
             'A94' : 'male-married/widowed', 
             'A95' : 'female-single'}],
            ['other_signators',
            {'A101' : 'none', 
             'A102' : 'co-applicant', 
             'A103' : 'guarantor'}],
            ['property',
            {'A121' : 'real estate',
             'A122' : 'building society savings/life insurance', 
             'A123' : 'car or other',
             'A124' : 'unknown-none' }],
            ['other_credit_outstanding',
            {'A141' : 'bank', 
             'A142' : 'stores', 
             'A143' : 'none'}],
             ['home_ownership',
            {'A151' : 'rent', 
             'A152' : 'own', 
             'A153' : 'for free'}],
            ['job_category',
            {'A171' : 'unemployed-unskilled-non-resident', 
             'A172' : 'unskilled-resident', 
             'A173' : 'skilled',
             'A174' : 'highly skilled'}],
            ['telephone', 
            {'A191' : 'none', 
             'A192' : 'yes'}],
            ['foreign_worker',
            {'A201' : 'yes', 
             'A202' : 'no'}],
            ['bad_credit',
            {2 : 1,
             1 : 0}]]

'''
hacer una inline function para joinnear el valor de cada ndice con su columna.
'''

for col in valores_indice:
    columna = col[0]
    dic = col[1]
    datos[columna] = [dic[x] for x in datos[columna]]
    
print(datos.head(5))

'''
buscamos la cantidad de malos creditos para empezar a hacer graficos
'''

totales = datos['bad_credit'].value_counts()

print(totales)

'''
hacemos boxplot de todas las variables numericas
'''

def boxplot_fx(col, col_fija,dataframe):
    for c in col:
        sea.boxplot(x=col_fija, y=c, data = dataframe)
        plt.xlabel(col_fija)
        plt.ylabel(c)
        plt.show()
        
col =  ['loan_duration_mo', 'loan_amount', 'payment_pcnt_income',
            'age_yrs', 'number_loans', 'dependents']

boxplot_fx(col, 'bad_credit',datos)        

'''
Ahora mostramos los totales de histogramas para las variables categoricas. para esto
generamos un contador para cada una teniendo en cuenta siempre el valor de buen/mal credito
'''

columnas_categoricas = ['checking_account_status', 'credit_history', 'purpose', 'savings_account_balance', 
                  'time_employed_yrs', 'gender_status', 'other_signators', 'property', 
                  'other_credit_outstanding', 'home_ownership', 'job_category', 'telephone', 
                  'foreign_worker']

for col in columnas_categoricas:
    datos['totales'] = 1
    mal_credito = datos[[col,'bad_credit','totales']].groupby([col,'bad_credit'], as_index = False).count()
    malo = mal_credito[mal_credito['bad_credit']==0][[col,'totales']]
    plt.bar(malo[col], malo.totales)
    plt.xticks(rotation = 90)
    plt.show()
    print(mal_credito, malo)
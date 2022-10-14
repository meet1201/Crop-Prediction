
import PySimpleGUI as sg
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


excel = pd.read_excel('crop.xlsx', header=0)
print(excel)
print(excel.shape)




le = preprocessing.LabelEncoder()
crop = le.fit_transform(list(excel["CROP"]))

NITROGEN = list(excel["NITROGEN"])
PHOSPHORUS = list(excel["PHOSPHORUS"])
POTASSIUM = list(excel["POTASSIUM"])
TEMPERATURE = list(excel["TEMPERATURE"])
HUMIDITY = list(excel["HUMIDITY"])
PH = list(excel["PH"])
RAINFALL = list(excel["RAINFALL"])

features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))
features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH,RAINFALL])

features = features.transpose()
print(features.shape)
print(crop.shape)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(features,crop)
sg.theme('TanBlue')
layout = [[sg.Text('                           Crop Prediction System', font=("Helvetica", 30), text_color='red')],
          # Defining the layout of the Graphical User Interface. It consist of some text, Buttons, and blanks to take Input.
          [sg.Text('Please enter the following details', font=("Arial", 22), text_color='black')],
          # We have defined the text size, font type, font size, blank size, colour of the text in the GUI.
          [sg.Text('1.Enter ratio of Nitrogen in the soil                                    :', font=("Arial", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('2.Enter ratio of Phosphorous in the soil                            :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('3.Enter ratio of Potassium in the soil                                 :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('4.Enter average Temperature value around the field        :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1)), sg.Text('*C', font=("Helvetica", 20))],
          [sg.Text('5.Enter average percentage of Humidity around the field :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1)), sg.Text('%', font=("Helvetica", 20))],
          [sg.Text('6.Enter PH value of the soil                                               :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('7.Enter average amount of Rainfall around the field         :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1)), sg.Text('mm', font=("Helvetica", 20))],
          [sg.Text(size=(50, 1), font=("Helvetica", 20), text_color='black', key='-OUTPUT1-')],
          [sg.Button('Submit', font=("Helvetica", 24)), sg.Button('Quit', font=("Helvetica", 24))]]
window = sg.Window('Crop Prediction V3.0', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    print(values[0])
    nitrogen_content = values[0]
    phosphorus_content = values[1]
    potassium_content = values[2]
    temperature_content = values[3]
    humidity_content = values[4]
    ph_content = values[5]
    rainfall = values[6]
    predict1 = np.array(
        [nitrogen_content, phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content,rainfall])  # Converting all the data that we collected from the user into a array form to make further predictions.
    print(predict1)
    predict1 = predict1.reshape(1,-1)
    print(predict1)
    predict1 = model.predict(predict1)
    print(predict1)
    crop_name = str()
    if predict1 == 0:
        crop_name = 'Apple'
    elif predict1 == 1:
        crop_name = 'Banana'
    elif predict1 == 2:
        crop_name = 'Blackgram'
    elif predict1 == 3:
        crop_name = 'Chickpea'
    elif predict1 == 4:
        crop_name = 'Coconut'
    elif predict1 == 5:
        crop_name = 'Coffee'
    elif predict1 == 6:
        crop_name = 'Cotton'
    elif predict1 == 7:
        crop_name = 'Grapes'
    elif predict1 == 8:
        crop_name = 'Jute'
    elif predict1 == 9:
        crop_name = 'Kidneybeans'
    elif predict1 == 10:
        crop_name = 'Lentil'
    elif predict1 == 11:
        crop_name = 'Maize'
    elif predict1 == 12:
        crop_name = 'Mango'
    elif predict1 == 13:
        crop_name = 'Mothbeans'
    elif predict1 == 14:
        crop_name = 'Mungbeans'
    elif predict1 == 15:
        crop_name = 'Muskmelon'
    elif predict1 == 16:
        crop_name = 'Orange'
    elif predict1 == 17:
        crop_name = 'Papaya'
    elif predict1 == 18:
        crop_name = 'Pigeonpeas'
    elif predict1 == 19:
        crop_name = 'Pomegranate'
    elif predict1 == 20:
        crop_name = 'Rice'
    elif predict1 == 21:
        crop_name = 'Watermelon'





    window['-OUTPUT1-'].update('The Suitable crop to grow is : ' + crop_name)


window.close()

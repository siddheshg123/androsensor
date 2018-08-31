"""activity_sensor"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from gmplot import gmplot

DATA_FRAME = pd.read_csv('Sensor_record_20180807_185126_AndroSensor.csv', sep=',', header=1)
DATA_FRAME = DATA_FRAME.set_index('Time since start in ms ')

LAT1 = DATA_FRAME['LOCATION Latitude : ']
LON1 = DATA_FRAME['LOCATION Longitude : ']
G_MAP1 = gmplot.GoogleMapPlotter(float(LAT1.iloc[1]), float(LON1.iloc[1]), 13)
G_MAP1.plot(LAT1, LON1, 'cornflowerblue', edge_width=2.5)
G_MAP1.draw("/home/kpit/Downloads/map3.html")


LIGHT_DATAFRAME = DATA_FRAME['LIGHT (lux)']
plt.plot(LIGHT_DATAFRAME)
COUNT_LIGHTS = 0
for i in LIGHT_DATAFRAME:
    if i >= 80:
        COUNT_LIGHTS = COUNT_LIGHTS+1
print("NUMBER OF STREET LIGHTS:")
print(int(COUNT_LIGHTS/30))
COUNT_TREES = 0
for i in LIGHT_DATAFRAME:
    if i <= 40:
        COUNT_TREES += 1
print("NUMBER OF COCONUT TREES:")
print(int(COUNT_TREES)/6)

SOUND_DATAFRAME = DATA_FRAME['SOUND LEVEL (dB)']
plt.plot(SOUND_DATAFRAME)
print("MAXIMUM SOUND INTENSITY:")
MAX_SOUND = max(SOUND_DATAFRAME)
print(max(SOUND_DATAFRAME))
MEAN_SOUND = abs(SOUND_DATAFRAME).mean()
print("MEAN SOUND INTENSITY:")
print(MEAN_SOUND)
if MAX_SOUND < 40:
    print("INCREASE VOLUME TO 45 db")
elif MAX_SOUND > 40 and MAX_SOUND < 60:
    print("INCREASE VOLUME TO 65 dB")
else:
    print("INCREASE VOLUME TO 80 dB")


MAGNETIC = DATA_FRAME['MAGNETIC FIELD X (μT)']
MX = np.array([])
MY = np.array([])
MZ = np.array([])
for i in range(len(DATA_FRAME['MAGNETIC FIELD X (μT)'])):
    MX = np.append(MX, float(DATA_FRAME['MAGNETIC FIELD X (μT)'][i].tolist()))
    MY = np.append(MY, float(DATA_FRAME['MAGNETIC FIELD Y (μT)'][i].tolist()))
    MZ = np.append(MZ, float(DATA_FRAME['MAGNETIC FIELD Z (μT)'][i].tolist()))
MT = np.sqrt(np.square(MX)+np.square(MY)+np.square(MZ))
plt.plot(MT)
print("MAXIMUM MAGNETIC FIELD:")
print(max(MT))
print("MEAN MAGNETIC INTENSITY:")
MEAN_MAGNETIC = abs(MT).mean()
print(MEAN_MAGNETIC)
DATA_FRAME1 = DATA_FRAME.loc[DATA_FRAME['MAGNETIC FIELD X (μT)'] >= 30]
LAT = DATA_FRAME1['LOCATION Latitude : ']
LON = DATA_FRAME1['LOCATION Longitude : ']
G_MAP2 = gmplot.GoogleMapPlotter(float(LAT.iloc[1]), float(LON.iloc[1]), 13)
G_MAP2.heatmap(LAT, LON, radius=25, opacity=0.6, dissipating=True, threshold=10)
G_MAP2.draw("/home/kpit/Downloads/magnetic_intensity.html")


AX = np.array([])
AY = np.array([])
AZ = np.array([])
for i in range(len(DATA_FRAME['LINEAR ACCELERATION Y (m/s²)'])):
    AX = np.append(AX, float(DATA_FRAME['LINEAR ACCELERATION X (m/s²)'][i].tolist()))
    AY = np.append(AY, float(DATA_FRAME['LINEAR ACCELERATION Y (m/s²)'][i].tolist()))
    AZ = np.append(AZ, float(DATA_FRAME['LINEAR ACCELERATION Z (m/s²)'][i].tolist()))
A_TOT = np.sqrt(np.square(AX)+np.square(AY)+np.square(AZ))
print("AVERAGE EUCLIDIAN ACCELERATION:")
print(A_TOT.mean())
plt.plot(A_TOT)

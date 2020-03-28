import xml.etree.ElementTree as XET
import pandas as pd

df = pd.DataFrame(columns = ['time', 'lng', 'lat', 'magnitude', 'depth' ])

for i in range(1990,2020):
    tree = XET.parse('data/CWB-EQ-Catalog-' + str(i) + '.xml')
    root = tree.getroot()
    for dataset in root.iter('dataset'):
        for catalog in dataset.iter('catalog'):
            for earthquakeinfo in dataset.iter('earthquakeinfo'):
                # 1990-01-01T21:47:59+08:00
                time = earthquakeinfo.find('originTime').text.replace('T', ' ').split('+')[0] 
                lng = earthquakeinfo.find('epicenter').find('epicenterLon').text
                lat = earthquakeinfo.find('epicenter').find('epicenterLat').text
                magnitude = earthquakeinfo.find('magnitude').find('magnitudeValue').text
                depth = earthquakeinfo.find('depth').text
                quake = pd.DataFrame({'time':[time], 'lng': [lng], 'lat':[lat], 'magnitude': [magnitude], 'depth': [depth]})
                df = pd.concat([df, quake], axis=0, join='outer', ignore_index = True)

df.to_csv('Earthquakes1990-2019.csv')
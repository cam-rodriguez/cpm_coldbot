import pandas as pd
import os
import numpy as np
import datetime





def splitdate(df):
    df[['inc_date','inc_time']] = df['incident_date'].str.split('T', expand=True)
    df[['dth_date', 'dth_time']] = df['death_date'].str.split('T', expand=True)


splitdate(df)

# generating things for text
    caselist = rows['casenumber']
    
    # data table
    # data cleaning that could literally be done anywhere else but for some reason i'm doing it here ugh
    rows['age'] = rows['age'].astype('str')
    rows['age'] = rows['age'].str.replace('.0','',regex=True)

    rows['latino'] = rows['latino'].astype('str')
    rows['latino'] = rows['latino'].str.replace('False','',regex=True)
    rows['latino'] = rows['latino'].str.replace('True','Latino',regex=True)

    rows['incident_zip'] = rows['incident_zip'].astype('str')
    rows['incident_zip'] = rows['incident_zip'].str.replace('.0','',regex=False)


    rows['inc_loc'] = rows['incident_street'].str.upper() + ', ' + rows['incident_city'] + ', IL ' + rows['incident_zip']
    rows['inc_loc'] = rows['inc_loc'].str.title()


    rows['maploc'] = rows['inc_loc'].str.replace(' ','+',regex=True)
    gmaps_start = "https://google.com/maps/place/"
    rows['gmaps_link'] = "<" + gmaps_start + rows['maploc'] + "/ | here >"

    # rows['gmaps_link'] = f'<{gmaps_start}/{maploc}/ | >'

    # concatenate to get a big string
    rows_trunc = rows[['casenumber','inc_date','dth_date','age', 'incident_city', 'gender','race','latino','primarycause','secondarycause','inc_loc','chi_ward','chi_commarea','residence_city','gmaps_link']]
    
    # make it a string list
    rows_trunc['stringy'] = "• *Case number " + rows_trunc['casenumber'] + "* — a " + rows_trunc['age'] + "-year-old " + rows_trunc['latino'] + " " + rows_trunc['race'] + " " + rows_trunc['gender'].str.lower() + " in " + rows_trunc['incident_city'].str.title() + ". \n The determined cause of death is " + rows_trunc['primarycause'] + " and " + rows_trunc['secondarycause'] + ". The death date was *" + rows_trunc['dth_date'] + "* and the incident that led to their death was on *" + rows_trunc['inc_date'] + "* at " + rows_trunc['inc_loc'] + ". 📍 view incident location " + rows_trunc['gmaps_link'] + ". \n"
    stringy_list = rows_trunc['stringy']

df.to_csv('./data/today_colddeaths.csv')

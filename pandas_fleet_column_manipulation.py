import pandas as pd
#from pd import dataframe

#import pandas.io.data
import numpy
import csv

# Environment Settings
myFolderPath = 'C:\\Airport Project\WebScrape\\'
git = 'C:\\Airport Project\Python-pandas-data-manipulation\\'
OutputPath = git + 'csv\\'
Cargo = myFolderPath + 'Cargo\\'
Legacy = myFolderPath + 'LEGACY_03_04_2017\\'
MidMajor = myFolderPath + 'Mid_Major_03_04_2017\\'
Regional = myFolderPath + 'Regional\\'

fedex_fleet_path = Cargo + 'fedex_fleet.csv'
ups_fleet_path = Cargo + 'ups_fleet.csv'
alaska_fleet_path = Legacy + 'alaska_fleet.csv'
american_fleet_path = Legacy + 'american_fleet.csv'
delta_fleet_path = Legacy + 'delta_fleet.csv'
hawaiian_fleet_path = Legacy + 'hawaiian_fleet.csv'
united_fleet_path = Legacy + 'united_fleet.csv'
allegiant_fleet_path = MidMajor + 'allegiant_fleet.csv'
frontier_fleet_path = MidMajor + 'frontier_fleet.csv'
jetblue_fleet_path = MidMajor + 'jetblue_fleet.csv'
southwest_fleet_path = MidMajor + 'southwest_fleet.csv'
spirit_fleet_path = MidMajor + 'spirit_fleet.csv'
suncountry_fleet_path = MidMajor + 'suncountry_fleet.csv'
virgin_fleet_path = MidMajor + 'virgin_fleet.csv'
airwisco_fleet_path = Regional + 'airwisco_fleet.csv'
compass_fleet_path = Regional + 'compass_fleet.csv'
endeavor_fleet_path = Regional + 'endeavor_fleet.csv'
envoy_fleet_path = Regional + 'envoy_fleet.csv'
expressjet_fleet_path = Regional + 'expressjet_fleet.csv'
gojet_fleet_path = Regional + 'gojet_fleet.csv'
horizon_fleet_path = Regional + 'horizon_fleet.csv'
mesa_fleet_path = Regional + 'mesa_fleet.csv'
piedmont_fleet_path = Regional + 'piedmont_fleet.csv'
psa_fleet_path = Regional + 'psa_fleet.csv'
republic_fleet_path = Regional + 'republic_fleet.csv'
skywest_fleet_path = Regional + 'skywest_fleet.csv'
transstates_fleet_path = Regional + 'transstates_fleet.csv'

fleet_output = OutputPath + 'fleet.csv'

#read a fleet csv and separate into columns
fedex_fleet = pd.read_csv(fedex_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
fedex_fleet['Airline'] = 'FedEx'
#code below is the option to remove " after every _csv read 
#fedex_fleet['Plane'] = fedex_fleet['Plane'].str.replace('"','')
#fedex_fleet['Fleet_Count'] = fedex_fleet['Fleet_Count'].str.replace('"','')
print(fedex_fleet)

ups_fleet = pd.read_csv(ups_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
ups_fleet['Airline'] = 'UPS'
print(ups_fleet)

alaska_fleet = pd.read_csv(alaska_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
alaska_fleet['Airline'] = 'Alaska'
print(alaska_fleet)

american_fleet = pd.read_csv(american_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
american_fleet['Airline'] = 'American'
print(american_fleet)

delta_fleet = pd.read_csv(delta_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
delta_fleet['Airline'] = 'Delta'
print(delta_fleet)

hawaiian_fleet = pd.read_csv(hawaiian_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
hawaiian_fleet['Airline'] = 'Hawaiian'
print(hawaiian_fleet)

united_fleet = pd.read_csv(united_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
united_fleet['Airline'] = 'United'
print(united_fleet)

allegiant_fleet = pd.read_csv(allegiant_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
allegiant_fleet['Airline'] = 'Allegiant'
print(allegiant_fleet)

frontier_fleet = pd.read_csv(frontier_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
frontier_fleet['Airline'] = 'Frontier'
print(frontier_fleet)

jetblue_fleet = pd.read_csv(jetblue_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
jetblue_fleet['Airline'] = 'JetBlue'
print(jetblue_fleet)

southwest_fleet = pd.read_csv(southwest_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
southwest_fleet['Airline'] = 'Southwest'
print(southwest_fleet)

spirit_fleet = pd.read_csv(spirit_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
spirit_fleet['Airline'] = 'Spirit'
print(spirit_fleet)

suncountry_fleet = pd.read_csv(suncountry_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
suncountry_fleet['Airline'] = 'SunCountry'
print(suncountry_fleet)

virgin_fleet = pd.read_csv(virgin_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
virgin_fleet['Airline'] = 'Virgin'
print(virgin_fleet)

airwisco_fleet = pd.read_csv(airwisco_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
airwisco_fleet['Airline'] = 'AirWisco'
print(airwisco_fleet)

compass_fleet = pd.read_csv(compass_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
compass_fleet['Airline'] = 'Compass'
print(compass_fleet)

endeavor_fleet = pd.read_csv(endeavor_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
endeavor_fleet['Airline'] = 'Endeavor'
print(endeavor_fleet)

envoy_fleet = pd.read_csv(envoy_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
envoy_fleet['Airline'] = 'Envoy'
print(envoy_fleet)

expressjet_fleet = pd.read_csv(expressjet_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
expressjet_fleet['Airline'] = 'ExpressJet'
print(expressjet_fleet)

gojet_fleet = pd.read_csv(gojet_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
gojet_fleet['Airline'] = 'GoJet'
print(gojet_fleet)

horizon_fleet = pd.read_csv(horizon_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
horizon_fleet['Airline'] = 'Horizon'
print(horizon_fleet)

mesa_fleet = pd.read_csv(mesa_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
mesa_fleet['Airline'] = 'Mesa'
print(mesa_fleet)

piedmont_fleet = pd.read_csv(piedmont_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
piedmont_fleet['Airline'] = 'Piedmont'
print(piedmont_fleet)

psa_fleet = pd.read_csv(psa_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
psa_fleet['Airline'] = 'PSA'
print(psa_fleet)

republic_fleet = pd.read_csv(republic_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
republic_fleet['Airline'] = 'Republic'
print(republic_fleet)

skywest_fleet = pd.read_csv(skywest_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
skywest_fleet['Airline'] = 'Skywest'
print(skywest_fleet)

transstates_fleet = pd.read_csv(transstates_fleet_path,sep=': ',names=['Plane','Fleet_Count'],engine='python',skiprows=1)
transstates_fleet['Airline'] = 'TransStates'
print(transstates_fleet)

##########################3
#df = pd.concat([fedex_fleet,delta_fleet],ignore_index=True)
df = pd.concat([fedex_fleet,ups_fleet,alaska_fleet,american_fleet,delta_fleet,hawaiian_fleet,united_fleet,allegiant_fleet,frontier_fleet,jetblue_fleet,southwest_fleet,spirit_fleet,suncountry_fleet,virgin_fleet,airwisco_fleet,compass_fleet,endeavor_fleet,envoy_fleet,expressjet_fleet,gojet_fleet,horizon_fleet,mesa_fleet,piedmont_fleet,psa_fleet,republic_fleet,skywest_fleet,transstates_fleet],ignore_index=True)
df['Plane'] = df['Plane'].str.replace('"','')
df['Fleet_Count'] = df['Fleet_Count'].str.replace('"','')
print(df)
#df = pd.concat([df,delta_fleet]) #for some reason Delta is the only data that has the fleet counts as an INT
#pd.dataframe.concat([fedex_fleet,ups_fleet,alaska_fleet,american_fleet,delta_fleet,hawaiian_fleet,united_fleet,allegiant_fleet,frontier_fleet,jetblue_fleet,southwest_fleet,spirit_fleet,suncountry_fleet,virgin_fleet,airwisco_fleet,compass_fleet,endeavor_fleet,envoy_fleet,expressjet_fleet,gojet_fleet,horizon_fleet,mesa_fleet,piedmont_fleet,psa_fleet,republic_fleet,skywest_fleet,transstates_fleet],ignore_index=True)


##writing dataframe to csv (to be imported into postgres)
df.to_csv(OutputPath+ '\\fleet.csv')
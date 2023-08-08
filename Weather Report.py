import pandas as pd
data = pd.read_csv ( r"C:\Users\Shankar V\OneDrive\Desktop\Py\1. Weather Data.csv" )
data  # Assuming you want to print the data to check its contents
data.head()
data.shape
data.index
data.columns
data.dtypes
data['Weather'].unique() #Wind Speed_km/h 
data.nunique()
data.count() #or can use data.notnull().sum()
data['Weather'].value_counts()
data.info()
data.nunique()
data['Wind Speed_km/h'].nunique()
data.Weather.value_counts()
#----#--------
#2

count_clear = (data["Weather"] == "Clear").sum() #ChatGPT
print(count_clear)

data.head(2)
data[data.Weather == 'Clear']  #Declaration as Weather is Column name
data[data['Weather'] == 'Clear']  #Declaration as Weather is a list

data.groupby("Weather").get_group("Clear")
#----#-------
 #3

count_wind = (data["Wind Speed_km/h"] == 4).sum()
print(count_wind)

data.groupby("Wind Speed_km/h").get_group(4)  #Using Groupby

data[data['Wind Speed_km/h'] == 4]
#----#----#----#--------
#4

data.isnull().sum()
#data[data.nunique() - data.count()]

#----#-----------
#5 

data.rename(columns={'Weather' : 'Weather Condition'})        #To change the columnname temporarily
data.head()
data.rename(columns={'Weather' : 'Weather Condition'}, inplace=True)        #To change the columnname permanently

#----#-----------
#6

data.head()
data.Visibility_km.mean()

###----#---------
#7
data.head(3)
data.Press_kPa.std()

##----#----#--------
#8
data.head(4)
data['Rel Hum_%'].var()

#----#----#----#-----
#9
count_snow = (data['Weather Condition']=='Snow').sum()
print(count_snow)

data.groupby("Weather Condition").get_group('Snow')

data[data['Weather Condition']=='Snow']    #[] are used when the columnname is separated with a space and . is used when the column name is separated by just an underscore

data[data['Weather Condition'].str.contains('Snow')]    #Used to represent all the column elements that contains the string 'snow' like snow showers too

data[data['Weather Condition'].str.contains('Snow')].head(10) #Used to represent the first 10 columns
data[data['Weather Condition'].str.contains('Snow')].tail(10) #Used to represent the last 10 columns

#----#----#----#----#----#-------
#10
data.head()
data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]   #When the common of 2 conditions are to be met '&' is used

#----#----#----#----#-----------
#11

data.head()
#data.groupby('Weather Condition').mean()

#----#----#----#----#--------
#12

data.head()
data.groupby('Weather Condition').min()
data.groupby('Weather Condition').max()

#----#----#----#----#-------
#13

data.head()
data[data['Weather Condition']=='Fog']

#----#----#----#----#-----------
#14
 
data.head()
data[(data['Weather Condition']=='Clear') | (data['Visibility_km'] > 40)]

#----#----#----#----#----#----#-----
#15

data.head()
data[ (data['Weather Condition']=='Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km']>40)]
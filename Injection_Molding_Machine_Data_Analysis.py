# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 14:32:36 2021

@author: CDarden
"""

###########################          WORKING JOURNAL FOR PROJECT           #####################################
# 25OCT21
# created GitHub account 
# created GitHub repository ISE-535-Data-Project 
# created local directory C:\Users\cdarden\Desktop\Personal BS\ISE 535\Injection_Molding_Project 
# changed terminal directory to point to local directory 
# initialized local directory as a git repository 
# added files in local directory to git repository 
# specified and added remote repository URL 
# pushed code in local repository to github 
# studied .XML file format
# worked on main code to parse data. Formatted parameter database page - *need to combine strings from multiple cells to read header, or strip rows and re-add header*
# how to read XML with pandas = https://pandas.pydata.org/docs/reference/api/pandas.read_xml.html
# 'C:/Users/cdarden/Desktop/Personal BS/ISE 535/Injection_Molding_Project/dataSample1.XML'
# 26OCT21 
# no luck opening XML files with pandas, trying .csv
# works great, must delete unnecesary rows and append header row to top. Constructed header row.
# trying to use pd.concat to add header row to formatted file
# found that header file must be reconstructed to preserve integrity in .csv format
# 27OCT21
# reconstructed header file
# contacted Dr. S. about concatenation issues. Going to stop using concatenate and try something else. Spent a couple of hours so far trying to add the header to the file
# https://www.codegrepper.com/code-examples/python/how+to+add+header+in+csv+file+in+python
# at some point during a write, I deleted all the data from my .csv file. That causes problems. 
# found a way to format the original file, then write a new file (dataSample1formatted.csv) with the headerList. 
# submitted project proposal
# 28OCT21
# dropped unused columns from df and set Cycle column as index
# wrote code for average cycle time with correct formatting
# pip installed dash, reading Dash tutorials
# completed database table for part 11841170001 (test part)
# 29OCT21
# worked on building dashboard code, Dash tutorials, web development
# 3NOV21
# continued building dashboard code, Dash tutorials, web development
# 11NOV21 
# learned about hsl values for css colors
# tweaked on dash format, layout and colors
# 16NOV21
# I learned a lot from exam 3 that hopefully I can use here
# Worked on main code to populate variables from databases, looping through dataframe to look for bad cycles
# 17NOV21
# worked on main code, same as yesterday. Using comparison columns to generate Good/Bad cycle dataframe
# success at pulling info for bad cycles due to 'Cycle time' :)
# 18NOV21
# continued buliding up code for all defects
# got main code parsing all required info, now need to pass that info to dashboard
# https://stackoverflow.com/questions/61423054/plotly-dash-show-variable-value-in-output
# 


'''
 access exported file, create new .csv file with correct header and dataframe formatting
'''
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objects as go



header = pd.read_csv('C:/Users/cdarden/Desktop/Personal BS/ISE 535/Injection_Molding_Project/headerRow.csv')
headerList = list(header)

file = pd.read_csv('C:/Users/cdarden/Desktop/Personal BS/ISE 535/Injection_Molding_Project/machineData.csv') 
df = file.drop([0,1,2,3,4,5,6], axis=0)      # drops the first 7 rows from the file for formatting purposes

runStartDate = df.iloc[7]['Export actual-value cycles onto USB stick']
runStartTime = df.iloc[7][ 'Unnamed: 1']
runStopDate = df.iloc[len(df)-6]['Export actual-value cycles onto USB stick']
runStopTime = df.iloc[len(df)-6][ 'Unnamed: 1']

df.columns = headerList      # creates a new csv file, formatted, with the header row appended
df.to_csv('C:/Users/cdarden/Desktop/Personal BS/ISE 535/Injection_Molding_Project/machineDataFormatted.csv')

df = pd.read_csv('C:/Users/cdarden/Desktop/Personal BS/ISE 535/Injection_Molding_Project/machineDataFormatted.csv', index_col=('Cycle')) 
df.drop(df.columns[df.columns.str.contains('Unnamed',case = False)],axis = 1, inplace = True)       # drops 'Unnamed' column from df
'''
average cycle time
'''
aveCycleTime = float("{:.2f}".format(df["Cycle time"].mean()))
#print (aveCycleTime)                    # key metric to be displayed on dashboard
'''
size of dataset (number of cycles)
'''
dfCycles = df.shape[0]

'''
access parameterDB.csv
'''
parameters = pd.read_csv('C:/Users/cdarden/Desktop/Personal BS/ISE 535/Injection_Molding_Project/parameterDB.csv')
'''
input part number (testing)
'''
partNum = input("Enter Part Number: ")   # as type string
'''
read parameter database 
'''
parameterDB = pd.read_csv('C:/Users/cdarden/Desktop/Personal BS/ISE 535/Injection_Molding_Project/parameterDB.csv')  # contains parameter set for all part numbers

'''
make a new df containing parameter set if partNum in Part Number column of parameterDB, this dataframe contains only the parameter ranges of the PN

'''
pnList = [partNum]
pnParamDB = parameterDB[parameterDB['Part Number'].isin(pnList)]

'''
reduce the two dataframes down to only the columns of interest for speed
'''


pnParamDB = pnParamDB[['Cycle time','Inj time','Plast time','Melt cushion','Switch MeltPr','Max MeltPr','SCF dosing','SCF inj open time','SCF OP drop','Max CavPr1','Barrel Z4']]
df = df[['Cycle time','Inj time','Plast time','Melt cushion','Switch MeltPr','Max MeltPr','SCF dosing','SCF inj open time','SCF OP drop','Max CavPr1','Barrel Z4']]


'''
set monitered parameters in pnParamDB as max/min for PN
'''
cycleTimeMax= pnParamDB.iloc[0].at['Cycle time']
cycleTimeMin= pnParamDB.iloc[1].at['Cycle time']

injTimeMax= pnParamDB.iloc[0].at['Inj time']
injTimeMin= pnParamDB.iloc[1].at['Inj time']

plastTimeMax= pnParamDB.iloc[0].at['Plast time']
plastTimeMin= pnParamDB.iloc[1].at['Plast time']

meltCushMax= pnParamDB.iloc[0].at['Melt cushion']
meltCushMin= pnParamDB.iloc[1].at['Melt cushion']

switchMPMax= pnParamDB.iloc[0].at['Switch MeltPr']
switchMPMin= pnParamDB.iloc[1].at['Switch MeltPr']

maxMPMax= pnParamDB.iloc[0].at['Max MeltPr']
maxMPMin= pnParamDB.iloc[1].at['Max MeltPr']

scfDosingMax= pnParamDB.iloc[0].at['SCF dosing']
scfDosingMin= pnParamDB.iloc[1].at['SCF dosing']

scfInjOpenTimeMax= pnParamDB.iloc[0].at['SCF inj open time']
scfInjOpenTimeMin= pnParamDB.iloc[1].at['SCF inj open time']

scfOpDropMax= pnParamDB.iloc[0].at['SCF OP drop']
scfOpDropMin= pnParamDB.iloc[1].at['SCF OP drop']

maxCavPressMax= pnParamDB.iloc[0].at['Max CavPr1']
maxCavPressMin= pnParamDB.iloc[1].at['Max CavPr1']

barrelZ4Max= pnParamDB.iloc[0].at['Barrel Z4']
barrelZ4Min= pnParamDB.iloc[1].at['Barrel Z4']

'''
check each column of df, comparing values to monitered parameters, creating Good/Bad columns
'''

maxCTGBColumn = np.where(df["Cycle time"] <= cycleTimeMax, 'Good', 'Bad' )
minCTGBColumn = np.where(df["Cycle time"] >= cycleTimeMin, 'Good', 'Bad' )
ct_comparison_column = np.where(maxCTGBColumn == minCTGBColumn, 'Good', 'Bad')

maxITGBColumn = np.where(df["Inj time"] <= injTimeMax, 'Good', 'Bad' )
minITGBColumn = np.where(df["Inj time"] >= injTimeMin, 'Good', 'Bad' )
it_comparison_column = np.where(maxITGBColumn == minITGBColumn, 'Good', 'Bad')

maxPTGBColumn = np.where(df["Plast time"] <= plastTimeMax, 'Good', 'Bad' )
minPTGBColumn = np.where(df["Plast time"] >= plastTimeMin, 'Good', 'Bad' )
pt_comparison_column = np.where(maxPTGBColumn == minPTGBColumn, 'Good', 'Bad')

maxMCGBColumn = np.where(df["Melt cushion"] <= meltCushMax, 'Good', 'Bad' )
minMCGBColumn = np.where(df["Melt cushion"] >= meltCushMin, 'Good', 'Bad' )
mc_comparison_column = np.where(maxMCGBColumn == minMCGBColumn, 'Good', 'Bad')

maxSMPGBColumn = np.where(df["Switch MeltPr"] <= switchMPMax, 'Good', 'Bad' )
minSMPGBColumn = np.where(df["Switch MeltPr"] >= switchMPMin, 'Good', 'Bad' )
smp_comparison_column = np.where(maxSMPGBColumn == minSMPGBColumn, 'Good', 'Bad')

maxMMPGBColumn = np.where(df["Max MeltPr"] <= maxMPMax, 'Good', 'Bad' )
minMMPGBColumn = np.where(df["Max MeltPr"] >= maxMPMin, 'Good', 'Bad' )
mmp_comparison_column = np.where(maxMMPGBColumn == minMMPGBColumn, 'Good', 'Bad')

maxSCFDGBColumn = np.where(df["SCF dosing"] <= scfDosingMax, 'Good', 'Bad' )
minSCFDGBColumn = np.where(df["SCF dosing"] >= scfDosingMin, 'Good', 'Bad' )
scfd_comparison_column = np.where(maxSCFDGBColumn == minSCFDGBColumn, 'Good', 'Bad')

maxSCFIOGBColumn = np.where(df["SCF inj open time"] <= scfInjOpenTimeMax, 'Good', 'Bad' )
minSCFIOGBColumn = np.where(df["SCF inj open time"] >= scfInjOpenTimeMin, 'Good', 'Bad' )
scfio_comparison_column = np.where(maxSCFIOGBColumn == minSCFIOGBColumn, 'Good', 'Bad')

maxSCFODGBColumn = np.where(df["SCF OP drop"] <= scfOpDropMax, 'Good', 'Bad' )
minSCFODGBColumn = np.where(df["SCF OP drop"] >= scfOpDropMin, 'Good', 'Bad' )
scfod_comparison_column = np.where(maxSCFODGBColumn == minSCFODGBColumn, 'Good', 'Bad')

maxMCPGBColumn = np.where(df["Max CavPr1"] <= maxCavPressMax, 'Good', 'Bad' )
minMCPGBColumn = np.where(df["Max CavPr1"] >= maxCavPressMin, 'Good', 'Bad' )
mcp_comparison_column = np.where(maxMCPGBColumn == minMCPGBColumn, 'Good', 'Bad')

maxBZ4GBColumn = np.where(df["Barrel Z4"] <= barrelZ4Max, 'Good', 'Bad' )
minBZ4GBColumn = np.where(df["Barrel Z4"] >= barrelZ4Min, 'Good', 'Bad' )
bz4_comparison_column = np.where(maxBZ4GBColumn == minBZ4GBColumn, 'Good', 'Bad')

'''
rewrite df with good/bad 
'''
df['Cycle time'] = ct_comparison_column.tolist()
df['Inj time'] = it_comparison_column.tolist()
df['Plast time'] = pt_comparison_column.tolist()
df['Melt cushion'] = mc_comparison_column.tolist()
df['Switch MeltPr'] = smp_comparison_column.tolist()
df['Max MeltPr'] = mmp_comparison_column.tolist()
df['SCF dosing'] = scfd_comparison_column.tolist()
df['SCF inj open time'] = scfio_comparison_column.tolist()
df['SCF OP drop'] = scfod_comparison_column.tolist()
df['Max CavPr1'] = mcp_comparison_column.tolist()
df['Barrel Z4'] = bz4_comparison_column.tolist()

'''
analyze df for Bad cycles caused by each parameter
'''
df = df.astype(str)

df2 = df[df['Cycle time'].str.contains('Bad')]   
badCyclesCT =  df2.shape[0]    

df3 = df[df['Inj time'].str.contains('Bad')]   
badCyclesIT =  df3.shape[0]   

df4 = df[df['Plast time'].str.contains('Bad')]   
badCyclesPT =  df4.shape[0]

df5 = df[df['Melt cushion'].str.contains('Bad')]   
badCyclesMC =  df5.shape[0]

df6 = df[df['Switch MeltPr'].str.contains('Bad')]   
badCyclesSMP =  df6.shape[0]

df7 = df[df['Max MeltPr'].str.contains('Bad')]   
badCyclesMMP =  df7.shape[0]

df8 = df[df['SCF dosing'].str.contains('Bad')]   
badCyclesSCFD =  df8.shape[0]

df9 = df[df['SCF inj open time'].str.contains('Bad')]   
badCyclesSCFOT =  df9.shape[0]

df10 = df[df['SCF OP drop'].str.contains('Bad')]   
badCyclesSCFOD =  df10.shape[0]

df11 = df[df['Max CavPr1'].str.contains('Bad')]   
badCyclesMCP =  df11.shape[0]

df12 = df[df['Barrel Z4'].str.contains('Bad')]   
badCyclesBZ4 =  df12.shape[0]

'''
combine defect dfs into one df for parsing
'''
frames = [df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]

dfDefects = pd.concat(frames)

dfDefects = dfDefects.astype(str)


dfDefects.sort_values('Cycle', inplace = True)  # sorting by Cycle
 
# dropping ALL duplicate values

dfDefects = dfDefects[~dfDefects.index.duplicated(keep='first')]

totalDefects = dfDefects.shape[0]

'''
Yield Calculation
'''
machineYield = (1- (totalDefects / dfCycles))*100
machineYield = float("{:.2f}".format(machineYield))

'''
print metrics
'''
print(f"Part Number: {partNum}")
print("Part Name: ")
print(f"Run Start: {runStartDate} {runStartTime}")
print(f"Run Stop: {runStopDate} {runStopTime}")
print(f"Total Cycles: {dfCycles}")
print(f"Average Cycle Time: {aveCycleTime} sec")
print(f"Yield: {machineYield} %")

'''
Dash code (for dashboard)
'''

app = dash.Dash()       

# define HTML component
app.layout = html.Div (children = [html.Div("Injection Molding Data Analysis", style = {
                                                        "color" : "black",
                                                        "font-size" : "50px",
                                                        "background-color" : "DimGrey",
                                                        "border-style" : "solid",
                                                        "text-align" : "center",
                                                        "display" : "inline-block",
                                                        "height" : "70px",
                                                        "width" : "80%"
                                                        }),
                
                        html.Div("LOGO", style = {
                                                        "color" : "white",
                                                        "font-size" : "50px",
                                                        "background-color" : "darkblue",
                                                        "border-style" : "solid",
                                                        "text-align" : "center",
                                                        "display" : "inline-block",
                                                        "height" : "70px",
                                                        "width" : "19%"
                                                        }),
                        
                       
                        html.Div("Part Number:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "DarkOliveGreen",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "25%"
                                                        }),
                        
                        html.Div("Part Name:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "hsl(184, 6%, 72%)",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "33%"
                                                        }),
                                                
                        html.Div("Run Start:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "DarkOliveGreen",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "33%"
                                                        }),
                        html.Div("Run Stop:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "hsl(184, 6%, 72%)",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "25%"
                                                        }),
                        html.Div("Total Cycles:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "DarkOliveGreen",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "33%"
                                                        }),
                        html.Div("Average Cycle Time:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "hsl(184, 6%, 72%)",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "33%"
                                                        }),
                        html.Div("Yield:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "DarkOliveGreen",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "40px",
                                                        "width" : "25%"
                                                        }),
                        html.Div("Defects:", style = {
                                                        "color" : "black",
                                                        "font-size" : "30px",
                                                        "background-color" : "Khaki",
                                                        "border-style" : "solid",
                                                        "text-align" : "left",
                                                        "display" : "inline-block",
                                                        "height" : "900px",
                                                        "width" : "99%"
                                                        }),])

if __name__ == '__main__':
    app.run_server()













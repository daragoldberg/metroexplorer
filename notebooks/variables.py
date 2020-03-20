#Total Population - to rename
PopTot = ['DP05_0001E','DP05_0001M']  #can also use b23001? 

#Foreign-Born Population - for calculation
PopFB = ['DP02_0092E','DP02_0092M']

#Tot Labor Force - to rename
LFTot = ['DP03_0002E','DP03_0002M']

#Age 25 to 54 in Labor Force - to caluclate
LF2554E = ['B23001_025E','B23001_032E','B23001_111E','B23001_118E','B23001_039E','B23001_125E','B23001_046E','B23001_132E']
LF2554M = ['B23001_025M','B23001_032M','B23001_111M','B23001_118M','B23001_039M','B23001_125M','B23001_046M','B23001_132M']

#Age 65+ in Labor Force - to calculate
LFO65E = ['B23001_074E','B23001_079E','B23001_084E','B23001_160E','B23001_165E','B23001_170E']
LFO65M = ['B23001_074M','B23001_079M','B23001_084M','B23001_160M','B23001_165M','B23001_170M']

#Total Housing Units - to rename
HouTot = ['DP04_0001E','DP04_0001M']

#Total Housing Units by Owner vs. Renter - to rename
HouO = ['DP04_0046E','DP04_0046M']
HouR = ['DP04_0047E','DP04_0047M']
HouV = ['DP04_0003E','DP04_0003M']

#Total Housing Units by Building Size - to calculate
Hou1UE = ['DP04_0007E','DP04_0008E']
Hou1UM = ['DP04_0007M','DP04_0008M']
Hou24UE = ['DP04_0009E','DP04_0010E']
Hou24UM = ['DP04_0009M','DP04_0010M']
Hou5UE = ['DP04_0011E','DP04_0012E','DP04_0013E']
Hou5UM = ['DP04_0011M','DP04_0012M','DP04_0013M']

HouU = Hou1UE + Hou1UM + Hou24UE + Hou24UM + Hou5UE + Hou5UM

#List of all variables used for calculation + total labor force variables - replace the total pop 16+ variables
var_data_test = [['GEO_ID'],PopTot,PopFB,LFTot,LF2554E,LF2554M,LFO65E,LFO65M,HouTot,HouO,HouR,HouV,HouU]
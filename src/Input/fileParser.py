import os
import csv
import math

def fileParser():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        _, extension = os.path.splitext(f)
        if(extension=='.csv'):
            print("parsing CSV")
            parseCSV(f)
            print("********************************************* End of CSV Parse ********************************************************")
        elif(extension=='.xml'):
            print("parsing XML")
        elif(extension=='.json'):
            print("parsing JSON")
        elif(extension=='.py'):
            continue
        else:
            print("Filetype " + extension + " is not supported yet")
    print("\n\n\n\n\n")
    
def parseCSV(filepath):
    dictdate = {}
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='#')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'ANUM {row[0]} | BNUM {row[1]} | ServiceType {row[2]} | CallCategory {row[3]} | SubscriberType {row[4]} | StartDateTime {row[5]} | usedAmt {row[6]}')
                unitsUsed = getUnitsUsed(row[2],row[6])
                print("UNITS USED: ",unitsUsed)
                totalCharge =  calculateCharges(row[2], row[3], row[4], unitsUsed)
                print("TOTAL CHARGE: ",totalCharge)
                normalizeBNUM(row[1])
                line_count += 1
                date = row[5][0:8]
                if(row[2] == '1' or row[2] =='3'):
                    if(date in dictdate):
                        dictdate[date] =  dictdate[date] + unitsUsed
                    else:
                        dictdate[date] = unitsUsed
                print("DICTIONARY OF USAGE BY DATE:     ",dictdate)
                print("========================================================================")
        print(dictdate)
        print(f'Processed {line_count} lines.')

def getUnitsUsed(serviceType, usedAmount): 
    print("C A L C U L A T I N G")
    if(serviceType=='1'):                           #If Service type 1, we will return duration in minutes rounded down
        # print("Calculating Voice Service")
        # print("seconds used: ",usedAmount)
        minutes = int(int(usedAmount)/60)
        seconds = int(usedAmount)%60
        if seconds>0:
            minutes = minutes+1
        # print("minutes rounded up: ", minutes )
        return minutes
    elif(serviceType=='2'):
        # print("SMS type does not have duration or volume")
        return 1;
    elif(serviceType=='3'):
        # print("calculating Volume in KB")           #For the interest of time, we assume that for every 2000KB or part thereof, we charge customers 2MB
        # print(usedAmount)   
        total2MB = int(usedAmount)/2000
        total2MB = math.ceil(total2MB)
        totalMB = total2MB * 2
        # print(totalMB)
        return totalMB
    else: 
        # print("invalid type")
        return -1;


def normalizeBNUM(BNUM):
    if(BNUM==""):
        pass
    else:
        BNUM = BNUM.lstrip("+")
        BNUM = BNUM.lstrip("00")
        print("Normalizing BNUM",BNUM,type(BNUM))
    return BNUM

def calculateCharges(serviceType, callCategory, subscriberType, unitsUsed):
    return ChargesTree[serviceType][callCategory][subscriberType] * unitsUsed

'''
To calculate charges, we use a tree dictionary as given in Figures 1-3
'''

ChargesTree = {
    '1':{  #SERVICE TYPE: VOICE
        '1': { #CALL CATEGORY
            '1': 0.3,  #SUBSCRIBER TYPE
            '2': 0.5
        },
        '2': {
            '1': 1.5,
            '2': 2
        }
    },
    '2': { #SERVICE TYPE: SMS
        '1':{
            '1':0.15,
            '2':0.25
        },
        '2':{
            '1':2,
            '2':2.5
        }
    },
    '3': { #SERVICE TYPE: GPRS
        '1':{
            '1':1,
            '2':1.5
        },
        '2':{
            '1':5,
            '2':6
        }
    }


}



fileParser()
# print(ChargesTree[3][2][2])
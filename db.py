# data base module

import json

def loadInfo( fileName ):
    file = open( f"{fileName}.json", "r" )
    data = json.loads( file.read() )
    file.close()
    return data

#def dataConversion( data ):
#    data.items()
#    data_as_list = list( data.items() )
#    return data_as_list

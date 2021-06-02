# data base module

import json

def loadInfo( fileName ):
    file = open( f"{fileName}.json", "r" )
    data = json.loads( file.read() )
    return data


import datetime


def boolToBit(bool):
    if bool: return '1'
    else: return '0'

def fixDateForSQL(_params):
        tstamp = datetime.strptime(_params, "%m/%d/%Y %I:%M:%S %p")
        newtstamp = datetime.date.strftime(tstamp, "%m-%d-%Y %I:%M:%S")
        replace = { _params: newtstamp }
        l = [replace.get(x, x) for x in _params]
        return l
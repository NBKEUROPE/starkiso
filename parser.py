from iso8583 import iso8583

def parse_iso_message(data):
    iso = iso8583.ISO8583()
    iso.setNetworkISO(data)
    return {
        'mti': iso.getMTI(),
        'fields': iso.getBitsAndValues()
    }

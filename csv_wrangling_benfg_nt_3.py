'''using named tuple

the tuple is typed each row is a FundingRecord
'''

import csv

from collections import namedtuple

FUNDING = 'funding.csv'

fields = ("permalink","company","numEmps", "category","city","state","fundedDate", "raisedAmt","raisedCurrency","round")

FundingRecord = namedtuple('FundingRecord', fields)

def read_funding_data(path):
    with open(path, 'rU') as data:
        data.readline()            # Skip the header
        reader = csv.reader(data)  # Create a regular tuple reader
        for row in map(FundingRecord._make, reader):
            yield row

if __name__ == "__main__":
    for row in read_funding_data(FUNDING):
        print (row)
        break
# https://medium.com/district-data-labs/simple-csv-data-wrangling-with-python-3496aa5d0a5e

'''
The namedtuple function actually returns a subclass of tuple 
with the type specified by the typename, 
the first argument to the function. 

The type that is returned is immutable once constructed 
and is extremely lightweight 

how can you parse the data into various types 
if you can’t assign it back to the object? 

the return from namedtuple is an actual type, 
one that you can subclass to add methods
'''
import csv
from collections import namedtuple
from datetime import datetime

FUNDING = 'funding.csv'

fields = ("permalink","company","numEmps", "category","city","state","fundedDate", "raisedAmt","raisedCurrency","round")

FundingRecord = namedtuple('FundingRecord', fields)


class FundingRecord(namedtuple('FundingRecord_', fields)):

    @classmethod
    def parse(klass, row):
        row = list(row)                                # Make row mutable
        row[2] = int(row[2]) if row[2] else None       # Convert "numEmps" to an integer
        row[6] = datetime.strptime(row[6], "%d-%b-%y") # Parse the "fundedDate"
        row[7] = int(row[7])                           # Convert "raisedAmt" to an integer
        return klass(*row)

    def __str__(self):
        date = self.fundedDate.strftime("%d %b, %Y")
        return "%s raised %i in round %s on %s" % (self.company, self.raisedAmt, self.round, date)


def read_funding_data(path):
    with open(path, 'rU') as data:
        data.readline()            # Skip the header
        reader = csv.reader(data)  # Create a regular tuple reader
        for row in map(FundingRecord.parse, reader):
            yield row


if __name__ == "__main__":
    for row in read_funding_data(FUNDING):
        print (row)
        break

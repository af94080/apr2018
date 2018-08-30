import csv
from collections import Counter

FUNDING = 'funding.csv'


class FundingReader(object):
    def __init__(self, path):
        self.path     = path
        self._length  = None
        self._counter = None

    def __iter__(self):
        self._length  = 0
        self._counter = Counter()
        with open(self.path, 'rU') as data:
            reader  = csv.DictReader(data)
            for row in reader:
                # Save the statistics
                self._length  += 1
                self._counter[row['company']] += 1
                yield row

    def __len__(self):
        if self._length is None:
            for row in self: continue # Read the data for length and counter
        return self._length

    @property
    def counter(self):
        if self._counter is None:
            for row in self: continue # Read the data for length and counter
        return self._counter

    @property
    def companies(self):
        return self.counter.keys()

    def reset(self):
        """
        In case of partial seeks (e.g. breaking in the middle of the read)
        """
        self._length  = None
        self._counter = None

if __name__ == "__main__":
    reader = FundingReader(FUNDING)
    print ("Funding reader with %i rows and %i companies" % (len(reader), len(reader.companies)))


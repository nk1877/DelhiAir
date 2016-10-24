import pandas as pd


class ColumnSearcher(object):
    def __init__(self, dataset, arnames=[]):
        self.arnames = arnames
        self.dataset = dataset

        def finder(d, arnames):
            s = []
            for i in d.columns:
                il = i.lower()
                for j in arnames:
                    jl = j.lower()
                    if il.find(jl) == -1:
                        pass
                    else:
                        s.append(i)
            return d[s]

        self.dataset= finder(self.dataset, self.arnames)

from barrel import *
from collections import defaultdict
from functools import partial


class Store:
    DEFAULT_PATH = 'F:\\storedb\\'

    def __init__(self, path = DEFAULT_PATH ):
        self.path = path
        self.global_record = {} 
        self.record_d = defaultdict(partial(defaultdict, defaultdict)) #infinitely deep 

    def make_record(self, rname): #make record for some particular key/value 
        if rname not in self.global_record:
            fp = open(rname+".txt", "w+")
            self.global_record[rname] = fp 
        return self.global_record[rname] 
 
    def del_record(self, rname):
        record = rname.name.split(".txt")[0]
        del self.global_record[record]
        
    def put(self, record, key, value):
        key = key[:32]
        rname = record.name
        
        if self.record_d[rname][key]:
            return "Already Exists"
        else:                          
            self.record_d[rname][key] = value

        fp = open(rname, "w")
        data = self.record_d[rname]
        json.dump(data, fp, indent=2)
        fp.close()        
        
    def get(self, record, key):
        data = json.loads(open(record.name).read())
        return data[key] 


store = Store()
newrecord = store.make_record("new record")
start = default_timer()
store.put(newrecord, "u1", {"name":"Darshan"})
print(default_timer() - start)


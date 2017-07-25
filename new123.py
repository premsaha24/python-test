import couchbase.subdocument as SD
from couchbase.bucket import Bucket

# Connecting to DB          

cb = Bucket('couchbase:///test', username = 'prem.saha',password='untrodden123')

# Creating DB
cb.upsert('55',{'55':[{'text':'text','user_id':'user_id','created_at':'created_at','time':'time'}]}) # only run once

# updating DB 
#cb.mutate_in('55', SD.array_append('55',{'text':'text','user_id':'user_id','created_at':'created_at','time':'time'}))


# Get Key-value operations from  db  

#rv = cb.get('12345')
#print rv.key
#print dir(rv)


# doing upsert and insert at same time in DB

#cb.mutate_in('hello',SD.upsert('path1', 'value1'),SD.insert('path2', 'value2', create_parents=True))
#cb.mutate_in('hello',SD.insert('path34', 'value', create_parents=True))
#cb.mutate_in('1234',SD.upsert('1234',{'text':'text','user_id':'user_id','created_at':'created_at','time':'time'}))
#cb.mutate_in('1234', SD.insert('fax', '775-867-5309'))
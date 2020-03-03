from database import connection
import re
# import parser
from tools import spliters


sql_query = '''SELECT ROUTINE_SCHEMA as sch, SPECIFIC_NAME as sp_name, 
                ROUTINE_TYPE, ROUTINE_BODY, ROUTINE_DEFINITION as `sql`, 
                SQL_DATA_ACCESS, CREATED, LAST_ALTERED FROM information_schema.routines 
                WHERE routine_type = 'PROCEDURE';'''
db = connection()

res = db.conn_mysql(sql_query)
spt = spliters()

#dictionary
ndict = {} 

#list
sch = [] 
sp = []
sbody = []

for i in res:
    sch.append(i[0])
    sp.append(i[1])
    sbody.append(i[4].lower())


ndict['sch'] = sch
ndict['sp_name'] = sp
ndict['sp_body'] = sbody


# Splitting comment and cleaning data
for k,v in ndict.items():
    if k == 'sp_body':
        nls = []
        for i in v:
            nls.append(spt.reformat(i))
        ndict[k] = nls

## Split data using space and dot
print(ndict['sp_body'][1])


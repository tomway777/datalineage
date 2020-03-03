import mysql.connector as ms
from config import config 


'''
    configuration on config.yaml.
     - expose group config using expose_config function
     - accessing certain data using dictionary key combination
'''
cfg = config()
db = cfg.expose_config('database')


# ----------------------------------------------------------------------------------------

class connection:

    def conn_mysql(self, query):
        # connect to mysql
        database = ms.connect(
            host= db['mysql']['host'],
            user= db['mysql']['user']
        )

        mcursor = database.cursor()

        mcursor.execute(query)

        res = mcursor.fetchall()

        return res
    
    
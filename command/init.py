import model.table
from conf import settings
import os

def run(app):
    os.system("mysqldump -u sandhub -h localhost -psm87Mp*#@ -t sandhub > data.sql ")
    
    model.table.init_db(settings["db_string"],"root","_+_#!&lbokl*^ljj")
    
    os.system("mysql -u sandhub -h localhost -psm87Mp*#@ -D sandhub -e 'source data.sql;'")
    os.system("[ -f data.sql ] && rm data.sql")

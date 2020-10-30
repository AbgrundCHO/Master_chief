from login import read_ras_password, decode2str
from py2neo import Graph


def data2neo4j():
    __username, __password = read_ras_password()
    link = Graph('http://localhost:7474',
                 username=decode2str(__username),
                 password=decode2str(__password))
    return link
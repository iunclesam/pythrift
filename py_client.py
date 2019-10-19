# _*_ coding:utf-8 _*_
__author__ = '作者'

from py.thrift.generated import PersonService
from py.thrift.generated import ttypes

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
import sys

reload(sys)
sys.setdefaultencoding('utf8')

try:
    tSocket = TSocket.TSocket('127.0.0.1', 8899)
    tSocket.setTimeout(600)

    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = PersonService.Client(protocol)

    transport.open()

    person = client.getPersonByUsername('张三')

    print person.username
    print person.age
    print person.married

    print '---------------'

    person2 = ttypes.Person()
    person2.username = '李四'
    person2.age = 33
    person2.married = True

    client.savePerson(person2)

    transport.close()

except Thrift.TException, tx:
    print '%s' % tx.message

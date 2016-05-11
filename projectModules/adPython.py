from ldap3 import *
from projectModules import distinctName
from config import adConfig

class AdPython:
    def __init__(self, ip, user, password, struct = ['Users','ferdi','baba']):
        self.distinctName = distinctName.DistinctName(struct)
        self.stdpath = self.distinctName.makeDN()
        server = Server(ip, get_info=ALL)
        self.conn = Connection(server, 'cn=' + user + ',cn=Users,dc=ferdi,dc=baba', password, auto_bind=True)
        self.handleResult()

    def searchUser(self,username='*'):
        self.conn.search(search_base='dc=ferdi,dc=baba',
                         search_filter='(cn='+username+')',
                         search_scope=SUBTREE)
        self.handleResult()
        if(len(self.conn.entries) > 1 or self.conn.entries == []):
            return self.conn.entries
        else:
            return self.conn.entries[0]._dn

    def searchOU(self,name='*'):
        self.conn.search(search_base= 'dc=ferdi,dc=baba',search_filter='(name ='+ name + ')')
        self.handleResult()
        if (len(self.conn.entries) > 1 or self.conn.entries == []):
            return self.conn.entries
        else:
            return self.conn.entries[0]._dn

    def addOU(self,name):
        path = self.searchOU(name[:2])
        self.conn.add('ou=' + name + ',' + path,['organizationalUnit'],{'description':name})
        self.handleResult()

    def addUser(self,username,firstname,surname,password,ou):
        #self.distinctName.addou(ou)
        path = self.searchOU(ou)
        self.conn.add('cn=' + username + ',' + path,['user'],{'displayName':firstname+' '+surname, 'givenName':firstname,'sn':surname,'userpassword':password})
        self.handleResult()

    def modifyUser(self,username,newou):
        oldPath = self.searchUser(username)

        newPath = self.searchOU(newou)

        self.conn.modify_dn(oldPath, 'CN=' + username, delete_old_dn=True, new_superior=newPath)
        self.handleResult()

    def deleteOU(self,name):
        path = self.searchOU()
        self.conn.delete(path)
        self.handleResult()

    def deleteUser(self,username):
        path = self.searchUser(username)
        self.conn.delete(path)
        print('User '+username+' deleted')
        self.handleResult()

    def handleResult(self):
        if (self.conn.result['description'] != 'success'):
            print(self.conn.result)

    def syncsql(self,list):
        for row in list:
            if(self.searchUser(row[3]) == []):
                print('User nicht vorhanden')
                if(self.searchOU(row[5]) == []):
                    print('OU nicht vorhanden')
                    self.addOU(row[5])
                    print('OU ' + row[5] + ' angelegt')
                else:
                    print('OU vorhanden')
                self.addUser(row[3],row[2],row[1],row[4],row[5])
                print('User '+row[3]+' added')
            else:
                print('User vorhanden')
                if (self.searchOU(row[5]) == []):
                    print('OU nicht vorhanden')
                    self.addOU(row[5])
                    print('OU '+row[5]+' angelegt')
                else:
                    print('OU vorhanden')
                self.modifyUser(row[3],row[5])
                print('User '+row[3]+' moved')



#adobj = AdPython(adConfig.server,adConfig.username,adConfig.password,['IT','Klassen','Schueler','Benutzer','ferdi','baba'])
 # #adobj.addUser('IT4-popopo','Po','Tato','1234!ASS','IT4a')
 #adobj.deleteOU('IT4a')
 # adobj.deleteUser('IT4-popopo')
 #
# print(adobj.searchUser('IT4-lentda'))
#ou = adobj.searchOU('IT4b')
#print(ou)
#adobj.modifyUser('IT4a-MustMa','IT4n')

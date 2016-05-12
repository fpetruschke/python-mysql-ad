from ldap3 import *
import config.adConfig as adC


class AdPython:
    def __init__(self, ip, user, password, dict=adC.dict):
        #pass general OU structure
        self.stddict = dict

        #initiate connection to AD, needs Administrator User in default container Users
        server = Server(ip, get_info=ALL)
        self.conn = Connection(server, 'cn=' + user + ',cn=Users,'+self.makeDN(1), password, auto_bind=True)
        self.handleResult()

        self.__initOU()

    # initiate general OU structure as passed in parameter dict
    # doesn't delete unused general OUs
    def __initOU(self):
        counter = 2
        while(counter <= len(self.stddict)-1):
            #only create OU if not already existing
            if(self.searchOU(self.stddict[counter]) == []):
                print('initial create '+self.makeDN(counter))
                self.conn.add(self.makeDN(counter),['organizationalUnit'],{'description':self.stddict[counter]})
                self.handleResult()
            counter += 1

    #check if OU is empty and return bool
    #needs complete dn
    def ouEmpty(self,path):
        self.conn.search(search_base= path,
                         search_filter='(objectClass=*)',
                         search_scope=LEVEL)
        if(self.conn.entries == []):
            return True
        else:
            return False

    #search for user in AD and return dn if distinct
    def searchUser(self,username='*',step=1):
        self.conn.search(search_base=self.makeDN(step),
                         search_filter='(cn='+username+')',
                         search_scope=SUBTREE)
        self.handleResult()
        if(len(self.conn.entries) > 1 or self.conn.entries == []):
            return self.conn.entries
        else:
            return self.conn.entries[0]._dn

    #search for OU in AD and return dn if distinct
    def searchOU(self,name='*'):
        self.conn.search(search_base= self.makeDN(1),search_filter='(name ='+ name + ')')
        self.handleResult()
        if (len(self.conn.entries) > 1 or self.conn.entries == []):
            return self.conn.entries
        else:
            return self.conn.entries[0]._dn

    #create new OU
    #just usable for specific classes i.e. IT4a
    def addOU(self,name):
        path = self.searchOU(name[:2])
        self.conn.add('ou=' + name + ',' + path,['organizationalUnit'],{'description':name})
        self.handleResult()

    #creates User under OU and populate info
    #OU needs to exist
    def addUser(self,username,firstname,surname,password,ou):
        path = self.searchOU(ou)
        self.conn.add('cn=' + username + ',' + path,['user'],{
            'displayName':firstname+' '+surname,
            'givenName':firstname,
            'sn':surname,
            'userpassword':password,
            'homeDirectory': "home/"+username})
        self.handleResult()

    #copy user to new OU and delete in old OU
    #not to be used to modify user info
    def modifyUser(self,username,newou):
        oldPath = self.searchUser(username)

        newPath = self.searchOU(newou)

        self.conn.modify_dn(oldPath, 'CN=' + username, delete_old_dn=True, new_superior=newPath)
        self.handleResult()

    #delete empty OUs after the general OU struct
    #doesn't delete OUs existent in stddict
    def deleteEmptyOU(self):
        self.conn.search(search_base=self.makeDN(len(self.stddict) - 1),
                         search_filter='(objectClass=*)',
                         search_scope=LEVEL)
        #iterate over all OUs after stddict
        for item in self.conn.entries:
            #check if empty and delete
            if(self.ouEmpty(item._dn)):
                print('delete '+item._dn)
                self.conn.delete(item._dn)
                self.handleResult()

    #delete user specified in parameter username
    def deleteUser(self,username):
        path = self.searchUser(username)
        self.conn.delete(path)
        print('User '+username+' deleted')
        self.handleResult()

    #handle the result of connection actions
    #prints if not success
    def handleResult(self):
        if (self.conn.result['description'] != 'success'):
            print(self.conn.result)

    #create dn from stddict with depth of num
    def makeDN(self,num):
        dn = ''
        counter = num
        while (counter >= 0):
            if(counter != num):
                dn += ','
            if(counter == 0 or counter == 1):
                dn += 'dc='
            else:
                dn += 'ou='
            dn =  dn + self.stddict[counter]
            counter -= 1
        return dn

    #logic for syncing tupels from GUI, db or csv with AD
    #creates OUs Users and deletes OUs if empty
    def syncsql(self,list,flg_sql=False):
        for row in list:
            if(self.searchUser(row[3]) == []):
                print('User '+row[3]+' not existent')

                if(self.searchOU(row[5]) == []):
                    print('OU '+row[5]+' not existent')
                    self.addOU(row[5])
                    print('OU ' + row[5] + ' created')
                else:
                    print('OU '+row[5]+' existent')

                self.addUser(row[3],row[2],row[1],row[4],row[5])
                print('User '+row[3]+' added')
            else:
                print('User '+row[3]+' existent')

                if (self.searchOU(row[5]) == []):
                    print('OU ' + row[5] + ' not existent')
                    self.addOU(row[5])
                    print('OU '+row[5]+' created')
                else:
                    print('OU ' + row[5] + ' existent')

                self.modifyUser(row[3],row[5])
                print('User '+row[3]+' moved')

        if(flg_sql):
            #delete Users not existent in SQL
            #only execute when sql-flag is set
            self.searchUser(step=5)
            for item in self.conn.entries:
                delete = True
                testeduser = item._dn[3:13]
                for row in list:
                    if(testeduser == row[3]):
                        delete = False
                if(delete):
                    self.deleteUser(testeduser)

        #delete empty OUs after sync actions
        self.deleteEmptyOU()

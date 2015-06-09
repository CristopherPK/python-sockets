'''

@author: Cristopher Freitas
'''
from bank.manager import Manager


class BankInterface():

    def __init__(self):
        self._manager = Manager()

    def clientUI(self):


    def managerUI(self):
        self._manager.load()

        while True:
            print "------------------\n" \
            "1 - Add Client\n" \
            "2 - List Clients\n" \
            "3 - Remove Client\n" \
            "4 - Reports\n" \
            "0 - Exit\n" \
            "------------------\n"

            x = int(input("Please enter an option: "))

            if x == 1:
                id = int(raw_input("Please enter an ID: "))
                name = str(raw_input("Please enter a name: "))
                c = self._manager.createAccount(id, name)
                print "Account created."
                self._manager.save()
            elif x == 2:
                self._manager.listClients()
            elif x == 3:
                id = int(raw_input("Please enter an ID: "))
                self._manager.removeClient(id)
                self._manager.save()
            elif x == 4:
                self._manager.genReport()
            else:
                break
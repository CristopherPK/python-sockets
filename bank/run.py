'''

@author: Cristopher Freitas
'''
from bank.manager import Manager

manager = Manager()

def start():

    #TODO: If load has nothing?
    manager.load()

    print "------------------\n" \
        "1 - Admin Interface\n" \
        "2 - Client Interface\n" \
        "0 - Exit\n" \
        "------------------\n"

    x = int(input("Please enter an option: "))

    if x == 1:
        managerUI()
    elif x == 2:
        clientUI()
    else:
        print 'Finishing...'


def clientUI():
    id = input('Insert your bank id: ')
    password = raw_input('Insert your bank password: ')
    client = manager.connectAccount(id, password)

    while True:
        print "------------------\n" \
        "1 - Check balance\n" \
        "2 - Deposit\n" \
        "3 - Withdraw\n" \
        "4 - Transfer\n" \
        "0 - Exit\n" \
        "------------------\n"

        x = int(input("Please enter an option: "))

        if x == 1:
            print client.balance

        elif x == 2:
            value = input('Insert the value: ')
            client.deposit(int(value))
        elif x == 3:
            value = input('Insert the value: ')
            client.withdraw(int(value))
        elif x == 4:
            dst_id = input('Insert the destination account id: ')
            dst = manager.lookForClientByID(dst_id)
            value = input('Insert the value: ')
            client.transfer(dst, value)
        elif x == 0:
            print 'Finishing...'
            break
        else:
            print 'Invalid operation'
            continue

    manager.save()

def managerUI():
    id = input('Insert your bank id: ')
    password = raw_input('Insert your bank password: ')
    admin = manager.connectAccount(int(id), password)

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
            password = str(raw_input("Please enter a password: "))
            c = manager.createAccount(id, name, password)
            print "Account created."
            manager.save()
        elif x == 2:
            manager.listClients()
        elif x == 3:
            id = int(raw_input("Please enter an ID: "))
            manager.removeClient(id)
            manager.save()
        elif x == 4:
            manager.genReport()
        else:
            break

if __name__ == '__main__':
    start()
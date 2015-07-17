'''

@author: Cristopher Freitas
'''
from manager import Manager

manager = Manager()

def start():

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

    while True:

        print "------------------\n" \
        "1 - Check balance\n" \
        "2 - Deposit\n" \
        "3 - Withdraw\n" \
        "4 - Transfer\n" \
        "5 - Return to main menu\n" \
        "0 - Exit\n" \
        "------------------\n"

        x = int(input("Please enter an option: "))

        manager.refresh()
        client = manager.connectAccount(id, password)

        if x == 1:
            if manager.auth():
                print client.balance
        elif x == 2:
            if manager.auth():
                value = input('Insert the value: ')
                client.deposit(int(value))
                manager.save()
        elif x == 3:
            if manager.auth():
                value = input('Insert the value: ')
                client.withdraw(int(value))
                manager.save()
        elif x == 4:
            dst_id = input('Insert the destination account id: ')
            dst = manager.lookForClientByID(dst_id)
            value = input('Insert the value: ')
            client.transfer(dst, value)
            manager.save()
        elif x == 5:
            start()
        elif x == 0:
            print 'Finishing...'
            break
        else:
            print 'Invalid operation'
            continue

def managerUI():
    id = input('Insert your bank id: ')
    password = raw_input('Insert your bank password: ')

    while True:
        print "------------------\n" \
        "1 - Add Client\n" \
        "2 - List Clients\n" \
        "3 - Remove Client\n" \
        "4 - Reports\n" \
        "5 - Return to main menu\n" \
        "0 - Exit\n" \
        "------------------\n"

        x = int(input("Please enter an option: "))

        manager.refresh()
        client = manager.connectAccount(id, password)

        if x == 1:
            if manager.auth():
                id = int(raw_input("Please enter an ID: "))
                name = str(raw_input("Please enter a name: "))
                password = str(raw_input("Please enter a password: "))
                c = manager.createAccount(id, name, password)
                manager.save()
                print "Account created."
        elif x == 2:
            manager.listClients()
        elif x == 3:
            if manager.auth():
                id = int(raw_input("Please enter an ID: "))
                manager.removeClient(id)
                manager.save()
        elif x == 4:
            if manager.auth():
                print repr(manager.genReport())
        elif x == 5:
            start()
        elif x == 0:
            print 'Finishing...'
            break
        else:
            print 'Invalid operation'
            continue

if __name__ == '__main__':
    start()
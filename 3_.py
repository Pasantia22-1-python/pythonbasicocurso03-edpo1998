
from glob import glob
from http import client


clients = ["pablo","ricardo"]


def create_cliente(client_name):
    global clients;

    if client_name not in clients:
        clients.append(client_name);
    else:
        print("Client already is in the client's list")
        

def list_clients():
    for idx,client in enumerate(clients):
        print("{}:{}".format(idx,client))


def update_client(client_name,update_client_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        clients[index]=  update_client_name
    else:
        print("Client is not in client list")

def delete_client(client_name):
    if client_name in clients:
        clients.remove(client_name)
    else:
        print("Client is not in client list")

import sys

def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return client

def _get_client_name():
    client_name = None;
    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            break

        if not client_name:
            sys.exit()
            
    return client_name;

def _print_welcome():
    print("WELCOM TO PLATZI VENTAS")
    print("*"*50)
    print("What would you like to do today?")
    print("[C]Create client")
    print("[D]Delete client")
    print("[U]Update client")
    print("[S]Search client")

if __name__ == '__main__':
    _print_welcome()

    command = input().upper()

    if command == 'C':
        cliente_name =  input("What is the client name? ")
        client_name = _get_client_name()
        create_cliente(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name =  input("What is the updated client name? ")
        update_client(client_name,update_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()  
        found = search_client(client_name)
        if found:
            print("The client is in the client\'s List")
        else:
            print("The client {} is not in the client\'s List".format(client_name)) 
    else:
        print("Invalid command")

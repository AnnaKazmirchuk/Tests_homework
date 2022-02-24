documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def request_doc_number(document_number):
    document_number = input('Введите номер документа ')
    for doc in documents:
        if doc["number"] == document_number:
            return doc["name"]
    return 'Такого документа в каталоге нет'


# print(request_doc_number(documents))

def request_doc_shelf(document_number):
    document_number = input('Введите номер документа ')
    for k in directories:
        if document_number in directories[k]:
            return (f'Номер полки {k}')
    return 'Такого документа в каталоге нет'


# print(request_doc_shelf(directories))

def request_doc_list(document_number):
    for doc in documents:
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')


# request_doc_list(documents)

def add_new_doc(documemt_number):
    shelf_number = input('Введите номер полки для хранения ')
    if shelf_number not in directories:
        return 'Такой полки нет'
    document_type = input('Введите тип документа ')
    document_number = input('Введите номер документа ')
    document_name = input('Введите имя владельца ')
    new_doc = dict(type=document_type, number=document_number, name=document_name)
    documents.append(new_doc)
    directories[shelf_number] += [document_number]
    print()
    return documents
    print()
    return directories


# print(add_new_doc(documents))


def main_request_by_doc_number(document_number):
    while True:
        command = input('Введите команду ')
        if command == 'p':
            print(request_doc_number(document_number))
        elif command == 's':
            print(request_doc_shelf(document_number))
        elif command == 'l':
            request_doc_list(document_number)
        elif command == 'a':
            print(add_new_doc(document_number))
        elif command == 'quit':
            print('Выход из программы')
            break




if __name__ == '__main__':
    main_request_by_doc_number(documents)
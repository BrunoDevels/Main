import pickle


def remetente_prefixo_dr_dra(lista):
    sublista = []
    for item in lista:
        if item[0].upper().startswith('DR'):
            sublista.append(item)
    return sublista


def total_remetente_prefixo_dr_dra(lista):
    sublista = remetente_prefixo_dr_dra(lista)
    count = 0
    for element in sublista:
        if element[0].upper().startswith('DR'):
            count += 1
    return count
    

def destinatario_prefixo_dr_dra(lista):
    sublista = []
    for receiver in lista:
        if receiver[4].upper().startswith('DR'):
            sublista.append(receiver)
    return sublista
        
def total_destinatario_prefixo_dr_dra(lista):
    sublista = destinatario_prefixo_dr_dra(lista)
    count_receiver = 0
    for element in sublista:
        if element[4].upper().startswith('DR'):
            count_receiver += 1
    return count_receiver

def remetente_destinatario_prefixo_dr_dra(lista):
    sublista = []
    for receiver_reme in lista:
        if receiver_reme[0].upper().startswith('DR') and receiver_reme[4].upper().startswith('DR'):
            sublista.append(receiver_reme)
    return sublista


def destinatario_busca_sobrenomes(lista, sobrenome):
    sublista = []
    for iten in lista:
        if sobrenome in iten[4]:
            if 'Dr' in iten[4] or 'Sr' in iten[4]:
                formated_name = iten[4].split(' ')[1]
                name = formated_name.split(' ')[0]
            else:
                name = iten[4].split(' ')[0]
            cpf = iten[6]
            lists = (name, cpf)
            sublista.append(lists)
    return sublista


def destinatario_busca_sobrenomes_primeiros(lista, sobrenome):
    sublista = []
    index = 0
    for iten in lista:
        if sobrenome in iten[4]:
            if 'Dr' in iten[4] or 'Sr' in iten[4]:
                formated_name = iten[4].split(' ')[1]
                name = formated_name.split(' ')[0]
            else:
                name = iten[4].split(' ')[0]
                cpf = iten[6]
                lists = (name, cpf)
                sublista.append(lists)
        sublista = sublista[:10]
    return sublista

def destinatario_busca_sobrenomes_ultimos(lista, sobrenome):
    sublista = []
    index = 0
    for iten in lista:
        if sobrenome in iten[4]:
            if 'Dr' in iten[4] or 'Sr' in iten[4]:
                formated_name = iten[4].split(' ')[1]
                name = formated_name.split(' ')[0]
            else:
                name = iten[4].split(' ')[0]
                cpf = iten[6]
                lists = (name, cpf)
                sublista.append(lists)
        sublista = sublista[-10:]
    return sublista

def remetente_destinatario_mesmo_estado(lista):
    sublista = []
    for state in lista:
        remetente = state[1].split(' / ')[1]
        destinatario = state[5].split(' / ')[1]
        if remetente == destinatario:
            sublista.append(state)   
    return sublista

def busca_email_remetente(lista, email):
    sublista = []
    listalen = len(lista)
    index = 0
    for iten in lista:
        if iten[3] == email:
            sublista.append(iten)
            if index == listalen:
                return sublista
            index += 1
    return tuple(sublista)

def busca_email_destinatario(lista, email):
    sublista = []
    listalen = len(lista)
    index = 0
    for iten in lista:
        if iten[7] == email:
            sublista.append(iten)
            if index == listalen:
                return sublista
            index += 1
    return sublista


def busca_estado_remetente(lista):
    sublista = []
    for state in lista:
        remetente = state[1].split(' / ')[1]
        sublista.append(remetente)
        ss = set(sublista)
        sl = list(ss)
    return sl


def busca_email_remetente_por_dominio(lista, dominio='gmail.com'):
    sublista = []
    listalen = len(lista)
    index = 0
    for iten in lista:
        dom = iten[3].split('@')[1]
        if dom == dominio:
            sublista.append(iten)
            if index == listalen:
                return sublista
            index += 1
    return sublista


def busca_email_destinatario_por_dominio(lista, dominio='gmail.com'):
    sublista = []
    listalen = len(lista)
    index = 0
    for iten in lista:
        dom = iten[7].split('@')[1]
        if dom == dominio:
            sublista.append(iten)
            if index == listalen:
                return sublista
            index += 1
    return sublista


def busca_cpf(lista, cpf):
    sublista = []
    for iten in lista:
        if iten[2] == cpf or iten[6] == cpf:
            sublista.append(iten)
    return sublista


def busca_primeira_data_por_mes(lista, mes):
    sublista = []
    for data in lista:
        month = data[8].split('-')[1]
        if month == mes:
            sublista.append(data)
    return(sublista)

def busca_segunda_data_por_mes(lista, mes):
    sublista = []
    for data in lista:
        month = data[9].split('-')[1]
        if month == mes:
            sublista.append(data)
    return(sublista)


def busca_terceira_data_por_mes(lista, mes):
    sublista = []
    for data in lista:
        month = data[10].split('-')[1]
        if month == mes:
            sublista.append(data)
    return(sublista)


def busca_data(lista, dia='01', mes='07', ano='2020'):
    sublista = []
    for iten in lista:
        date = f'{ano}-{mes}-{dia}'
        if date == iten[8] or date == iten[9] or date == iten[10]:
            sublista.append(iten)
    return sublista
        
if __name__ == "__main__":
    with open('lista.bin', 'rb') as list_in_file:
        lista = pickle.load(list_in_file)
    sublista = remetente_prefixo_dr_dra(lista)

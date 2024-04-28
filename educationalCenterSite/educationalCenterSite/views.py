from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def index(request):
    return HttpResponseRedirect('/login')

def information(request):
    import json
    with open('company.json') as json_file:
        data = json.load(json_file)
    return render(request, 'information.html', {'dates': data})

def users(request):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    if request.method == 'POST':
        allUsers = cur.execute('SELECT id FROM users').fetchall()
        listData = [int(i[0])-1 for i in list(request.POST.keys())[1:]]
        print(listData)
        for data in allUsers:
            if data[0] in listData:
                cur.execute(f'''UPDATE users SET admin = 1 WHERE id = {data[0]}''')
            else:
                cur.execute(f'''UPDATE users SET admin = 0 WHERE id = {data[0]}''')
        con.commit()
        return HttpResponseRedirect('/information/users')
    else:
        allUsers = cur.execute('SELECT * FROM users').fetchall()
        allUser = []
        for user in range(len(allUsers)):
            users1 = list(allUsers[user])
            users1[3] = UsersAdmin(initial={'admin':True}, prefix=user+1) if users1[3] == 1 \
                else UsersAdmin(prefix=user+1)
            allUser.append(users1)
        return render(request, 'users.html', {'allUsers': allUser})

def login(request):
    out = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            import sqlite3
            con = sqlite3.connect('educationalDate.db')
            cur = con.cursor()
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            passwordTrue = cur.execute(f'''SELECT id, password from users WHERE name = "{name}" ''').fetchall()
            if passwordTrue == []:
                out = 'Неверный логин'
            else:
                id = passwordTrue[0][0]
                if passwordTrue[0][1] == password:
                    outt = HttpResponseRedirect('/information')
                    outt.set_cookie("id", id, max_age=7*24*60*60)
                    return outt
                else:
                    out = 'Неверный пароль'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'out': out})

def employees(request):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    allEmployees = cur.execute('SELECT * FROM employees').fetchall()
    return render(request, 'employees.html', {'allEmployees': allEmployees})

def groupReports(request):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    allGroupReports = cur.execute('SELECT * FROM groupReports').fetchall()
    return render(request, 'groupReports.html', {'allGroupReports': allGroupReports})

def studyingProgramTranslate(listDate, x = 0):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    if x == 0:
        boolFields = ['Нет', 'Да']
        resulChoose = ['Зачет', 'Незачет', 'Пропуск']
        listDate[8] = boolFields[int(listDate[8])]
        listDate[9] = boolFields[int(listDate[9])]
        listDate[10] = boolFields[int(listDate[10])]
        listDate[11] = boolFields[int(listDate[11])]
        listDate[12] = boolFields[int(listDate[12])]
        listDate[13] = boolFields[int(listDate[13])]
        listDate[14] = resulChoose[listDate[14]]
        return listDate
    else:
        nameGroup = cur.execute(f'select nameGroup from groupReports where id = {listDate[4]}').fetchone()[0]
        listDate.insert(5, nameGroup)
        return listDate

def studyingProgram(request):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    allStudyingProgram = cur.execute('SELECT * FROM studyingPrograms').fetchall()
    for i in range(len(allStudyingProgram)):
        allStudyingProgram[i] = studyingProgramTranslate(list(allStudyingProgram[i]))
    return render(request, 'studyingProgram.html', {'allStudyingProgram': allStudyingProgram})

def applicationsTranslate(listData, idUser = -1):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    if idUser == -1:
        boolVal = ['Нет', 'Да']
        stat = ['Новый', 'Выставлен счет', 'Обучение частично', 'Выполнена']
        listUser = [i[0] for i in cur.execute('SELECT name FROM users').fetchall()]
        listData[4] = stat[int(listData[4])]
        listData[5] = boolVal[int(listData[5])]
        listData[6] = boolVal[int(listData[6])]
        listData[8] = listUser[int(listData[8])]
        return listData
    else:
        import datetime
        nameClient = cur.execute(f'SELECT name FROM clients where id = {listData[1]}').fetchone()[0]
        listData.insert(1, nameClient)
        listData.insert(3, datetime.datetime.now())
        listData.insert(4, 0)
        listData.append(idUser)
        idTrainee = listData[0]
        listData.append(idTrainee)
        return listData

def protocolsTranslate(listData, idUser = -1):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    import datetime
    nameProgram = cur.execute(f'SELECT name FROM studyingPrograms where id = {listData[1]}').fetchone()[0]
    listData.insert(2, nameProgram)
    listData.insert(3, datetime.datetime.now())
    listData.insert(4, 1)
    listData.append(idUser)
    return listData

def clients(request):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    allClients = cur.execute('SELECT * FROM clients').fetchall()
    return render(request, 'clients.html', {'allClients': allClients})

def add(request):
    listForm = [EmployeesForm, GroupReportsForm, ClientsForm, StudyingProgramForm, ApplicationsForm, ProtocolsForm]
    idForm = int(request.GET.get('id-form'))
    if request.method == 'POST':
        import sqlite3
        con = sqlite3.connect('educationalDate.db')
        cur = con.cursor()
        addRequest = [
            ['employees', '?,?,?'],
            ['groupReports', '?,?'],
            ['clients', '?,?,?,?,?'],
            ['studyingPrograms', '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?'],
            ['applications', '?,?,?,?,?,?,?,?,?,?'],
            ['protocols', '?,?,?,?,?,?']
        ]
        id = len(cur.execute(f"SELECT * FROM {addRequest[idForm][0]}").fetchall())
        if idForm == 3:
            listDate = tuple(studyingProgramTranslate(([id] + list(request.POST.values())[1:]), 1))
        elif idForm == 4:
            listDate = tuple(applicationsTranslate(([id] + list(request.POST.values())[1:]), request.COOKIES.get('id')))
        elif idForm == 5:
            listDate = tuple(protocolsTranslate(([id] + list(request.POST.values())[1:]), request.COOKIES.get('id')))
        else:
            listDate = tuple(([id] + list(request.POST.values())[1:]))
        cur.execute(f'''INSERT INTO {addRequest[idForm][0]} VALUES({addRequest[idForm][1]})''', listDate)
        if idForm == 4:
            for i in range(int(listDate[-3])):
                cur.execute(f'''INSERT INTO trainee values ({listDate[-1]}, NULL, NULL, NULL, NULL, NULL, NULL, {i})''')
        if idForm == 5:
            for i in range(int(listDate[4])):
                cur.execute(f'''INSERT INTO protocolsClients values ({i} ,{listDate[0]}, NULL, NULL, NULL, NULL, NULL)''')
        con.commit()
        red = ['/information/employees', '/information/group-reports',
               '/applications/clients', '/information/studying-program',
               f'/applications/list?id={id}', f'/protocols/clients?id={id}']
        return HttpResponseRedirect(red[idForm])
    else:
        form = listForm[idForm]()
    return render(request, 'add.html', {'form': form})

def application(request):
    return render(request, 'application.html')

def edit(request):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    listForm = [EmployeesForm, GroupReportsForm, ClientsForm, StudyingProgramForm]
    idForm = int(request.GET.get('id-form'))
    idRow = int(request.GET.get('id-row'))
    addRequest = ['employees', 'groupReports', 'clients', 'studyingPrograms']
    if request.method == 'POST':
        listValue = list(request.POST.values())[1:]
        if idForm == 3:
            boolFields = {'Нет': 0, 'Да': 1}
            resulChoose = {'Зачет': 0, 'Незачет': 1, 'Пропуск': 2}
            print(listValue)
            listValue[6] = boolFields[listValue[6]]
            listValue[7] = boolFields[listValue[7]]
            listValue[8] = boolFields[listValue[8]]
            listValue[9] = boolFields[listValue[9]]
            listValue[10] = boolFields[listValue[10]]
            listValue[11] = boolFields[listValue[11]]
            listValue[12] = resulChoose[listValue[12]]
        listKey = list(request.POST.keys())[1:]
        outReq = f'UPDATE {addRequest[idForm]} SET '
        for dataOne in listKey:
            outReq += f'{dataOne} = ?, '
        outReq = outReq[:-2] + f' WHERE id = {idRow}'
        cur.execute(outReq, listValue)
        con.commit()
        red = ['/information/employees', '/information/group-reports', '/applications/clients',
               '/information/studying-program']
        return HttpResponseRedirect(red[idForm])
    else:
        listValue = cur.execute(f'SELECT * from {addRequest[idForm]} WHERE id = {idRow}').fetchone()
        listValue = list(listValue)
        if idForm == 3:
            listValue = studyingProgramTranslate(listValue)
            listValue = listValue[1:4]+listValue[5:]
        else:
            listValue = listValue[1:]
        form = listForm[idForm](my_arg=listValue)
    return render(request, 'edit.html', {'form': form})

def applicationsList(request):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    allApplications = cur.execute('SELECT * FROM applications').fetchall()
    nList = []
    for i in range(len(allApplications)):
        nList.append(applicationsTranslate(list(allApplications[i])))
    return render(request, 'applicationsList.html', {'allApplications': nList})

def listClients(request):
    idApplication = int(request.GET.get('idApplication'))
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    if request.method == 'POST':
        listData = list(request.POST.values())[1:]
        applications = listData[:4]
        if listData[-1] == "1":
            idTrainee = int(cur.execute(f'SELECT MAX(idInd) FROM trainee WHERE id = {idApplication}').fetchone()[0]) + 1
            countTrainee = int(cur.execute(f'SELECT countEmployees FROM applications WHERE id = {idApplication}').fetchone()[0]) + 1
            cur.execute(f'''INSERT INTO trainee values ({idTrainee}, {idApplication}, NULL, NULL, NULL, NULL, NULL)''')
            cur.execute(f"update applications set countTrainee = {countTrainee} WHERE id = {idApplication}")
        listData = listData[4:-1]
        nameClient = cur.execute(f'SELECT name FROM clients where id = {applications[0]}').fetchone()[0]
        applications.insert(1, nameClient)
        cur.execute(f'update applications set idClient = ?, nameClient = ?, postpaid = ?, receiptPayment = ?, countEmployees = ? where id = {idApplication}', tuple(applications))
        for i in range(len(listData)//6):
            listValue = listData[i*6:(i+1)*6]
            cur.execute(
                f'update trainee set fullName = ?, post = ?, gender = ?, snils = ?, age = ?, prefStudyingProgram = ? where idInd = {i} and id = {idApplication}',
                tuple(listValue)
            )
        con.commit()
        return HttpResponseRedirect(f'/applications/list/clients?idApplication={idApplication}')
    else:
        allApplications = list(cur.execute(f'SELECT * FROM applications where id = {idApplication}').fetchone())
        allApplications = applicationsTranslate(allApplications)
        allApplicationsForm = [allApplications[1]]+allApplications[5:8]
        allApplications = [allApplications[0]]+allApplications[2:5]+allApplications[8:]
        form = ApplicationsForm(my_arg=allApplicationsForm)
        listClient = list(cur.execute(f'SELECT * FROM trainee where id = {allApplications[-1]}').fetchall())
        formsClients = []
        for i in range(len(listClient)):
            formsClients.append(ClientListForm(my_arg=listClient[i][1:], prefix=i))
        return render(request, 'listClients.html', {'form': form, 'formsClients': formsClients, 'allApplications': allApplications})
    
def installAccount(request, id):
    import docx, sqlite3, json
    doc = docx.Document()
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    
    cur.execute(f'''update applications set status = 1 where id = {id}''')
    
    applicationOne = cur.execute(f'SELECT * FROM applications where id = {id}').fetchone()
    client = cur.execute(f'SELECT * FROM clients where id = {applicationOne[-1]}').fetchone()
    par1 = doc.add_paragraph(f'Заказчик: {client[1]}').bold = True
    par2 = doc.add_paragraph(f'Юридический адрес ЗАКАЗЧИКА: {client[-1]}')
    par3 = doc.add_paragraph(f'ИНН ')
    s1 = par3.add_run(str(client[2]))
    s1.bold = True
    par3.add_run(f' КПП ')
    s2 = par3.add_run(str(client[3]))
    s2.bold = True
    par4 = doc.add_paragraph(f'Исполнитель: ')
    par4.bold = True
    with open('company.json') as json_file:
        data = json.load(json_file)
        par4.add_run(data['name'])
        par5 = doc.add_paragraph(f"Адрес {data['address']}")
        par6 = doc.add_paragraph(f"ИНН/КПП {data['inn']} / {data['kpp']}")
        par7 = doc.add_paragraph(f"Бик {data['bankAccount']}")
        supervisor = data['supervisor']
    allUsers = cur.execute('SELECT prefStudyingProgram FROM trainee').fetchall()
    allPrograms = [i[0] for i in allUsers]
    reqText = 'SELECT name, price, prefix FROM studyingPrograms WHERE '
    for i in allPrograms:
        reqText += f"prefix = '{i}' or "
    reqText = reqText[:-4]
    listPrograms = cur.execute(reqText).fetchall()
    setPrograms = set(allPrograms)
    table = doc.add_table(rows=len(setPrograms) + 2, cols=6)
    table.style = 'Light Shading Accent 1'
    summ = 0
    for program in range(len(listPrograms)):
        table.cell(program+1, 0).text = str(program+1)
        table.cell(program+1, 1).text = listPrograms[program][0]
        table.cell(program+1, 2).text = 'чел.'
        countProg = allPrograms.count(listPrograms[program][-1])
        table.cell(program+1, 3).text = str(countProg)
        table.cell(program+1, 4).text = str(listPrograms[program][1])
        table.cell(program+1, 5).text = str(int(listPrograms[program][1])*countProg)
        summ += int(listPrograms[program][1])*countProg
    table.cell(len(setPrograms)+1, 0).merge(table.cell(len(setPrograms)+1, 4))
    table.cell(len(setPrograms)+1, 0).text = 'Итого'
    table.cell(len(setPrograms)+1, 5).text = str(summ)
    table.cell(0, 0).text = ''
    table.cell(0, 1).text = 'Наименование товара'
    table.cell(0, 2).text = 'Единица измерения'
    table.cell(0, 3).text = 'Количество'
    table.cell(0, 4).text = 'Цена, руб.'
    table.cell(0, 5).text = 'Сумма, руб.'
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=download.docx'
    doc.save(response)
    con.commit()
    return response

def protocols(request):
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    allProtocols = cur.execute('SELECT * FROM protocols').fetchall()
    nList = []
    for protocol in range(len(allProtocols)):
        listR = list(allProtocols[protocol])
        listR[5] = (cur.execute(f'select name from users where id = {listR[5]}').fetchone()[0])
        nList.append(listR)
    return render(request, 'protocols.html', {'allProtocols': nList})

def protocolsClients(request):
    idProtocols = int(request.GET.get('id'))
    import sqlite3
    con = sqlite3.connect('educationalDate.db')
    cur = con.cursor()
    if request.method == 'POST':
        listData = list(request.POST.values())[1:]
        protocol = [listData[0]]
        if listData[-1] == "1":
            idTrainee = int(cur.execute(f'SELECT MAX(id) FROM protocolsClients WHERE idProtocols = {idProtocols}').fetchone()[0]) + 1
            countTrainee = int(cur.execute(f'SELECT countTrainee FROM protocols WHERE id = {idProtocols}').fetchone()[0]) + 1
            cur.execute(f'''INSERT INTO protocolsClients values ({idTrainee}, {idProtocols}, NULL, NULL, NULL, NULL, NULL)''')
            cur.execute(f"update protocols set countTrainee = {countTrainee} WHERE id = {idProtocols}")
        listData = listData[1:-1]
        nameClient = cur.execute(f'SELECT name FROM studyingPrograms where id = {protocol[0]}').fetchone()[0]
        protocol.append(nameClient)
        cur.execute(
            f'update protocols set idStudyingProgram = ?, nameStudyingProgram = ? where id = {idProtocols}',
            tuple(protocol)
        )
        for i in range(len(listData) // 4):
            listValue = listData[i * 4:(i + 1) * 4]
            cur.execute(
                f'update protocolsClients set fullName = ?, idClient = ?, snils = ?, result = ? where id = {i} and idProtocols = {idProtocols}',
                tuple(listValue)
            )
        con.commit()
        return HttpResponseRedirect(f'/protocols/clients?id={idProtocols}')
    else:
        allProtocols = list(cur.execute(f'SELECT * FROM protocols where id = {idProtocols}').fetchone())
        allProtocols[5] = cur.execute(f'select name from users where id = {allProtocols[5]}').fetchone()[0]
        allApplicationsForm = [allProtocols[1]]
        allProtocols = [allProtocols[0]] + allProtocols[3:]
        form = ProtocolsForm(my_arg=allApplicationsForm)
        listClient = list(cur.execute(f'SELECT * FROM protocolsClients where idProtocols = {allProtocols[0]}').fetchall())
        formsClients = []
        for i in range(len(listClient)):
            formsClients.append(ProtocolsClientsForm(my_arg=listClient[i][1:], prefix=i))
        return render(request, 'procolsClients.html',
                      {'form': form, 'formsClients': formsClients, 'allProtocols': allProtocols})


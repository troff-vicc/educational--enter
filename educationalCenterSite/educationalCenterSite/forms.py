from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label_suffix=False, label='', max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Логин',
                                                        'autocomplete': "off"}))
    password = forms.CharField(label_suffix=False, label='', max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Пароль',
                                                            'autocomplete': "off"}))
    
class UsersAdmin(forms.Form):
    admin = forms.BooleanField(label_suffix=False, label='')

class EmployeesForm(forms.Form):
    fullName = forms.CharField(label='ФИО', max_length=100)
    position = forms.CharField(label='Должность', max_length=100)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(EmployeesForm, self).__init__(*args, **kwargs)
            listFields = list(self.fields.values())
            for i in range(len(listFields)):
                listFields[i].widget = forms.TextInput(attrs={'value': my_arg[i]})
        else:
            super(EmployeesForm, self).__init__(*args, **kwargs)
            
class GroupReportsForm(forms.Form):
    nameGroup = forms.CharField(label='Имя группы', max_length=100)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(GroupReportsForm, self).__init__(*args, **kwargs)
            listFields = list(self.fields.values())
            for i in range(len(listFields)):
                listFields[i].widget = forms.TextInput(attrs={'value': my_arg[i]})
        else:
            super(GroupReportsForm, self).__init__(*args, **kwargs)
            
class ClientsForm(forms.Form):
    name = forms.CharField(label='Клиент', max_length=100)
    inn = forms.IntegerField(label='ИНН')
    kpp = forms.IntegerField(label='КПП')
    address = forms.CharField(label='Адрес', max_length=256)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(ClientsForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget = forms.TextInput(attrs={'value': my_arg[0]})
            self.fields['inn'].widget = forms.NumberInput(attrs={'value': my_arg[1]})
            self.fields['kpp'].widget = forms.NumberInput(attrs={'value': my_arg[2]})
            self.fields['address'].widget = forms.TextInput(attrs={'value': my_arg[3]})
        else:
            super(ClientsForm, self).__init__(*args, **kwargs)

class StudyingProgramForm(forms.Form):
    import sqlite3
    conn = sqlite3.connect('educationalDate.db')
    cur = conn.cursor()
    listGroup = cur.execute('select * from groupReports').fetchall()
    tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
    boolFields = ((0, 'Нет'), (1, 'Да'))
    resulChoose = ((0, 'Зачет'), (1, 'Незачет'), (2, 'Пропуск'))
    name = forms.CharField(label='Имя', max_length=256)
    prefix = forms.CharField(label='Префикс', max_length=50)
    landing = forms.ChoiceField(label = 'Признак выгрузки', choices = boolFields)
    nameGroupReports = forms.ChoiceField(label='Группа отчётов', choices = tupleGroup)
    textForReport = forms.CharField(label='Текст для протокола', max_length=256)
    price =(forms.FloatField(label='Цена по умолчанию'))
    fullName = forms.ChoiceField(label = 'ФИО', choices = boolFields)
    client = forms.ChoiceField(label = 'Клиент', choices = boolFields)
    snils = forms.ChoiceField(label = 'СНИЛС', choices = boolFields)
    registerNumber = forms.ChoiceField(label = 'Номер реестра', choices = boolFields)
    resultOf = forms.ChoiceField(label = 'Результат проведения', choices = boolFields)
    signature =forms.ChoiceField(label = 'Подпись', choices = boolFields)
    result = forms.ChoiceField(label = 'Результат', choices = resulChoose)
    def __init__(self, *args, **kwargs):
        t = False
        if kwargs:
            t = True
            my_arg = kwargs.pop('my_arg')
        super(StudyingProgramForm, self).__init__(*args, **kwargs)
        import sqlite3
        conn = sqlite3.connect('educationalDate.db')
        cur = conn.cursor()
        listGroup = cur.execute('select * from groupReports').fetchall()
        tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
        self.fields['nameGroupReports'].choices = tupleGroup
        if t:
            self.fields['name'].widget = forms.TextInput(attrs={'value': my_arg[0]})
            self.fields['prefix'].widget = forms.TextInput(attrs={'value': my_arg[1]})
            self.initial['landing'] = my_arg[2]
            self.initial['nameGroupReports'] = my_arg[3]
            self.fields['textForReport'].widget = forms.TextInput(attrs={'value': my_arg[4]})
            self.fields['price'].widget = forms.NumberInput(attrs={'value': my_arg[5]})
            self.initial['fullName'] = my_arg[6]
            self.initial['client'] = my_arg[7]
            self.initial['snils'] = my_arg[8]
            self.initial['registerNumber'] = my_arg[9]
            self.initial['resultOf'] = my_arg[10]
            self.initial['signature'] = my_arg[11]
            self.initial['result'] = my_arg[12]
            
class ApplicationsForm(forms.Form):
    import sqlite3
    conn = sqlite3.connect('educationalDate.db')
    cur = conn.cursor()
    boolFields = ((0, 'Нет'), (1, 'Да'))
    listGroup = cur.execute('select * from clients').fetchall()
    tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
    idClient = forms.ChoiceField(label='Клиент', choices = tupleGroup)
    postpaid = forms.ChoiceField(label='Признак постоплаты', choices = boolFields)
    receiptPayment = forms.ChoiceField(label = 'Признак поступления оплаты', choices = boolFields)
    def __init__(self, *args, **kwargs):
        t = False
        if kwargs:
            t = True
            my_arg = kwargs.pop('my_arg')
        super(ApplicationsForm, self).__init__(*args, **kwargs)
        import sqlite3
        conn = sqlite3.connect('educationalDate.db')
        cur = conn.cursor()
        listGroup = cur.execute('select * from clients').fetchall()
        tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
        self.fields['idClient'].choices = tupleGroup
        if t:
            self.initial['idClient'] = my_arg[0]
            self.initial['postpaid'] = my_arg[1]
            self.initial['receiptPayment'] = my_arg[2]

class ClientListForm(forms.Form):
    import sqlite3
    conn = sqlite3.connect('educationalDate.db')
    cur = conn.cursor()
    listPrograms = cur.execute('select id, prefix from studyingPrograms').fetchall()
    tuplePrograms = tuple([(i[0], i[1]) for i in listPrograms])
    boolFields = ((0, 'Мужчина'), (1, 'Женщина'))
    fullName = forms.CharField(label_suffix=False, label='', max_length =100)
    post = forms.CharField(label_suffix=False, label='', max_length =100)
    gender = forms.ChoiceField(label_suffix=False, label='', choices=boolFields)
    snils = forms.IntegerField(label_suffix=False, label='')
    age = forms.IntegerField(label_suffix=False, label='')
    prefStudyingProgram = forms.ChoiceField(label_suffix=False, label='', choices=tuplePrograms)
    def __init__(self, *args, **kwargs):
        t = False
        if kwargs:
            t = True
            my_arg = kwargs.pop('my_arg')
        super(ClientListForm, self).__init__(*args, **kwargs)
        import sqlite3
        conn = sqlite3.connect('educationalDate.db')
        cur = conn.cursor()
        listPrograms = cur.execute('select id, prefix from studyingPrograms').fetchall()
        tuplePrograms = tuple([(i[0], i[1]) for i in listPrograms])
        self.fields['prefStudyingProgram'].choices = tuplePrograms
        if t:
            self.fields['fullName'].widget = forms.TextInput(attrs={'value': my_arg[0]})
            self.fields['post'].widget = forms.TextInput(attrs={'value': my_arg[1]})
            self.initial['gender'] = my_arg[2]
            self.fields['snils'].widget = forms.NumberInput(attrs={'value': my_arg[3]})
            self.fields['age'].widget = forms.NumberInput(attrs={'value': my_arg[4]})
            self.initial['prefStudyingProgram'] = my_arg[5]

class ProtocolsForm(forms.Form):
    import sqlite3
    conn = sqlite3.connect('educationalDate.db')
    cur = conn.cursor()
    listGroup = cur.execute('select * from studyingPrograms').fetchall()
    tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
    idClient = forms.ChoiceField(label='Программа обучения', choices = tupleGroup)
    def __init__(self, *args, **kwargs):
        t = False
        if kwargs:
            t = True
            my_arg = kwargs.pop('my_arg')
        super(ProtocolsForm, self).__init__(*args, **kwargs)
        import sqlite3
        conn = sqlite3.connect('educationalDate.db')
        cur = conn.cursor()
        listGroup = cur.execute('select * from studyingPrograms').fetchall()
        tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
        self.fields['idClient'].choices = tupleGroup
        if t:
            self.initial['idClient'] = my_arg[0]

class ProtocolsClientsForm(forms.Form):
    import sqlite3
    conn = sqlite3.connect('educationalDate.db')
    cur = conn.cursor()
    listGroup = cur.execute('select * from clients').fetchall()
    tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
    fullName = forms.CharField(label='Имя', max_length =100)
    idClients = forms.ChoiceField(label='Клиент', choices=tupleGroup)
    snils = forms.IntegerField(label='Снилс')
    result = forms.CharField(label='Результат', max_length=100)
    def __init__(self, *args, **kwargs):
        t = False
        if kwargs:
            t = True
            my_arg = kwargs.pop('my_arg')
        super(ProtocolsClientsForm, self).__init__(*args, **kwargs)
        import sqlite3
        conn = sqlite3.connect('educationalDate.db')
        cur = conn.cursor()
        listGroup = cur.execute('select * from clients').fetchall()
        tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
        self.fields['idClients'].choices = tupleGroup
        if t:
            self.fields['fullName'].widget = forms.TextInput(attrs={'value': my_arg[0]})
            self.initial['idClients'] = my_arg[1]
            self.fields['snils'].widget = forms.NumberInput(attrs={'value': my_arg[2]})
            self.fields['result'].widget = forms.TextInput(attrs={'value': my_arg[3]})
            
class CompanyForm(forms.Form):
    name = forms.CharField(label='Наименование', max_length=256)
    inn = forms.IntegerField(label='ИНН')
    kpp = forms.IntegerField(label='КПП')
    bankAcaunt = forms.IntegerField(label='Банковский cчёт')
    address = forms.CharField(label='Адрес', max_length=256)
    supervisor = forms.CharField(label='Руководитель', max_length=256)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(CompanyForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget = forms.TextInput(attrs={'value': my_arg[0]})
            self.fields['inn'].widget = forms.NumberInput(attrs={'value': my_arg[1]})
            self.fields['kpp'].widget = forms.NumberInput(attrs={'value': my_arg[2]})
            self.fields['bankAcaunt'].widget = forms.NumberInput(attrs={'value': my_arg[3]})
            self.fields['address'].widget = forms.TextInput(attrs={'value': my_arg[4]})
            self.fields['supervisor'].widget = forms.TextInput(attrs={'value': my_arg[5]})
        else:
            super(CompanyForm, self).__init__(*args, **kwargs)
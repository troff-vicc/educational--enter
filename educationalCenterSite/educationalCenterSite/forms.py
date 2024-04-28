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
    nameClient = forms.CharField(label='Клиент', max_length=100)
    inn = forms.CharField(label='ИНН', max_length=50)
    kpp = forms.CharField(label='КПП', max_length=50)
    address = forms.CharField(label='Адрес', max_length=256)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(ClientsForm, self).__init__(*args, **kwargs)
            listFields = list(self.fields.values())
            for i in range(len(listFields)):
                listFields[i].widget = forms.TextInput(attrs={'value': my_arg[i]})
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
    landing = forms.CharField(label='Признак выгрузки', max_length=50)
    nameGroupReports = forms.ChoiceField(label='Группа отчётов', choices = tupleGroup)
    textForReport = forms.CharField(label='Текст для протокола', max_length=256)
    price =forms.CharField(label='Цена по умолчанию', max_length=100)
    fullName = forms.ChoiceField(label = 'ФИО', choices = boolFields)
    client = forms.ChoiceField(label = 'Клиент', choices = boolFields)
    snils = forms.ChoiceField(label = 'СНИЛС', choices = boolFields)
    registerNumber = forms.ChoiceField(label = 'Номер реестра', choices = boolFields)
    resultOf = forms.ChoiceField(label = 'Результат проведения', choices = boolFields)
    signature =forms.ChoiceField(label = 'Подпись', choices = boolFields)
    result = forms.ChoiceField(label = 'Результат', choices = resulChoose)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(StudyingProgramForm, self).__init__(*args, **kwargs)
            listFields = list(self.fields.values())
            for i in range(len(listFields)):
                listFields[i].widget = forms.TextInput(attrs={'value': my_arg[i]})
        else:
            super(StudyingProgramForm, self).__init__(*args, **kwargs)

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
    countEmployees = forms.CharField(label = 'Количество работников', max_length = 100)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(ApplicationsForm, self).__init__(*args, **kwargs)
            self.initial['idClient'] = my_arg[0]
            self.initial['postpaid'] = my_arg[1]
            self.initial['receiptPayment'] = my_arg[2]
            self.fields['countEmployees'].widget = forms.TextInput(attrs={'value': my_arg[3]})
        else:
            super(ApplicationsForm, self).__init__(*args, **kwargs)

class ClientListForm(forms.Form):
    boolFields = ((0, 'Мужчина'), (1, 'Женщина'))
    fullName = forms.CharField(label_suffix=False, label='', max_length =100)
    post = forms.CharField(label_suffix=False, label='', max_length =100)
    gender = forms.ChoiceField(label_suffix=False, label='', choices=boolFields)
    snils = forms.CharField(label_suffix=False, label='', max_length=100)
    age = forms.CharField(label_suffix=False, label='', max_length =100)
    prefStudyingProgram = forms.CharField(label_suffix=False, label='', max_length =100)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(ClientListForm, self).__init__(*args, **kwargs)
            self.fields['fullName'].widget = forms.TextInput(attrs={'value': my_arg[0]})
            self.fields['post'].widget = forms.TextInput(attrs={'value': my_arg[1]})
            self.initial['gender'] = my_arg[2]
            self.fields['snils'].widget = forms.TextInput(attrs={'value': my_arg[3]})
            self.fields['age'].widget = forms.TextInput(attrs={'value': my_arg[4]})
            self.fields['prefStudyingProgram'].widget = forms.TextInput(attrs={'value': my_arg[5]})
        else:
            super(ClientListForm, self).__init__(*args, **kwargs)

class ProtocolsForm(forms.Form):
    import sqlite3
    conn = sqlite3.connect('educationalDate.db')
    cur = conn.cursor()
    listGroup = cur.execute('select * from studyingPrograms').fetchall()
    tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
    idClient = forms.ChoiceField(label='Программа обучения', choices = tupleGroup)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(ProtocolsForm, self).__init__(*args, **kwargs)
            self.initial['idClient'] = my_arg[0]
        else:
            super(ProtocolsForm, self).__init__(*args, **kwargs)

class ProtocolsClientsForm(forms.Form):
    import sqlite3
    conn = sqlite3.connect('educationalDate.db')
    cur = conn.cursor()
    listGroup = cur.execute('select * from clients').fetchall()
    tupleGroup = tuple([(i[0], i[1]) for i in listGroup])
    fullName = forms.CharField(label='Имя', max_length =100)
    idClients = forms.ChoiceField(label='Клиент', choices=tupleGroup)
    snils = forms.CharField(label='Снилс', max_length=100)
    result = forms.CharField(label='Результат', max_length=100)
    def __init__(self, *args, **kwargs):
        if kwargs:
            my_arg = kwargs.pop('my_arg')
            super(ProtocolsClientsForm, self).__init__(*args, **kwargs)
            self.fields['fullName'].widget = forms.TextInput(attrs={'value': my_arg[1]})
            self.initial['idClients'] = my_arg[2]
            self.fields['snils'].widget = forms.TextInput(attrs={'value': my_arg[3]})
            self.fields['result'].widget = forms.TextInput(attrs={'value': my_arg[4]})
        else:
            super(ProtocolsClientsForm, self).__init__(*args, **kwargs)
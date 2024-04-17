from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm

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
    allUsers = cur.execute('SELECT * FROM users').fetchall()
    return render(request, 'users.html', {'allUsers': allUsers})
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

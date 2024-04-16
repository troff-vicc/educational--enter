from django.http import HttpResponseRedirect
from django.shortcuts import render

def index():
    return HttpResponseRedirect('/information')
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
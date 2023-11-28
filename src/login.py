# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:12:08 2023

@author: agonjur
"""

from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

@app.route('/')
def login():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario.
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('log.html', data=insertObject)

@app.route('/registro/<string:id>')
def registro():
    cursor = db.database.cursor()
    user = request.form['user']
    password = request.form['password']
    conf_pass = request.form['conf_pass']
    if user and password and conf_pass:
        if password == conf_pass:    
            sql = "INSERT INTO users (user, password) VALUES (%s, %s);"
            
if __name__ == '__main__':
    app.run(debug=True, port=4000)
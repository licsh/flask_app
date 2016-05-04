#coding=utf-8

from app import app

@app.route('/login')
def login():
	return '<h1>李春生</h1>'
from flask import json
import os

jsonheaders = {
	'Content-Type': 'application/json',
	'Accept': 'application/json'
}

def test_home(client):
	res = client.get('/')
	assert b'<h1>Oishi Sushi</h1>' in res.data

def test_favicon(client):
	res = client.get('/favicon.ico')
	assert res.status_code == 200

def test_menu(client):
	res = client.get('/menu/')
	assert res.status_code == 200

def test_api_add(client):
	res = client.post('/api/order/add',
		data=json.dumps({'id': 'Maki'}), headers=jsonheaders
	)
	client.post('/api/order/add',
		data=json.dumps({'id': 'Temaki'}), headers=jsonheaders
	)
	assert res.status_code == 200
	res2 = client.get('/api/order/')
	assert res2.json['Maki'] == 1
	res2 = client.get('/api/order/total')
	assert res2.json['total'] == 2

def test_api_remove(client):
	res = client.post('/api/order/remove',
		data=json.dumps({'id': 'Maki'}), headers=jsonheaders
	)
	assert res.status_code == 200
	client.post('/api/order/add',
		data=json.dumps({'id': 'Maki'}), headers=jsonheaders
	)
	res = client.post('/api/order/remove',
		data=json.dumps({'id': 'Maki'}), headers=jsonheaders
	)
	assert res.status_code == 200
	res2 = client.get('/api/order/')
	assert res2.json == {}

def test_api_emptycart(client):
	res = client.get('/api/order/')
	assert res.json == {}
	res = client.get('/api/order/total')
	assert res.json['total'] == 0

def test_db(client):
	assert os.path.exists('test.db')

def test_api_items(client):
	res = client.get('/api/item/')
	assert res.status_code == 200

def test_api_newitem(client):
	res = client.post('/api/item/new',
		data=json.dumps({'name': ''.join(['a'] * 410), 'price': '200'}), headers=jsonheaders
	)
	assert res.status_code == 400 and b'Error: Name' in res.data
	res = client.post('/api/item/new',
		data=json.dumps({'name': 'Shrimp tempura', 'price': 'aaa'}), headers=jsonheaders
	)
	assert res.status_code == 400 and b'Error: Invalid' in res.data
	res = client.post('/api/item/new',
		data=json.dumps({'name': 'Shrimp tempura', 'price': '200'}), headers=jsonheaders
	)
	assert res.status_code == 200
	res = client.get('/api/item/')
	assert b'Shrimp tempura' in res.data

from flask import json

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

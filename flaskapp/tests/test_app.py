def test_test(client):
	res = client.get('/')
	assert b'<h1>Testing</h1>' in res.data
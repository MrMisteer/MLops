from app import app, items


def setup_function():
    items.clear()


def test_index_returns_ok():
    app.testing = True
    with app.test_client() as client:
        response = client.get('/')

    assert response.status_code == 200
    assert b'Items' in response.data


def test_add_endpoint_redirects_and_adds_item():
    app.testing = True
    with app.test_client() as client:
        response = client.post('/add', 
                               data={'item': 'Test Task'}, 
                               follow_redirects=True)

    assert response.status_code == 200
    assert b'Test Task' in response.data

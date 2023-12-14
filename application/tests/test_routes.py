from application import create_app

app = create_app()

def test_home_route():
    response = app.test_client().get('/')
    assert response.status_code == 200    

def test_view_route():
    response = app.test_client().get('/view')
    assert response.status_code == 200
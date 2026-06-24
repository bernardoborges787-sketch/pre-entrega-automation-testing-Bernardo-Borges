import requests

headers = {
 "x-api-key": "pub_78197f6e3771f98395f3cfe72afdd0b86a557a89a025b2b59b26bfbfb03f1afa"
        
}

def test_loging_valido():
 body = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
 }
  
 response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
 
 assert response.status_code == 200 
 
 
def test_loging_sin_password():
 body = {
    "email": "eve.holt@reqres.in",
   
 }
 
 response = requests.post("https://reqres.in/api/login", headers=headers, json=body)
 
 assert response.status_code == 400
 
 
def test_create_user():    
    
    body = {
        "name": "morpheus",
        "email": "eve.holt@reqres.in",
        "password": "123456"
    }
 
    
    response = requests.post("https://reqres.in/api/users", headers=headers, json=body)
    data = response.json()   


    assert response.status_code == 201    
    assert data["name"] == body["name"]  
    


def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)
     
         
    assert response.status_code == 204
    
def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)
     
         
    assert response.status_code == 204
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() < 1, "La respuesta tardó más de 1 segundo"
      
    

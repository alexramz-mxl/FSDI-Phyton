from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask"


@app.get("/test")
def home():
    return "This is a test page"

@app.get("/about")
def test_about():
    me = {"name": "Alexis"}
    return json.dumps(me)

@app.get("/api/versions")
def versions():
    versions = {"version":"dog", "name":"lukas", "description":"the real newest version"}
    return json.dumps(versions)

@app.get("/admin")
def admin():
    return "Hello I am the admin"

products = []
@app.get("/api/products")
def get_products():
    return json.dumps(products)
@app.post("api/products")
def save_products():
    prod= request.get_json()

@app.post("/api/products")
def save_products():
    prod = request.get_json()
    print(prod)
    #mock save
    products.append(prod)
    return json.dumps(prod)

@app.put("/api/products")
def update_products(index):
    updated_product = request.get_json()
    if 0<= index < len(products):
       products[0] = updated_product
       return json.dumps(updated_product)
    else:
       return "That index doesn t exist"

@app.delete("/api/products/<int:index>")
def delete_products(index):
    deleted_product = request.get_json()
    if 0<= index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else:
        return "That product was deleted"
      

@app.delete("/api/products")
def patch_products(index):
    updated_field = request.get_json()
    if 0<= index < len(products):
       products(index).update(updated_field)
       return json.dumps(updated_field)
    else:
       return "That product was deleted"

#use the same logic but qremember that you need
#use list.pop
#create the logic for the delete API
    
app.run(debug=True)

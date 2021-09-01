from flask import Flask,jsonify,request
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'Cart',
    'host': 'mongodb+srv://redmaniac:redmaniac@cart.z9rdo.mongodb.net/Cart?retryWrites=true&w=majority'
}
db = MongoEngine(app)

class Items(db.Document):
    item_id = db.IntField()
    price = db.FloatField()
    qty = db.IntField()

    def to_json(self):
        return {
            "item_id" : self.item_id,
            "price" : self.price,
            "qty" : self.qty
        }

@app.route('/getitem', methods=['GET'])
def getitems():
    items = []
    for item in Items.objects():
        items.append(item.to_json())
    return jsonify({'result' : items})

@app.route('/postitem', methods=['POST'])
def postitem():
    item_id = request.json['item_id']
    price = request.json['price']
    qty = request.json['qty']

    item = Items(item_id = item_id,
    price = price,
    qty = qty)
    item.save()

    items = []
    for item in Items.objects():
        items.append(item.to_json())
    return jsonify({'result' : items})

@app.route('/updateitem', methods=['PATCH'])
def upditem():
    qty = request.json['qty']

    item = Items.objects(item_id = 1)
    item.update(qty = qty)

    items = []
    for item in Items.objects():
        items.append(item.to_json())
    return jsonify({'result' : items})

@app.route('/deleteitem', methods=['DELETE'])
def delitem():

    item = Items.objects(item_id = 1)
    item.delete()

    items = []
    for item in Items.objects():
        items.append(item.to_json())
    return jsonify({'result' : items})


if __name__== "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)

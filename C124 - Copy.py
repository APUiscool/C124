from flask import Flask,jsonify,request
app=Flask(__name__)
data=[
    {
        "id":1,
        "contact":u"9900229933",
        "name":u"Random1",
        "done":False
    },
    {
        "id":2,
        "contact":u"9900222255",
        "name":u"Random2",
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "Status":"ERROR",
            "Message":"Please provide the data"
        },400)
    task={
        "id":data[-1]['id'] + 1 ,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
         }
    data.append(task)
    return jsonify({
        "status":"Sucess",
        "message":"Data added sucessfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":data
    })
if(__name__=="__main__"):
    app.run()
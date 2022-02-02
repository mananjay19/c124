from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/')
def helloworld():
    return 'hello world'


tasks = [
    {
        'id':1,
        'title':u'buy grocery',
        'description':u'milk,butter,cheese,fruit,rice,oil',
        'done':False
    },
     {
        'id':2,
        'title':u'complete homework',
        'description':u'maths excersice,science chapter, python project',
        'done':False
    }
]
@app.route('/get-data')
def gettask():
    return jsonify({
        'data':tasks
    })
@app.route('/add-data',methods=['POST'])
def addtask():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data in json format'
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
            'status':'success',
            'message':'task added successfully'
        },400)
if(__name__=='__main__'):
    app.run(debug=True)
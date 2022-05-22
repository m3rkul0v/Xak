from flask import Flask, request, jsonify
import pickle
import pandas

app = Flask(__name__)
list = []


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    # test2 = '[{"Time":888,"Mood":2,"Reason":1,"Category":2,"Result(%)":20}]'
    data = request.json
    list.append(data)
    # df_test = pandas.read_json(data)
    df_test = pandas.DataFrame(data)
    print(df_test)
    a = loaded_model.predict(df_test)
    print(a)
    print(list)
    print(len(list))
    while len(list) < 15:
        {
            #Sending data to DF only
        }

    return jsonify(str(a))
from flask import Flask, request, jsonify
import pickle
import pandas
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'] )
def hello_world():
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    data = request.json
    print(type(data))
    df_test = pandas.DataFrame(data)
    print(df_test)
    a = loaded_model.predict(df_test)
    print(a)
    return jsonify(str(a))




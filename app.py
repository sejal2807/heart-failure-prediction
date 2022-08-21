from flask import Flask , request , render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('heart_failure_model.pickle','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['Get','Post'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction == 0:
        return render_template('index.html',
                               response='High chances of failure'.format(prediction),
                               )
    else:
        return render_template('index.html',
                               response='Low chances of failure'.format(prediction),
                               )


if __name__ == "__main__":
    app.run(debug=True)

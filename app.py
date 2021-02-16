from flask import Flask, render_template, request
from sample_temps import FtoCtemp
# from temp_calculations.temp_conversion import Unit

application = Flask(__name__)

@application.route("/")
@application.route("/index")
@application.route('/result', methods=['GET', 'POST'])
@application.route('/sample_temps/ftemp.py')

def input():
    if request.method == 'POST': 
        number = request.form['number']
        unit = request.form['unit']
        target = request.form['target']
        response = request.form['response']
        return render_template('result.html', number=number, unit=unit, target=target, response=response)
    return render_template('index.html')


# run the app
if __name__ == "__main__": 
    # application.run()
    application.run(debug=True, port=8080)
from flask import Flask, render_template, request
from areacircle import calculate_area_circle
from areatriangle import calculate_area_triangle

app = Flask(__name__, static_url_path='', static_folder="D:\Flask\Flask_Intro\static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/areaoftriangle')
def areaoftriangle():
    return render_template('areaoftriangle.html')

@app.route('/areaofcircle')
def areaofcircle():
    return render_template('areaofcircle.html')

@app.route('/contacts')
def contact():
    return render_template('contacts.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaofcircle', methods=['GET', 'POST'])
def areaofacircle():
    area = None
    if request.method == 'POST':
        input_radius = request.form.get('Inputfloat', '')
        try:
            input_radius = int(input_radius)
            area = calculate_area_circle(input_radius)
        except ValueError as e:
            area = str(e)
    return render_template('areaofcircle.html', area=area)

@app.route('/areaoftriangle', methods=['POST'])
def areaofatriangle():
    try:
        input_base = float(request.form.get('inputBase', ''))
        input_height = float(request.form.get('inputHeight', ''))

        area = calculate_area_triangle(input_base, input_height)
    except ValueError as e:
        area = str(e)
    return render_template('areaoftriangle.html', area=area)

if __name__ == "__main__":
    app.run(debug=True)
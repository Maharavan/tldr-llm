from flask import Flask, render_template,request
from llm import summarize_text
app = Flask(__name__, template_folder='templates/tldm',static_folder='templates/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        text = request.form.get('text')
        result = summarize_text(text)
        return render_template('summarize_result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
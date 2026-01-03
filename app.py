from flask import Flask, render_template,request
from llm import summarize_text
app = Flask(__name__, template_folder='templates/tldm',static_folder='templates/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Generate Web page for AI Summarizer
    """
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        text = request.form.get('text')
        length = request.form.get('length')
        style = request.form.get('style')
        language = request.form.get('language')
        structure = request.form.get('structure')
        result = summarize_text(text,length,style,language,structure)
        return render_template('summarize_result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
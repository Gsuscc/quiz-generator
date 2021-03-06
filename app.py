from flask import Flask, request, render_template, jsonify
import connection


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/quiz', methods=['GET'])
def start_quiz():
    questions = connection.get_all_questions()
    return jsonify(questions)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000,
    )

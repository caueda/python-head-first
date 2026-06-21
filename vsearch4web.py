from flask import Flask, render_template, request
from markupsafe import escape
from vsearch import search4letters

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log','a') as log:
        # print(req.form,file=log, end='|')
        # print(req.remote_addr, file=log, end='|')
        # print(req.user_agent, file=log, end='|')
        # print(res, file=log)
        contents = log.readlines()
        print(' '.join(contents))


@app.route('/search4', methods=['POST'])
def search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html', the_title='Search Results', result=result,
                           phrase=phrase, letters=letters)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        #contents = log.read()
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    title=['Form Data', 'Remote Addr', 'User Agent', 'Results']
    return render_template('viewlog.html', the_title='View Log', the_row_titles=title, the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)

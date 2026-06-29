from flask import Flask, render_template, request
from markupsafe import escape
from vsearch import search4letters
from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig'] = {
        'host': '127.0.0.1',
        'user':'vsearch',
        'password':'welcome1',
        'database':'vsearchlogDB',
    }

def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.string,
                              res))

@app.route('/search4', methods=['POST'])
def search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html', the_title='Search Results', the_results=result,
                           phrase=phrase, letters=letters)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_log() -> 'html':
    contents = []
    # with open('vsearch.log') as log:
    #     #contents = log.read()
    #     for line in log:
    #         contents.append([])
    #         for item in line.split('|'):
    #             contents[-1].append(escape(item))
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = 'select phrase, letters, ip, browser_string, results from log'
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    title=['Phrase', 'Letters', 'Remote Addr', 'User Agent', 'Results']
    return render_template('viewlog.html', the_title='View Log', the_row_titles=title, the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)

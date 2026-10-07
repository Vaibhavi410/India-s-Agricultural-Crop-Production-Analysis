import os

from flask import Flask, render_template, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder='Template',
    static_folder='Static',
    static_url_path='/assets'
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<path:page_name>')
def serve_html_page(page_name):
    if page_name == 'favicon.ico':
        return ('', 404)

    page_name = page_name.rstrip('/')

    if page_name in ('', 'index', 'index.html'):
        return home()

    if '.' not in page_name:
        candidate = f'{page_name}.html'
    else:
        candidate = page_name

    candidate_path = os.path.join(BASE_DIR, candidate)
    if os.path.isfile(candidate_path):
        return send_from_directory(BASE_DIR, candidate)

    return ('Page not found', 404)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    request_hero = request.form.get('request_hero')
    catatan_penjoki = request.form.get('catatan_penjoki')
    star_order = request.form.get('star_order')
    diamond_order = request.form.get('diamond_order')

    # Render the response.html template with form data
    return render_template(
        'response.html',
        name=name,
        email=email,
        password=password,
        request_hero=request_hero,
        catatan_penjoki=catatan_penjoki,
        star_order=star_order,
        diamond_order=diamond_order
    )

if __name__ == '__main__':
    app.run(debug=True)
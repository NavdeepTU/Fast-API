from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with a simple form
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <h2>Enter a number to see its multiplication table:</h2>
    <form method="POST">
        <input type="number" name="number" required>
        <input type="submit" value="Generate Table">
    </form>
    {% if table %}
        <h3>Multiplication Table for {{ number }}:</h3>
        <ul>
            {% for line in table %}
                <li>{{ line }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    table = []
    number = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
        except ValueError:
            table = ["Invalid input. Please enter a valid number."]
    return render_template_string(HTML_TEMPLATE, table=table, number=number)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
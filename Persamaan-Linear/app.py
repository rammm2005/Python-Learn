from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__, template_folder='components', static_folder='assets')

def solve_linear_equations(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            n = int(request.form['variables'])
            A = []
            for i in range(n):
                row = list(map(float, request.form[f'row{i+1}'].split()))
                A.append(row)
            b = list(map(float, request.form['vector'].split()))
            A = np.array(A)
            b = np.array(b)
            solution = solve_linear_equations(A, b)
            return render_template('index.html', solution=solution, n=n)
        except ValueError:
            return render_template('index.html', error="Invalid input. Please enter numbers only.")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

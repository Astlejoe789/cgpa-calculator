from flask import Flask, render_template, request

app = Flask(__name__)

# Grade to point mapping
grade_points = {
    'O': 10,
    'A+': 9,
    'A': 8,
    'B+': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'F': 0
}

@app.route('/', methods=['GET', 'POST'])
def index():
    cgpa = None
    if request.method == 'POST':
        grades = request.form.getlist('grade')
        credits = request.form.getlist('credit')

        try:
            total_points = sum(grade_points[g] * float(c) for g, c in zip(grades, credits))
            total_credits = sum(float(c) for c in credits)
            cgpa = round(total_points / total_credits, 2) if total_credits else 0
        except (ValueError, KeyError):
            cgpa = "Invalid input!"

    return render_template('index.html', cgpa=cgpa, grade_list=grade_points.keys())

if __name__ == '__main__':
    app.run(debug=True)

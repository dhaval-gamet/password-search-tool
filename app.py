from flask import Flask, request, render_template
import itertools

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        chars = "AcDb0r28@"
        target_password = request.form.get('password')
        found = False
        for length in range(1, 10):
            for attempt in itertools.product(chars, repeat=length):
                password = ''.join(attempt)
                if password == target_password:
                    result = f"Password मिल गया: {password}"
                    found = True
                    break
            if found:
                break
        if not found:
            result = "Password नहीं मिला।"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()

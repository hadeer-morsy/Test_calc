from flask import Flask, render_template, request, url_for
import json
app = Flask(__name__)

class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Division by zero error"
        else:
            return a / b

def get_visit_count():
    """Reads the visit count from visits.json."""
    try:
      with open('visits.json', 'r') as f:
          data = json.load(f)
          return data['visit_count']
    except (FileNotFoundError, json.JSONDecodeError):
	    # Handle cases where the file doesn't exist or is corrupt
      return 0
	
def update_visit_count(count):
  """Writes the updated visit count to visits.json."""
  with open('visits.json', 'w') as f:
    json.dump({'visit_count': count}, f)
	
@app.route("/", methods=["GET"])
def main():
  visit_count = get_visit_count()
  visit_count += 1
  update_visit_count(visit_count)
  return render_template("index.html", visit_count=visit_count)
	
@app.route("/visits", methods=["GET"])
def get_visits():
  visit_count = get_visit_count()
  data = {'visit_count': visit_count}  # Create a dictionary with visit count
  return json.dumps(data)  # Return JSON data

@app.route("/calculate", methods=["POST"])
def calculate():
  calculator = Calculator()
  first_number = int(request.form["firstNumber"])
  operation = request.form["operation"]
  second_number = int(request.form["secondNumber"])
  result = None
  note = ""

  if operation == "add":
    result = calculator.add(first_number, second_number)
    note = "Successful"
  elif operation == "sub":
    result = calculator.sub(first_number, second_number)
    note = "Successful"
  elif operation == "mult":
    result = calculator.mult(first_number, second_number)
    note = "Successful"
  elif operation == "div":
    result = calculator.div(first_number, second_number)
    note = "result"  # Set note to the result (error message or calculated value)
  else:
    result = None
    note = "Invalid operation"

  return render_template("index.html", result=result, note=note)

if __name__ == "__main__":
  app.run('0.0.0.0', 5000, 50001)





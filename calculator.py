from flask import Flask, render_template, request, url_for

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

@app.route("/", methods=["GET"])
def main():
  return render_template("index.html")

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
    note = result  # Set note to the result (error message or calculated value)
  else:
    result = None
    note = "Invalid operation"

  return render_template("index.html", result=result, note=note)

if __name__ == "__main__":
  app.run(debug=True)





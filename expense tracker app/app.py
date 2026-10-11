
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    welcome = ""
    expenses = []
    descriptions = []
    total = 0
    average = 0
    smallest = 0
    largest = 0
    error = ""
    name = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        welcome = f"Welcome, {name}! Let's track your expenses."
        
        amounts = request.form.getlist("amount")
        descriptions = request.form.getlist("description")

        # Get the number of expenses requested
        try:
            numexpenses = int(request.form.get("numexpenses", "0"))
        except ValueError:
            numexpenses = 0

        amounts = request.form.getlist("amount")

        # Validate the number of expenses
        if not 1 <= numexpenses <= 100:
            error = "Please enter a number between 1 and 100."

        elif len(amounts) != numexpenses or len(descriptions) != numexpenses:
            error = "Please create the correct number of expense fields."

        else:
            try:
                expenses = [int(amount) for amount in amounts]

                if any(amount <= 0 for amount in expenses):
                    raise ValueError

            except ValueError:
                expenses = []
                error = "Please enter a whole number greater than zero for every expense."

        # Calculate only when all expenses are valid
        if not error:
            total = sum(expenses)
            average = round(total / len(expenses), 2)
            smallest = min(expenses)
            largest = max(expenses)

    return render_template(
        "index.html",
        welcome=welcome,
        name=name,
        expenses=expenses,
        descriptions=descriptions,
        total=total,
        average=average,
        smallest=smallest,
        largest=largest,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)


const createButton = document.getElementById("create-fields");
const numberInput = document.getElementById("numexpenses");
const expenseFields = document.getElementById("expense-fields");
const calculateButton = document.getElementById("calculate-button");

createButton.addEventListener("click", function () {
    const count = Number(numberInput.value);

    // Check that the number of expenses is valid
    if (!Number.isInteger(count) || count < 1 || count > 100) {
        alert("Please enter a number between 1 and 100.");
        return;
    }

    // Clear any previously generated fields
    expenseFields.innerHTML = "";

    // Create the requested number of numbered fields
    for (let i = 1; i <= count; i++) {
        const label = document.createElement("label");
        label.textContent = `Expense ${i} (Rs)`;
        label.htmlFor = `expense-${i}`;

        const input = document.createElement("input");
        input.type = "number";
        input.id = `expense-${i}`;
        input.name = "amount";
        input.placeholder = `Enter amount for expense ${i}`;
        input.min = "1";
        input.step = "1";
        input.required = true;

        const descriptionLabel = document.createElement("label");
        descriptionLabel.textContent = `What was expense ${i} for?`;
        descriptionLabel.htmlFor = `description-${i}`;

        const descriptionInput = document.createElement("input");
        descriptionInput.type = "text";
        descriptionInput.id = `description-${i}`;
        descriptionInput.name = "description";
        descriptionInput.placeholder = "e.g. Food, transport, books";
        descriptionInput.required = true;

        expenseFields.appendChild(descriptionLabel);
        expenseFields.appendChild(descriptionInput);
        expenseFields.appendChild(label);
        expenseFields.appendChild(input);
    }

    calculateButton.hidden = false;
});

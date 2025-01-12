const form = document.getElementById('form');

form.addEventListener('submit', async function (event) {
    event.preventDefault(); 

    const expression = String(document.getElementById('expression').value);

    if (expression == "") {
        document.getElementById('result').textContent = "Please enter an arithmetic expression.";
        return;
    }

    try {
        const response = await fetch('/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: expression }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        document.getElementById('result').textContent = `Result: ${data.result}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').textContent = "An error occurred. Please try again.";
    }
});
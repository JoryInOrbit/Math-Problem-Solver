const form = document.getElementById('form');

form.addEventListener('submit', async function (event) {
    event.preventDefault(); 

    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    if (isNaN(num1) || isNaN(num2)) {
        document.getElementById('result').textContent = "Please enter valid numbers.";
        return;
    }

    try {
        const response = await fetch('/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input1: num1, input2: num2 }),
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
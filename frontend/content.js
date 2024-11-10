// content.js
console.log("Content script loaded");

document.addEventListener('mouseup', function () {
    const selection = window.getSelection().toString().trim();
    if (selection.length > 0) {
        console.log("Selected text:", selection); // Log selected text

        // Send the selected text to Flask backend (localhost:5000)
        fetch('http://localhost:5000/highlight', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ word: selection })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Response from server:", data.message); // Optional: log response from server
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
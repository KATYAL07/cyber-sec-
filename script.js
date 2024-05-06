function encrypt() {
    var message = document.getElementById("message").value;
    var shift = document.getElementById("shift").value;

    fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: message,
            key: shift
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Encrypted message: " + data.encrypted_message;
    });
}

function decrypt() {
    var message = document.getElementById("message").value;
    var shift = document.getElementById("shift").value;

    fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: message,
            key: shift
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Decrypted message: " + data.decrypted_message;
    });
}

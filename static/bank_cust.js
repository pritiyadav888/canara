function startTimer(duration, display, codeDisplay) {
    var timer = duration;
    var endInterval = setInterval(function () {
        var minutes = parseInt(timer / 60, 10);
        var seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = timer > 0 ? minutes + ":" + seconds : "0"; // Update to show "0" when the timer ends

        if (--timer < 0) {
            clearInterval(endInterval);
            if (codeDisplay) {
                codeDisplay.textContent = "Code has expired"; // Update to show expiration message
            }
        }
    }, 1000);
}

document.getElementById('model').addEventListener('click', function () {
    // Redirect to the new Flask route, which will then redirect to index.html
    window.location.href = '/model';
});

document.addEventListener('DOMContentLoaded', function () {
    var socket = io.connect(window.location.origin);

    var requestButton = document.getElementById('request-code');
    var bankCodeDisplay = document.getElementById('code-display');
    var customerCodeDisplay = document.getElementById('code');
    var bankCountdownDisplay = document.getElementById('countdown-bank');
    var customerCountdownDisplay = document.getElementById('countdown-customer');

    requestButton.addEventListener('click', function () {
        socket.emit('request code');
    });

    socket.on('code update', function (data) {
        console.log('Code update:', data);
        if (bankCodeDisplay && customerCodeDisplay) {
            bankCodeDisplay.textContent = data.code; // Display the new code for bank
            customerCodeDisplay.textContent = data.code; // Display the new code for customer
        }

        // Reset countdown display text and start a 30-second countdown for both bank and customer
        if (bankCountdownDisplay && customerCountdownDisplay) {
            bankCountdownDisplay.textContent = "00:30";
            customerCountdownDisplay.textContent = "00:30";
            startTimer(30, bankCountdownDisplay, bankCodeDisplay); // Bank countdown
            startTimer(30, customerCountdownDisplay, customerCodeDisplay); // Customer countdown
        }
    });

    socket.on('code expired', function (message) {
        console.log('Code expired:', message); // This should log the expiration message
        if (bankCodeDisplay && customerCodeDisplay) {
            bankCodeDisplay.textContent = message; // Updates the text content to show the expiration message for bank
            customerCodeDisplay.textContent = message; // Updates the text content to show the expiration message for customer
        }
    });

    // Listen for fraud alerts specific to the logged-in customer
    socket.on('fraud alert', function (alert) {
        const alertsDiv = document.getElementById('alerts');
        if (alertsDiv) {
            // Make the alerts div visible
            alertsDiv.style.display = 'block';
            // Set the text of the alert
            alertsDiv.textContent = alert.message;
            // Set a timeout to hide the alert after 20 seconds
            setTimeout(function () {
                alertsDiv.style.display = 'none';
            }, 20000); // 20000 milliseconds = 20 seconds
        } else {
            console.error('Alerts div not found.');
        }
    });

    var fraudTriggerButton = document.getElementById('fraud-trigger'); // Select the button by its ID
    fraudTriggerButton.addEventListener('click', function() {
        // Send a GET request to the /send-fraud-email endpoint
        fetch('/send-fraud-email')
            .then(response => {
                if (response.ok) {
                    return response.text(); // or `response.json()` if your server sends back JSON
                }
                throw new Error('Network response was not ok.');
            })
            .then(text => {
                console.log('Fraud email sent:', text); // Log the success response from the server
            })
            .catch(error => {
                console.error('There has been a problem with your fetch operation:', error);
            });
    });

});

function analyzeActivity() {
    let activity = document.getElementById('activityInput').value; // Get user input
    $.ajax({
        url: '/analyze', // Match this with the Flask route
        type: 'POST', // POST request
        contentType: 'application/json', // Data sent as JSON
        data: JSON.stringify({ activity: activity }), // Ensure JSON key matches backend
        success: function(response) {
            document.getElementById('result').innerText = response.message; // Show backend response
        },
        error: function(xhr, status, error) {
            console.error("AJAX Error: ", status, error); // Log the error for debugging
            document.getElementById('result').innerText = "Error processing request.";
        }
    });
}
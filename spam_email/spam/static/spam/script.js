function checkSpam() {
    let emailText = document.getElementById("emailInput").value.trim();
    if (!emailText) {
        alert("Please enter an email to classify.");
        return;
    }

    fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: emailText })
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById("result");
        resultDiv.textContent = data.result === "spam" ? "Spam" : "Not Spam";
        resultDiv.style.color = data.result === "spam" ? "red" : "green";
    })
    .catch(error => console.error("Error:", error));
}
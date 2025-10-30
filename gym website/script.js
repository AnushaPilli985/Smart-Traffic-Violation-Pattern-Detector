document.addEventListener("DOMContentLoaded", () => {
    const callBtn = document.getElementById('callBtn');
    const emailBtn = document.getElementById('emailBtn');

    if (callBtn) {
        callBtn.addEventListener('click', () => {
            alert("Calling Srinu's Fitness Center at +91-9876543210...");
        });
    }

    if (emailBtn) {
        emailBtn.addEventListener('click', () => {
            alert("Opening email client...");
            window.location.href = "mailto:harryfitness@example.com";
        });
    }

    const bmiBtn = document.getElementById('bmiBtn');
    if (bmiBtn) {
        bmiBtn.addEventListener('click', () => {
            const weight = parseFloat(document.getElementById('weight').value);
            const height = parseFloat(document.getElementById('height').value);
            const result = document.getElementById('bmiResult');

            if (!weight || !height || height <= 0) {
                result.innerText = "Please enter valid weight and height.";
                result.style.color = "red";
                return;
            }

            const bmi = weight / (height * height);
            let status = "";

            if (bmi < 18.5) status = "Underweight";
            else if (bmi < 24.9) status = "Normal weight";
            else if (bmi < 29.9) status = "Overweight";
            else status = "Obese";

            result.innerText = `Your BMI is ${bmi.toFixed(2)} (${status})`;
            result.style.color = "lightgreen";
        });
    }
});

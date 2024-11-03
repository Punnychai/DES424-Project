// Validate Sign-Up Form
document.getElementById('signupForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get input values
    const fullname = document.getElementById('fullname').value;
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Simple password matching validation
    if (password !== confirmPassword) {
        alert('Passwords do not match. Please try again.');
        return;
    }

    // Display success message (simulates successful sign-up)
    document.getElementById('signupSuccess').style.display = 'block';
    
    // Reset form fields
    document.getElementById('signupForm').reset();
});

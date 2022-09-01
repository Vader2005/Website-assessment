const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    checkInputs();
});

function checkInputs() {
    // Get the values from the inputs
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();

    // Check if there is a value inside


    if(emailValue === '') {
        setErrorFor(email, 'Email cannot be blank');
    } else if(!isEmail(emailValue)) {
        setErrorFor(email, 'Email is not valid');
    } else {
        setSuccessFor(email);
    }

    if(passwordValue === '') {
        setErrorFor(password, 'Password cannot be blank');
    } else {
        setSuccessFor(password);
    }

}

function setErrorFor(input, message) {
    const FormControl = input.parentElement;  // Form control
    const small = FormControl.querySelector('small');

    // Add the error message inside the small
    small.innerText = message;

    // Add the error class
    FormControl.className = 'form-control error';
}

function setSuccessFor(input, message) {
    const FormControl = input.parentElement;
    FormControl.className = 'form-control success';
}

function isEmail(email) {
    return /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

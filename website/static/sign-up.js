const form = document.getElementById('form');
const firstName = document.getElementById('firstName');
const email = document.getElementById('email');
const password1 = document.getElementById('password1');
const password2 = document.getElementById('password2');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    checkInputs();
    doFunction();
});

function checkInputs() {
    // Get the values from the inputs
    const firstNameValue = firstName.value.trim();
    const emailValue = email.value.trim();
    const password1Value = password1.value.trim();
    const password2Value = password2.value.trim();

    // Check if there is a value inside
    
    if(firstNameValue === '') {
        // Show error, since the string is empty, and add error class
        setErrorFor(firstName, 'Name cannot be blank');
    } else {
        // Add the success class
        setSuccessFor(firstName);
    }

    if(emailValue === '') {
        setErrorFor(email, 'Email cannot be blank');
    } else if(!isEmail(emailValue)) {
        setErrorFor(email, 'Email is not valid');
    } else {
        setSuccessFor(email);
    }

    if(password1Value === '') {
        setErrorFor(password1, 'Password cannot be blank');
    } else {
        setSuccessFor(password1);
    }

    if(password2Value === '') {
        setErrorFor(password2, 'Confirm Password cannot be blank');
    } else if(password1Value !== password2Value) {
        setErrorFor(password2, 'Passwords do not match');
    } else {
        setSuccessFor(password2);
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

function doFunction() {
    $.ajax ({
        type: 'POST',
        url: '/sign-up',
        data: {
            email: email.value.trim(),
        }
    });
}

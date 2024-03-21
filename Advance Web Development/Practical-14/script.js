const form = document.querySelector('form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const enrollmentInput = document.querySelector('#enrollment');
const passwordInput = document.querySelector('#password');


const nameRegex = /^[a-zA-Z\s]+$/;
const emailRegex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
const enrollmentRegex = /^\d{15}$/;
const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;

form.addEventListener('submit', (event) => {
  event.preventDefault(); 
  let isValid = true;

  if (!nameRegex.test(nameInput.value.trim())) {
    nameInput.classList.add('is-invalid');
    isValid = false;
  } else {
    nameInput.classList.remove('is-invalid');
    nameInput.classList.add('is-valid');
  }

  if (!emailRegex.test(emailInput.value.trim())) {
    emailInput.classList.add('is-invalid');
    isValid = false;
  } else {
    emailInput.classList.remove('is-invalid');
    emailInput.classList.add('is-valid');
  }

  if (!enrollmentRegex.test(enrollmentInput.value.trim())) {
    enrollmentInput.classList.add('is-invalid');
    isValid = false;
  } else {
    enrollmentInput.classList.remove('is-invalid');
    enrollmentInput.classList.add('is-valid');
  }

  if (!passwordRegex.test(passwordInput.value)) {
    passwordInput.classList.add('is-invalid');
    isValid = false;
  } else {
    passwordInput.classList.remove('is-invalid');
    passwordInput.classList.add('is-valid');
  }

  if (isValid) {
    form.submit();
  }
});


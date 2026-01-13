const wrapper = document.querySelector('.wrapper');
const registerLink = document.querySelector('.register-link');
const loginLink = document.querySelector('.login-link');
const error = document.querySelector(".error-message");


function clearError() {
    if (error) {
        error.classList.add("fade-out");
        setTimeout(() => error.remove(), 400);
    }
}

registerLink.onclick = () => {
    wrapper.classList.add('active');
    clearError();
}

loginLink.onclick = () => {
    wrapper.classList.remove('active');
    clearError();
}


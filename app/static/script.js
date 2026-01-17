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

function openLogModal(title, location, date, type, zone = null, imageUrl) {
    console.log("MODAL CLICKED", title, imageUrl);
    document.getElementById("modalTitle").innerText = title;
    document.getElementById("modalLocation").innerText = "Location: " + location;
    document.getElementById("modalDate").innerText = "Date: " + date;
    document.getElementById("modalType").innerText = "Type: " + type;
    document.body.style.overflow = "hidden";

    const img = document.getElementById("modalImage");
    if (imageUrl) {
        img.src = imageUrl;
        img.style.display = "block";
    } else {
        img.style.display = "none";
    }

    document.getElementById("logModal").style.display = "block";
}

function closeLogModal() {
    document.getElementById("logModal").style.display = "none";
    document.body.style.overflow = "";
}

window.addEventListener("click", function (event) {
    const modal = document.getElementById("logModal");
    if (event.target === modal) {
        closeLogModal();
    }
});

document.addEventListener("keydown", e => {
    if (e.key === "Escape") closeLogModal();
});


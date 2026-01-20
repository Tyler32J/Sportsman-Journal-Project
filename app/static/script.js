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

if (registerLink && wrapper) {
    registerLink.onclick = () => {
        wrapper.classList.add('active');
        clearError();
    };
}

if (loginLink && wrapper) {
    loginLink.onclick = () => {
        wrapper.classList.remove('active');
        clearError();
    };
}

function openLogModal(title, location, date, type, quantity, zone, imageUrl) {
    console.log("MODAL CLICKED", title, imageUrl);
    document.getElementById("modalTitle").innerText = title;
    document.getElementById("modalLocation").innerText = "Location: " + location;
    document.getElementById("modalDate").innerText = "Date: " + date;
    document.getElementById("modalType").innerText = "Type: " + type;
    document.getElementById("modalQuantity").innerText = "Quantity: " + quantity;
   
     const zoneElement = document.getElementById("modalZone");
     if (zone) {
        document.getElementById("modalZone").innerText = "Zone: " + zone;
    }
    
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

function openPostModal(username, location, date, quantity, type, zone, imageUrl) {
    console.log("POST MODAL CLICKED", username, imageUrl);
    document.getElementById("postModalUser").innerText = username;
    document.getElementById("postModalLocation").innerText = "Location: " + location;
    document.getElementById("postModalDate").innerText = "Date: " + date;
     document.getElementById("postModalQuantity").innerText = "Quantity: " + quantity;
    document.getElementById("postModalType").innerText = "Type: " + type;
   
    const zoneElement = document.getElementById("postModalZone");
    if (zone && zone.trim() !== '') {
        zoneElement.innerText = "Zone: " + zone;
        zoneElement.style.display = "block";
    } else {
        zoneElement.style.display = "none";
    }
    
    document.body.style.overflow = "hidden";

    const img = document.getElementById("postModalImage");
    if (imageUrl) {
        img.src = imageUrl;
        img.style.display = "block";
    } else {
        img.style.display = "none";
    }

    document.getElementById("postModal").style.display = "block";
}

function closePostModal() {
    document.getElementById("postModal").style.display = "none";
    document.body.style.overflow = "";
}

window.addEventListener("click", function (event) {
    const postModal = document.getElementById("postModal");
    if (event.target === postModal) {
        closePostModal();
    }
});

document.addEventListener("keydown", e => {
    if (e.key === "Escape") closePostModal();
});

document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("id_picture");
    const preview = document.getElementById("previewImage");
    const imagePreview = document.querySelector(".image-preview");

    if (!input || !preview) return;

    input.addEventListener("change", function () {
        const file = this.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = "block";
            imagePreview.classList.add("has-image");
        };
        reader.readAsDataURL(file);
    });
});

document.addEventListener("DOMContentLoaded", function () {
     const logType = document.getElementById("logTypeSelect");
     const huntingGroup = document.getElementById("huntingGroup");
     const fishingGroup = document.getElementById("fishingGroup");
 
     if (!logType || !huntingGroup || !fishingGroup) return;
 
     function toggleGroups() {
         if (logType.value === "hunting") {
             huntingGroup.classList.remove("hidden");
             fishingGroup.classList.add("hidden");
         } else if (logType.value === "fishing") {
             fishingGroup.classList.remove("hidden");
             huntingGroup.classList.add("hidden");
         } else {
             huntingGroup.classList.add("hidden");
             fishingGroup.classList.add("hidden");
         }
     }
 
     toggleGroups();
 
     logType.addEventListener("change", toggleGroups);
 });
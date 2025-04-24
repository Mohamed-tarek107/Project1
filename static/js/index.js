document.addEventListener("DOMContentLoaded", function () {
    const displayElement = document.getElementById("username");
    const username = displayElement.getAttribute("data-username");

    let i = 0;
    const speed = 100;

    function writer() {
        if (i < username.length) {
            displayElement.innerHTML += username.charAt(i);
            i++;
            setTimeout(writer, speed);
        }
    }

    writer();
});


document.addEventListener('DOMContentLoaded', function() {
    
    const elements = {
        openBtn: document.getElementById("openBtn"),
        closeBtn: document.getElementById("closeBtn"),
        overlay: document.getElementById("overlay"),
        popup: document.getElementById("popup")
    };
        for (const [name, element] of Object.entries(elements)) {
        if (!element) {
            console.error(`Element ${name} not found!`);
            return;
        }
    }

    function openPopup() {
        console.log('Opening popup');
        elements.popup.style.display = 'block';
        elements.overlay.style.display = 'block';
    }

    function closePopup() {
        console.log('Closing popup');
        elements.popup.style.display = 'none';
        elements.overlay.style.display = 'none';
    }

    // Add event listeners
    elements.openBtn.addEventListener('click', openPopup);
    elements.closeBtn.addEventListener('click', closePopup);
    elements.overlay.addEventListener('click', closePopup);

    // Add keyboard support (ESC to close)
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && elements.popup.style.display === 'block') {
            closePopup();
        }
    });
});



document.addEventListener('DOMContentLoaded', function () {
    // Settings Popup
    const settings = {
        openBtn: document.getElementById("openBtnSettings"),
        closeBtn: document.getElementById("closeBtnSettings"),
        overlay: document.getElementById("overlaySettings"),
        popup: document.getElementById("popupSettings")
    };

    if (settings.openBtn && settings.closeBtn && settings.overlay && settings.popup) {
        settings.openBtn.addEventListener('click', function (e) {
            e.preventDefault();
            settings.popup.style.display = 'block';
            settings.overlay.style.display = 'block';
        });

        settings.closeBtn.addEventListener('click', function () {
            settings.popup.style.display = 'none';
            settings.overlay.style.display = 'none';
        });

        settings.overlay.addEventListener('click', function () {
            settings.popup.style.display = 'none';
            settings.overlay.style.display = 'none';
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && settings.popup.style.display === 'block') {
                settings.popup.style.display = 'none';
                settings.overlay.style.display = 'none';
            }
        });
    
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const flashContainer = document.getElementById('flash-messages');
    
    if (flashContainer) {
        setTimeout(function() {
            const alerts = flashContainer.querySelectorAll('.alert');
            alerts.forEach(function(alert) {
                alert.classList.add('fade-out');
                setTimeout(function() {
                    const bsAlert = new bootstrap.Alert(alert);
                    bsAlert.close();
                }, 500);
            });
        }, 1700);
    }
});
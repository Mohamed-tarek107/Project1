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
    // Debugging: Log all found elements
    console.log('DOM fully loaded, running inventory.js');
    
    const elements = {
        openBtn: document.getElementById("openBtn"),
        closeBtn: document.getElementById("closeBtn"),
        overlay: document.getElementById("overlay"),
        popup: document.getElementById("popup")
    };

    // Verify all elements exist
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

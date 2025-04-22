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

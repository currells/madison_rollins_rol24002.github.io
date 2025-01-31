document.addEventListener('DOMContentLoaded', function() {
    const menuButton = document.getElementById("menuButton");
    const nav = document.querySelector("nav");

    if (menuButton && nav) {
        menuButton.addEventListener("click", function() {
            nav.classList.toggle("hide");
        });
    } else {
        console.error("Menu button or nav element not found!");
    }

    function handleResize() {
        if (window.innerWidth > 1000) {
            nav.classList.remove("hide");  // Remove 'hide' class
        } else {
            nav.classList.add("hide");     // Add 'hide' class
        }
    }

    // Call handleResize initially on page load
    handleResize();

    // Add event listener for resize
    window.addEventListener("resize", handleResize);

    function viewerTemplate(imagePath, altText) {
        return `
            <div class="viewer">
                <button class="close-viewer">X</button>
                <img src="${imagePath}" alt="${altText}">
            </div>
        `;
    }

    function viewHandler(event) {
        const clickedImage = event.target;
        const imageSrcParts = clickedImage.src.split("-");
        const fullImagePath = imageSrcParts[0] + "-full.jpeg"; // Construct full path
        const altText = clickedImage.alt;

        document.body.insertAdjacentHTML("afterbegin", viewerTemplate(fullImagePath, altText));

        const closeButton = document.querySelector(".close-viewer");
        closeButton.addEventListener("click", closeViewer);
    }

    function closeViewer() {
        const viewer = document.querySelector(".viewer");
        viewer.remove();
    }

    const gallery = document.querySelector(".gallery");
    gallery.addEventListener("click", viewHandler);
});

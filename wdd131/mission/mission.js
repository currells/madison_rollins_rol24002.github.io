const themeSelector = document.querySelector('#theme-select');
const body = document.body; // Get body outside the function
const logo = document.getElementById('byui-logo'); // Get the logo outside the function

function changeTheme() {
    const selectedTheme = themeSelector.value;

    console.log("Selected theme:", selectedTheme);

    if (selectedTheme === 'dark') {
        console.log("Applying dark theme");
        body.classList.add('dark');
        logo.src = "byui-logo_white.webp";
    } else {
        console.log("Applying light theme");
        body.classList.remove('dark');
        logo.src = "byui-logo_blue.webp";
    }
    localStorage.setItem('theme', selectedTheme);
}

themeSelector.addEventListener('change', () => {
    console.log("Theme selector changed!"); // Check if this logs
    changeTheme();
});

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        themeSelector.value = savedTheme;
        changeTheme(); // Apply the saved theme
    }
});
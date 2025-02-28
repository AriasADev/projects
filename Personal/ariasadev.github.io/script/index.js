function isDarkMode() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
}

function loadThemeStylesheet() {
    let themeLink = document.getElementById('theme-stylesheet');

    // If the theme stylesheet link element does not exist, create and append it to the head
    if (!themeLink) {
        themeLink = document.createElement('link');
        themeLink.rel = 'stylesheet';
        themeLink.id = 'theme-stylesheet';
        document.head.appendChild(themeLink);
    }

    // Set the stylesheet URL, adding a cache-busting timestamp
    const themeFile = isDarkMode() ? 'css/darkmode.css' : 'css/lightmode.css';
    themeLink.href = `${themeFile}?v=${new Date().getTime()}`;
}

// Initial theme loading
loadThemeStylesheet();

// Listen for color scheme changes and apply the appropriate theme
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', loadThemeStylesheet);


// VANTA fog effect settings with color adjustments based on the current color scheme
const baseColor = isDarkMode() ? 0x000000 : 0xffffff; // Dark mode: black, Light mode: white
const highlightColor = isDarkMode() ? 0xc200b7 : 0xfd00ff; // Dark mode: darker purple
const midtoneColor = isDarkMode() ? 0x7a00cc : 0x9300ff; // Dark mode: darker midtone

VANTA.FOG({
    el: "#background",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    highlightColor: highlightColor,
    midtoneColor: midtoneColor,
    baseColor: baseColor
});

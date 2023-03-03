console.log('JavaScript is working!!');


/* Mission 1 - Create Event Handles that would change the theme of the website */

// Theme from LocalStorage (memory of the browser)
let theme = localStorage.getItem('theme');
// Check if it is the first of the user in my website
if (theme == null)
    setTheme('light');
else
    setTheme(theme);

// Themes Dots
let theme_dots = document.getElementsByClassName("theme-dot");

// Iterate all Theme Dots and add the Event Handler to each Dot that was clicked
for (var i = 0; i < theme_dots.length; i++) {
    theme_dots[i].addEventListener("click", function() {
        let mode = this.dataset.mode;
        console.log("Theme option clicked!", mode);
        setTheme(mode); // Set the Theme
    })
}

function setTheme(mode) {
    if (mode == "light") {
        // Set the link element to link to default.css
        document.getElementById('theme-style').href = static + "/default.css";
    }
    if (mode == "blue") {
        // Set the link element to link to blue.css
        document.getElementById('theme-style').href = static + "/blue.css";
    }
    if (mode == "green") {
        // Set the link element to link to green.css
        document.getElementById("theme-style").href = static + "/green.css";
    }
    if (mode == "purple") {
        // Set the link element to link to purple.css
        document.getElementById("theme-style").href = static + "/purple.css";
    }

    // Save value in LocalStorage (memory of the browser)
    localStorage.setItem('theme', mode);
}
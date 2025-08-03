document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("theme-toggle-btn"); // or use querySelector(".theme-toggle-btn")
    if (!toggleBtn) {
        console.log("Toggle button NOT found!");
        return;
    }
    toggleBtn.addEventListener("click", () => {
        document.body.classList.toggle("dark");
        console.log("Toggled dark mode");
    });
});

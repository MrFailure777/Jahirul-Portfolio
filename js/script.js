// Optional: JavaScript to handle dropdown behavior for mobile
// (you can enhance this later with toggle menus if needed)

// Future enhancement idea: 
// Convert hover dropdowns to click dropdowns for mobile

console.log("Portfolio script loaded.");



const form = document.getElementById("contactForm");

form.addEventListener("submit", (e) => {
  e.preventDefault(); // stop default submit
  form.submit(); // allow formsubmit.co to work
  // optional: add loading spinner or success message
});


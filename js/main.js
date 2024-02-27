const menuToggle = document.querySelector('.menu-toggle');
const slider = document.querySelector('.slider');

menuToggle.addEventListener('click', function() {
    const dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.classList.toggle('show');

    // Sembunyikan slider saat menu toggle diklik
    if (slider.style.display === 'none') {
        slider.style.display = 'block';
    } else {
        slider.style.display = 'none';
    }
});

function updateProgressBar(elementId, percentage) {
    const circle = document.getElementById(elementId).querySelector('.progress-bar');
    const label = document.getElementById(elementId).querySelector('.progress-label');
    const radius = circle.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (percentage / 100) * circumference;
    circle.style.strokeDasharray = `${circumference}`;
    circle.style.strokeDashoffset = offset;
    label.textContent = `${percentage}%`;
}

// Call the function for each progress bar
updateProgressBar('progress-bar-1', 90); // Laravel - 90%
updateProgressBar('progress-bar-2', 80); // Laravel - 90%




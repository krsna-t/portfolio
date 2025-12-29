// document.addEventListener("DOMContentLoaded", function() {
//         const track = document.getElementById('track');
//         if (track) {
//             track.innerHTML += track.innerHTML;
//         }
//     });

document.addEventListener("DOMContentLoaded", function() {
    // Project Track Cloning
    const projectTrack = document.getElementById('track');
    if (projectTrack) {
        projectTrack.innerHTML += projectTrack.innerHTML;
    }
});
document.addEventListener("DOMContentLoaded", function() {
    const skillsTrack = document.getElementById("skillsTrack");
    if (skillsTrack) {
        skillsTrack.innerHTML;
        skillsTrack.innerHTML += skillsTrack.innerHTML;
 
    }
});


document.addEventListener("DOMContentLoaded", () => {
    const reveals = document.querySelectorAll(".reveal");

    const observer = new IntersectionObserver(
        entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("show");
                    observer.unobserve(entry.target); // important
                }
            });
        },
        {
            threshold: 0.2,
            rootMargin: "0px 0px -80px 0px" // 🔥 THIS IS THE KEY
        }
    );

    // Delay observing until after first render
    setTimeout(() => {
        reveals.forEach(el => observer.observe(el));
    }, 100);
});


document.addEventListener("DOMContentLoaded", () => {
    const section = document.getElementById("experience-root");
    const cards = document.querySelectorAll(".experience-card");

    if (!section) return;

    const observer = new IntersectionObserver(
        entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    cards.forEach(card => card.classList.add("show"));
                }
            });
        },
        { threshold: 0.9 }
    );

    observer.observe(section);
});

document.addEventListener("DOMContentLoaded", function() {
    const track = document.getElementById('track');
    if (track) {
        // This doubles the content inside the track
        track.innerHTML += track.innerHTML;
    }
});
document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('.navbar-ikos');

    window.onscroll = function() {
        if (window.scrollY > 50) {
            nav.classList.add('navbar-scrolled');
        } else {
            nav.classList.remove('navbar-scrolled');
        }
    };
    
    console.log("Le script de la navbar est chargé !");
});
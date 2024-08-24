document.addEventListener('DOMContentLoaded', () => {
    // Smooth Scrolling for Navigation Links
    const smoothScroll = (event) => {
        event.preventDefault();
        const targetId = event.currentTarget.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        window.scrollTo({
            top: targetElement.offsetTop,
            behavior: 'smooth'
        });
    };

    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => link.addEventListener('click', smoothScroll));

    // Toggle Mobile Menu (optional)
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const nav = document.querySelector('nav');

    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', () => {
            nav.classList.toggle('open');
        });
    }
});

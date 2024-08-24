document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.getElementById('navbar');
    const scrollThreshold = 50; // Adjust based on your preference
    const orderForm = document.getElementById('order-form');
    const orderConfirmation = document.getElementById('order-confirmation');

    window.addEventListener('scroll', () => {
        if (window.scrollY > scrollThreshold) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    orderForm.addEventListener('submit', (event) => {
        event.preventDefault();
        orderConfirmation.classList.remove('hidden');
        orderForm.reset();
    });
});

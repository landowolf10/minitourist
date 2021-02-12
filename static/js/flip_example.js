function flip() {
    var cards = document.querySelectorAll('.card');

    for (const card of cards) {
        card.addEventListener('click', function() {
            card.classList.toggle('is-flipped');
        });
    }
}
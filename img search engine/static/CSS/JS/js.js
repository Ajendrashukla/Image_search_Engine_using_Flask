
const linkElement = document.querySelector('.bulge-link');

linkElement.addEventListener('click', function(event) {
    if (isMobileDevice()) {
        event.preventDefault(); 
        window.open(this.href, '_blank'); 
    }
});

function isMobileDevice() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

document.addEventListener("DOMContentLoaded", function() {
    var images = document.querySelectorAll('.product-image');
    images.forEach(function(img) {
        img.onload = function() {
            var tempImg = new Image();
            tempImg.src = img.src;
            tempImg.onload = function() {
                var originalWidth = tempImg.width;
                var originalHeight = tempImg.height;

                if (originalWidth !== originalHeight) {
                    img.style.width = 'auto';
                    img.style.height = '150px';
                } else {
                    img.style.width = '150px';
                    img.style.height = '150px';
                }
            };
        };
    });
});

function showImageModal(imageSrc) {
    var modal = document.getElementById('image-modal');
    var modalImg = document.getElementById('modal-image');
    modal.style.display = 'block';
    modalImg.src = imageSrc;
}

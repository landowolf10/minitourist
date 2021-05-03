const selectFrontImage = document.querySelector('.front-image');
const selectBackImage = document.querySelector('.back-image');

selectFrontImage.addEventListener('change', changeFrontImage);
selectBackImage.addEventListener('change', changeBackImage);

function changeFrontImage(evt)
{
    let frontImage = evt.target.value.split('\\').pop();
    newBackImageInput = document.querySelector('.new-card').value = frontImage;
}

function changeBackImage(evt)
{
    let backImage = evt.target.value.split('\\').pop();
    newBackImageInput = document.querySelector('.new-card-back').value = backImage;
}
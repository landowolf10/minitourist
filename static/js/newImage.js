function changeImage()
{
    document.getElementById('img').addEventListener('change', function()
    { 
        var name = document.getElementById('img').files[0].name; 
        console.log(name);

        document.getElementById('new-card').value = name;
    });
}
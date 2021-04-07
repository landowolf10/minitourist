function validateSelectors()
{
    let selectedOption = document.getElementById('location').value;
    console.log(selectedOption);
    let cityTextbox =  document.getElementById('city');
    cityTextbox.value = selectedOption;
}

function emptyTextBoxes() 
{
    let name = document.getElementById('name').value;
    console.log('Name: ', name);

    if(name === '')
    {
        alert('Favor de llenar todos los campos');
        window.location.href = 'http://localhost:5000/clients';
    }
}
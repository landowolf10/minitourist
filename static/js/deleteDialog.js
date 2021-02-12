const btnDelete = document.querySelectorAll('.btn-delete');

if(btnDelete)
{
    console.log('Si existen');
    const btnArray = Array.from(btnDelete);

    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('¿Seguro de eliminar este cliente?'))
                e.preventDefault();
        });
    });
}
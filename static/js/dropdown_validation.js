function validateSelectors()
{
    let locationSelector = document.getElementById("location").value;
    //let locationSelectedIndex = locationSelector.options[locationSelector.selectedIndex].value;

    console.log("locationSelector: ", locationSelector);

    if (locationSelector == "Seleccione una ciudad")
    {
      alert("Seleccione una ciudad");
      window.location.href = "http://localhost:5000/clients";
    }
}
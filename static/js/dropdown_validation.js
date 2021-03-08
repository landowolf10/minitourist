function validateSelectors()
{
    let locationSelector = document.getElementById("location");
    let locationSelectedIndex = locationSelector.options[locationSelector.selectedIndex].value;

    console.log("locationSelector: ", locationSelector);

    if (locationSelectedIndex == "Seleccione una ciudad")
      alert("Seleccione una ciudad");
}
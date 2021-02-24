function showDinnerCost() {
    var dinnerCostItems = document.getElementById('amount-container');
    dinnerCostItems.style.display = "block";
}

function hideDinnerCost() {
    var dinnerCostItems = document.getElementById('amount-container');
    dinnerCostItems.style.display = "none";
}

function addPlaceholder(){
    var address = document.getElementById('id_address');
    var postnr = document.getElementById('id_postnr');
    var poststed = document.getElementById('id_poststed');
    address.placeholder = "Eksempelveien 1";
}

addPlaceholder()
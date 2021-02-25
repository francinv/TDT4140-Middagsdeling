var menu = document.getElementById('id_sharing');
var dinnerCost = document.getElementById('amount-container')

function showDinnerCost(dinnerSelect){

    console.log(dinnerSelect);
    if(dinnerSelect){
        if(menu.value == "ja"){
            dinnerCost.style.display = "flex";
        }
        else{
            dinnerCost.style.display = "none";
        }
    }
    else{
        dinnerCost.style.display = "none";
    }
}
menu.addEventListener("change" ,showDinnerCost);


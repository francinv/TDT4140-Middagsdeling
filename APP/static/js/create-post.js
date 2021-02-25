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

function calculateCost(){
    num1 = document.getElementById("middag_guests").value;
    num2 = document.getElementById("middag_sharing_cost").value;
    document.getElementById('sharing_cost_number').innerHTML = num2 / num1;
}
calculateCost();
menu.addEventListener("change" ,showDinnerCost);



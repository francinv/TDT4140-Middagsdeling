function calculate(){
    let num1 = document.getElementById('middag_sharing_cost');
    let num2 = document.getElementById('middag_guests');
    const num3 = num1 / num2;
    console.log("HEI");
    console.log(num3);
    document.getElementById("sharing_cost_number").innerHTML = num3;
}



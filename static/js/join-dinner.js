var joinBtn = document.getElementById('join-button');

joinBtn.addEventListener("click", joinedDinner);

function joinedDinner(){
    console.log("funker");
    
    joinBtn.style.backgroundColor = "rgb(234, 246, 225)";
    joinBtn.innerHTML = "Du er meldt på!"
    joinBtn.style.color = "purple";
    joinBtn.style.border = "none";
}
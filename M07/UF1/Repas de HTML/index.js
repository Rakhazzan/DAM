function funcioBurguer() {
    var menu = document.getElementById("menu");
    var burger = document.getElementById("burger");
    burger.style.display = "none";
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}


function funcioOption() {
    if(screen.width<768){
        burger.style.display = "block";
        menu.style.display = "none";
    }
}
function canviaContingut() {
    var textIntroduit = document.getElementById("text1").value;
    var elementAltres = document.getElementById("Altres");
    elementAltres.textContent = textIntroduit;
}

function canviaAtribut() {
    document.getElementById('Hawaii').src='img.jpg'
}

function canviaCSS() {
    document.body.style.backgroundColor = "black";
    document.body.style.color = "white";
}
let logo = document.querySelector(".logo")
let navar = document.querySelector(".navbar")
window.addEventListener("scroll",()=>{
    if  (window.scrollY == 0){

        console.log(window.scrollY)
        logo.classList.remove("logo-lg");
        logo.classList.add("logo-sn");
        navar.classList.add("nav-sn");
        navar.classList.remove("nav-lg")
        
    }
    else {
        logo.classList.remove("logo-sn");
        logo.classList.add("logo-lg");
        navar.classList.add("nav-lg");
        navar.classList.remove("nav-sn")
    }
})

// slider image ici

let section1 = document.querySelector(".section1")

const liste_image = [
    "/static/image/img1.jpeg",
    "/static/image/img3.jpg",
    "/static/image/img4.jpg",
    "/static/image/img6.jpg"
];
let index = 0 
setInterval(()=>{
    index = (index + 1) % liste_image.length;
    section1.style.backgroundImage =`url(${liste_image[index]})`;  
 },6000)


// partie du popup 
const button_popup = document.querySelector(".overlay-popup");
let active_popup = ()=>{
    button_popup.classList.toggle("active-popup")
}

// le popup reste active s'il ya un message erreur et aussi gerer le temp d'affichage
const erreur = document.querySelector(".erreur") ;
if(erreur){
    button_popup.classList.add("active-popup")
    setTimeout(()=>{
        erreur.style.opacity= "0"
    },4000)
  }

const btn_success = document.querySelector(".success")
if(btn_success){
    setTimeout(()=>{
        btn_success.style.opacity= "0"
    },4000)
}


// gestion du numero de telephone s'il est valide ou pas 
function valide_numero(number) {
    // Supprime les espaces et vérifie le format
    const regex = /^[789]\d{7}$/;
    return regex.test(number);
}

const input_tel = document.getElementById("phone")
const erreur_tel = document.querySelector(".erreur_tel")
const btn_submit = document.querySelector(".submit-btn")

btn_submit.disabled = true;

input_tel.addEventListener("input",()=>{
const tel = input_tel.value.trim();
if (input_tel.value === ""){ erreur_tel.style.opacity = "0"; btn_submit.disabled = true;}
else if (!valide_numero(tel)){ erreur_tel.style.opacity = "1";  btn_submit.disabled = true; }
else {  erreur_tel.style.opacity = "0";; btn_submit.disabled = false;}

})
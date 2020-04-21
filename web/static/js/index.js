let menu = document.querySelector("#menu");

menu.addEventListener("click", function(){
    let showMenu = document.querySelector(".navbar").style.display;
    if(showMenu == 'none')
        document.querySelector(".navbar").style.display = 'block';
    else
        document.querySelector(".navbar").style.display = 'none';
});
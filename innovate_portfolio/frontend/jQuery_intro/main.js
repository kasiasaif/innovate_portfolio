$(document).ready(function(){

    $("#change-colour").click(function(){
        $("h1").toggleClass("red-title");

    })

    $("#hide-text").click(function(){
        $("p").toggle();
    })
    $("#dark-mode").click(function(){
        $("body").toggleClass("dark-mode");
    })



})

function displayDate(id){
    document.getElementById("date").innerHTML = Date()
}

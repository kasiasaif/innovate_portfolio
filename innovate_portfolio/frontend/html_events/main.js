console.log("JS is working");

function displayDate(id){
    document.getElementById("date").innerHTML = Date()
}

function chechCookies(){
     let text = "";
     if (navigator.cookieEnabled === true){
        text = "cookies are enabled";
     }else{
        text = "cookies are not enabled";
     } document.getElementById("cookie").innerHTML = text;
}


function mOver(){
    document.getElementById("title").style.color = 'blue'
}
function mOut(){
    document.getElementById("title").style.color = 'black'
}

function sendAlert(){
    alert(`This is confidential image${location.hostname}`)
}
function mode(){
    let page = document.body;
    page.classList.toggle("dark-mode")
}

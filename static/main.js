
localStorage.setItem("session-state","false")
var content = document.getElementById("content-user")

function session_state(){
    var state = localStorage.getItem("session-state")
    if (state == "false"){
        modal.style.display = "block";
        content.innerHTML = "<a href='/login'>Log in</a>"
    } else {
        modal.style.display = "none";
        content.innerHTML = "<ul><li>Programming</li><li>Football</li><li>Bussines</li><li>Life</li><span>All Post</span></ul>";
    }
}

document.addEventListener("load",modal_state);
content.addEventListener("click",function(){
    localStorage.setItem("ssesion-state","true")
})
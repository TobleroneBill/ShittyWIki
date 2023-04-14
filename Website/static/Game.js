// Make sure its loaded
console.log('Game Load')


// Image drag stuff
var draggable = document.getElementById("dragpic")
draggable.style.cursor = "grab"

draggable.addEventListener("dragstart",function(e){
    console.log("mstart")
    e.dataTransfer.setData("text", e.target.id);
});


function allowDrop(e){
    e.preventDefault()
}

function drop(e){
    e.preventDefault()
    var data = e.dataTransfer.getData("text");
    e.target.appendChild(document.getElementById(data));
    
    // Need to check if the containting div has text = to image name for correct/incorrect stuff

    pic = document.getElementById("dragpic");
    pic.classList.add("placeAni");
    
    // Remove Image in sync with animation (1s)
    setTimeout(function(){
        location.reload()
    },800)


}

// add a new image to center
function ResetImg(){

}

document.addEventListener("keydown", (e) => {
    console.log('HI')
});


// Set image box texts
/*
for(var i = 1; i<9;i++){
    document.getElementById(String(i)).textContent = String(i).concat(" hehe");
}
*/
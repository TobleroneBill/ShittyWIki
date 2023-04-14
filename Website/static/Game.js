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
    imgLink = pic.src
    imgLink = String(imgLink)
    Dirs = imgLink.split('/')
    image = null
    Dirs.forEach(element => {
        if (String(element).search('.jpg') != -1 ){
            image = element
        }
    });
    image = image.replace('.jpg','')    // this is raw name 
    //console.log(image)
    pic = document.getElementById("dragpic");
    parent = pic.parentElement
    ChooseText = parent.children[0].innerHTML

    // detect if choice is correct
    if (encodeURIComponent(ChooseText) == image){
        parent.classList.add("correctPlace");
    } else{
        parent.classList.add("incorrectPlace");
    }
    console.log(ChooseText)
    pic.classList.add("placeAni");
    
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


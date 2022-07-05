let song = document.querySelectorAll(".song");

for (const songs of song) {
songs.addEventListener("click", function playSong() {
    let player = document.querySelector('#player')
    player.src = songs.dataset.parent
    console.log(song)
})
}

let albumQuery = (new URL(document.location)).searchParams
let album = albumQuery.get('album')
let dropDown = document.querySelector('#id_album')
dropDown.value = album
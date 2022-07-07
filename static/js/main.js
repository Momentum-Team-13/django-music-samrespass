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
let artist = albumQuery.get('artist')
if (album != null) {
let dropDown = document.querySelector('#id_album')
dropDown.value = album
}
if (artist != null) {
let dropDown = document.querySelector('#id_artist')
dropDown.value = artist
}




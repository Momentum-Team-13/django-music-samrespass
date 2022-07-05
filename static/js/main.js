let song = document.querySelectorAll(".song");

for (const songs of song) {
songs.addEventListener("click", function playSong() {
    let player = document.querySelector('#player')
    player.src = songs.dataset.parent
    console.log(song)
})
}


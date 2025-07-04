//console.log("checking things Yo know");
// let img1= "C:\\Users\\Lenovo\\Desktop\\Mah Code\\Flask_use\\static\\images\\Gahiro.png";
// let mp3_1="C:\Users\Lenovo\Desktop\Mah Code\Flask_use\static\music\Gahiro.mp3"; 
// console.log("img url:", img1);

// let img2= "{{ url_for('static', filename='images/SHANGRILA.png') }}";
// let mp3_2= "{{ url_for('static', filename='music/SHANGRILA.mp3') }}"; 

// let img3= "{{ url_for('static', filename='images/Udayo_Relaile.png') }}";
// let mp3_3= "{{ url_for('static', filename='music/Udayo Relaile.mp3') }}"; 

// let img4= "{{ url_for('static', filename='images/Badi_Mushkil_Hai.png') }}";
// let mp3_4= "{{ url_for('static', filename='music/Badi Mushkil Hai.mp3') }}"; 

// let img5= "{{ url_for('static', filename='images/Dark_Souls_3_Main_Theme.png') }}";
// let mp3_5= "{{ url_for('static', filename='music/Dark Souls 3 Main Theme.mp3') }}"; 

const base_url = '/static/images';
const base_mp3 = '/static/music';

let now_playing = document.querySelector('.now-playing');
let track_art = document.querySelector('.track-art');
let track_name = document.querySelector('.track-name');
let track_artist = document.querySelector('.track-artist');

let playpause_btn = document.querySelector('.playpause-track');
let next_btn = document.querySelector('.next-track');
let prev_btn = document.querySelector('.prev-track');

let seek_slider = document.querySelector('.seek_slider');
let volume_slider = document.querySelector('.volume_slider');
let curr_time = document.querySelector('.current-time');
let total_duration = document.querySelector('.total-duration');
//let wave = document.getElementById('.wave');
//let randomIcon = document.querySelector('.fa-random');
let curr_track = document.createElement('audio');

let track_index = 0;
let isPlaying = false;
let isRandom = false;
let updateTimer;

const music_list = [
    {
        img: base_url + '/Gahiro.png',
        name: 'Gahiro',
        artist: 'Monkey Temple',
        music: base_mp3 + '/Gahiro.mp3',
    },

    {
        img: base_url + '/SHANGRILA.png',
        name: 'SHANGRILA',
        artist: 'SteelHeart',
        music: base_mp3 + '/SHANGRILA.mp3',
    },

    {
        img: base_url + '/Udayo_Relaile.png',
        name: 'Udayo Relaile',
        artist: 'Nepathya',
        music: base_mp3 + '/Udayo Relaile.mp3',
    },

    {
        img: base_url + '/Badi_Mushkil_Hai.png',
        name: 'Badi Mushkil Hai',
        artist: 'Abhijeet, Sameer',
        music: base_mp3 + '/Badi Mushkil Hai.mp3',
    },

    {
        img: base_url + '/Dark_Souls_3_Main_Theme.png',
        name: 'Dark Souls 3',
        artist: 'Yuka Kitamura',
        music: base_mp3 + '/Dark Souls 3 Main Theme.mp3',
    }

    
];

loadTrack(track_index);

function loadTrack(track_index){
    clearInterval(updateTimer);
    reset();

    curr_track.src = music_list[track_index].music;
    curr_track.load();

    track_art.style.backgroundImage = "url(" + music_list[track_index].img + ")";
    console.log( music_list[track_index].img)
    track_name.textContent = music_list[track_index].name;
    track_artist.textContent = music_list[track_index].artist;
    now_playing.textContent = "Playing Music " + (track_index + 1) + " of " + music_list.length;

    updateTimer = setInterval(setUpdate, 1000);
    curr_track.addEventListener('ended', nextTrack);
    random_bg_color();
}

function random_bg_color(){
    let hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e'];
    let a;

    function populate(a){
        for(let i=0; i<6; i++){
            let x = Math.round(Math.random()*14);
            let y = hex[x];
            a += y;
        }
        return a;
    }
    let Color1 = populate('#');
    let Color2 = populate('#');
    var angle = 'to right';

    let gradient = 'linear-gradient(' + angle + ',' + Color1 + ', ' + Color2 + ")";
    document.body.style.background = gradient;
}

function reset(){
    curr_time.textContent = "00:00";
    total_duration.textContent = "00:00";
    seek_slider.value = 0;
}
function randomTrack(){
    isRandom ? pauseRandom() : playRandom();
}
function playRandom(){
    isRandom = true;

    //randomIcon.classList.add('randomActive');
}
function pauseRandom(){
    isRandom = false;
    //randomIcon.classList.remove('randomActive');
}
function repeatTrack(){
    let current_index = track_index;
    loadTrack(current_index);
    playTrack();
}
function playpauseTrack(){
    isPlaying ? pauseTrack() : playTrack();
}
function playTrack(){
    curr_track.play();
    isPlaying = true;
    //track_art.classList.add(rotate);
    //wave.classList.add('loader');
    playpause_btn.innerHTML = '<i class="fa-solid fa-pause"></i>';
}
function pauseTrack(){
    curr_track.pause();
    isPlaying = false;
    //track_art.classList.remove(rotate);
    //wave.classList.remove('loader');
    playpause_btn.innerHTML = '<i class="fa-solid fa-play"></i>';
}

function nextTrack(){
    if(track_index < music_list.length -1 && isRandom === false){
        track_index += 1;
    }
    else if(track_index < music_list.length -1 && isRandom === true){
        let random_index = Number.parseInt(Math.random()* music_list.length);
        track_index = random_index;
    }
    else{
        track_index = 0;
    }

    loadTrack(track_index);
    playTrack();
}

function prevTrack(){
    if(track_index > 0){
        track_index -= 1;
    }
    else{
        track_index = music_list.length - 1;
    }
    loadTrack(track_index);
    playTrack();
}
function seekTo(){
    let seekto = curr_track.duration * (seek_slider.value / 100);
    curr_track.currentTime = seekto;
}
function setVolume(){
    curr_track.volume = volume_slider.value / 100;
}

function setUpdate(){
    let seekPosition = 0;
    if(!isNaN(curr_track.duration)){
        seekPosition = curr_track.currentTime * (100 / curr_track.duration);
        seek_slider.value = seekPosition;

        let currentMinutes = Math.floor(curr_track.currentTime / 60);
        let currentSeconds = Math.floor(curr_track.currentTime - currentMinutes * 60);
        let durationMinutes = Math.floor(curr_track.duration / 60);
        let durationSeconds = Math.floor(curr_track.duration - durationMinutes * 60);

        if(currentSeconds < 10){
            currentSeconds = "0" + currentSeconds;
        }
        if(durationSeconds < 10){
            durationSeconds = "0" + durationSeconds;
        }
        if(currentMinutes < 10){
            currentMinutes = "0" + currentMinutes;
        }
        if(durationMinutes < 10){
            durationMinutes = "0" + durationMinutes;
        }

        curr_time.textContent = currentMinutes + ":" + currentSeconds;
        total_duration.textContent = durationMinutes + ":" + durationSeconds;
    }
}
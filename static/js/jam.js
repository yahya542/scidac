
 function updateTime(){
    var currentTime = new Date(); 
    var hours = currentTime.getHours() ;
    var minutes = currentTime.getMinutes();
    var seconds = currentTime.getSeconds();


//edit gaya 
    hours = (hours < 10 ? "0" : "") + hours ;
    minutes = (minutes < 10 ? "0" : "") + minutes ;
    seconds = (seconds < 10 ? "0" : "") + seconds ;

    //format penuisan 
    var timeString = hours + ":" + minutes + ":" + seconds;

    document.getElementById("waktu").innerText = timeString;

}

// atur intervalnya 
setInterval(updateTime, 1000); 

updateTime();
 
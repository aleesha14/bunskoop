document.addEventListener('DOMContentLoaded', function() {


var a;
a = document.getElementById("circle");
txt = document.getElementById("text_air");



console.log("hi")
fetch('air_js')
.then(response => response.json())
.then(aqi => {

const aqi_var = aqi 



if (aqi_var > 301) {
  a.style.color = "#7e0022"
  txt.innerHTML="Hazardous"
 
}

else if  (aqi_var > 200 && aqi_var < 300) {
  a.style.color = "#8f4097"
  txt.innerHTML="Very Unhealthy"
  
}

else if (aqi_var > 151 && aqi_var < 200) {
  a.style.color = "#ff0000"
  txt.innerHTML="Unhealthy"
 
  
}

else if (aqi_var > 101 && aqi_var < 150) {
  a.style.color = "#ff7e00"
  txt.innerHTML="Unhealthy for Sensitive Groups"
  
}

else if (aqi_var > 51 && aqi_var < 100) {
  a.style.color = "#feff01"
  txt.innerHTML="Moderate"
  
}

else if (aqi_var > 0 && aqi_var < 50) {
  a.style.color = "#0de301"
  txt.innerHTML="Good"
  
}



console.log("hello")
})

})








function chargebattery() {
  var a;
  a = document.getElementById("circle");
  a.innerHTML = "&#xf192;";
  setTimeout(function () {
    a.innerHTML = "&#xf111;";
  }, 1000);
  setTimeout(function () {
    a.innerHTML = "&#xf192;";
  }, 2000);
  setTimeout(function () {
    a.innerHTML = "&#xf111;";
  }, 3000);
  setTimeout(function () {
    a.innerHTML = "&#xf192;";
  }, 4000);
}
chargebattery();
setInterval(chargebattery, 3000);



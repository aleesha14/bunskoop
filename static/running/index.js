document.addEventListener('DOMContentLoaded', function() {




  console.log("hi")
  $('.carousel').carousel({
  interval: 3000
})

})


function chargebattery() {
  var a;
  a = document.getElementById("charging");
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
setInterval(chargebattery, 5000);

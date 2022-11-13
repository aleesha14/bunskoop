document.addEventListener('DOMContentLoaded', function() {


document.querySelector('.top_container').style.display = 'flex';
document.querySelector('#runs_container').style.display = 'flex';
document.querySelector('#add_run').style.display = 'none';


})


function add_run() {
document.querySelector('.top_container').style.display = 'none';
document.querySelector('#runs_container').style.display = 'none';
document.querySelector('#add_run').style.display = 'block';


}
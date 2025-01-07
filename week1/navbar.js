const Hambur = document.getElementById('hambur');
const menu = document.getElementById('menu');
const cross = document.getElementById('cross');

Hambur.addEventListener('click', function(){
    menu.classList.add('active');
    cross.classList.add('block');
});

cross.addEventListener('click',function(){
    menu.classList.remove('active');
});
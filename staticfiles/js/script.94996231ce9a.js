const active_burger = document.querySelector('.active_burger');
const right_content = document.querySelector('.right_content');
// querySelector connected your class in html




// burger is active!!

active_burger.addEventListener('click' , e => {
    e.preventDefault();
    right_content.classList.toggle('active-navbar')
})
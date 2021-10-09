const active_burger = document.querySelector('.active_burger');
const right_content = document.querySelector('.right_content');
// querySelector connected your class in html

// // inputs documents on html
// let nameInput = document.querySelector('.inputName');
// let inputSecondName = document.querySelector('.inputSecondName');
// let inputMidleName = document.querySelector('.inputMidleName');
// let inputNumber = document.querySelector('.leftinput');
// let emailInput = document.querySelector('.emailInput');
// let dateInput = document.querySelector('.dateInput');
// let inputPasport = document.querySelector('.inputPasport');
// let AddressInput = document.querySelector('.AddressInput');
// let dataGive = document.querySelector('.dataGive');
// let datecompate = document.querySelector('.datecompate');

// let identityInput = document.querySelectorAll('.redinput')
// // button document on html
// let button = document.querySelector('.anketabutton');


// const base = [...identityInput]

// // validate
// button.addEventListener('click', e => {
//     e.preventDefault()

//     if(nameInput.value !== '' && inputSecondName.value !== '' && inputMidleName.value !== '' && inputNumber.value !== '' && emailInput.value !== '' && dateInput.value !== '' && inputPasport.value !== '' && AddressInput.value !== '' && dataGive.value !== '' && datecompate.value !== ''){
//         fetch('http://127.0.0.1:8000/' , {
//             method:'POST',
//             body:JSON.stringify({
//                 name:nameInput.value,
//                 secondName:inputSecondName.value,
//                 middleName:inputMidleName.value,
//                 number:inputNumber.value,
//                 email:emailInput.value,
//                 date:dateInput.value,
//                 passport:inputPasport.value,
//                 address:AddressInput.value,
//                 give:dataGive.value,
//                 compate:datecompate.value
//             })
//         }).then(res => res.json()).then(r => console.log(r))
//     }else if(nameInput.value == '' || inputSecondName.value == '' || inputMidleName.value == '' || inputNumber.value == '' || emailInput.value == '' || dateInput.value == '' || inputPasport.value == '' || AddressInput.value == '' || dataGive.value == '' || datecompate.value == ''){  
//         base.map(item =>{
//            item.style.borderColor = 'red'
//         })
//     }


// })



// burger is active!!

active_burger.addEventListener('click' , e => {
    e.preventDefault();
    right_content.classList.toggle('active-navbar')
})


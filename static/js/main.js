import { dom } from "./dom.js";

// This function is to initialize the application
function init() {
    // init data
    dom.init();
    // loads the boards to the screen
    dom.loadBoards();

    const modalRegister = document.querySelector('#my-modal-register');
    const modalLogin = document.querySelector('#my-modal-login');
    const modalBtnRegister = document.querySelector('#modal-btn-register');
    const modalBtnLogin = document.querySelector('#modal-btn-login');
    const closeBtnLogin = document.querySelector('.close-login');
    const closeBtnRegister = document.querySelector('.close-register');

    modalBtnRegister.addEventListener('click', openModalRegister);
    modalBtnLogin.addEventListener('click', openModalLogin);

    closeBtnLogin.addEventListener('click', closeModalLogin);
    closeBtnRegister.addEventListener('click', closeModalRegister);

    function openModalRegister() {
        modalRegister.style.display = 'block';
    }

    function openModalLogin() {
        modalLogin.style.display = 'block';
    }

    function closeModalRegister() {
         modalRegister.style.display = 'none';
    }

    function closeModalLogin() {
        modalLogin.style.display = 'none';
    }


}


init();

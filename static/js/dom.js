// It uses data_handler.js to visualize elements
import {dataHandler} from "./data_handler.js";

export let dom = {
    init: function () {
        // This function should run once, when the page is loaded.
    },
    loadBoards: function () {
        // retrieves boards and makes showBoards called
        dataHandler.getBoards(function (boards) {
            dom.showBoards(boards);
        });
    },
    showBoards: function (boards) {
        // shows boards appending them to #boards div
        // it adds necessary event listeners also

        let boardList = '';

        for (let board of boards) {
            boardList += `
            <section class="board">
                <div class="board-header"><span class="board-title">${board.title}</span>
                    <button class="btn btn-dark" id="buttonNewCardForBoard${board.id}">Add Card</button>            
                </div>
            </section>
            `;
        }

        const outerHtml = `
            <ul class="board-container">
                ${boardList}
            </ul>
        `;

        let boardsContainer = document.querySelector('#boards');
        boardsContainer.insertAdjacentHTML("beforeend", outerHtml);

        const boardButtons = document.getElementsByTagName('button');
        for (let button of boardButtons) {
            if (button.id.slice(0, 21) === 'buttonNewCardForBoard') {
                button.addEventListener('click', dom.createNewCard);
            }
        }


    },
    loadCards: function (boardId) {
        // retrieves cards and makes showCards called
    },
    showCards: function (cards) {
        // shows the cards of a board
        // it adds necessary event listeners also
    },
    // here comes more features
    createNewCard: function (event) {
        // console.log(event);
        let cardTitle = 'New Card';
        let boardId = event.target.id.slice(21);
        let statusId = 0;
        dataHandler.createNewCard(cardTitle, boardId, statusId, dom.alertWeb)
    },
    alertWeb: function (message) {
        alert(message);
        window.location.reload();

    }

};
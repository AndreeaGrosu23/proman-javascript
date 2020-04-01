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
                <div>
                <p>             
                    <div id="board-title" data-board-id = "${board.id}" data-board-title="${board.title}">${board.title}</div>
                    <button type="button" class="btn btn-dark mr-1 rounded border-secondary" id="buttonNewCardForBoard${board.id}">Add Card</button>
                </p>
                    </div>
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
        for (let button of boardButtons){
            if (button.id.slice(0,21) === 'buttonNewCardForBoard'){
                button.addEventListener('click', dom.createNewCard );
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
        dataHandler.createNewCard(cardTitle,boardId,statusId)
    }

};
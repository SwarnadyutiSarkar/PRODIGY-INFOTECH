document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('game-board');
    const cells = document.querySelectorAll('.cell');
    const message = document.getElementById('message');
    const resetButton = document.getElementById('reset');

    let currentPlayer = 'X'; // Player starts first
    let boardState = ['', '', '', '', '', '', '', '', ''];
    let isGameActive = true;

    const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];

    function checkWinner() {
        for (const condition of winningConditions) {
            const [a, b, c] = condition;
            if (boardState[a] && boardState[a] === boardState[b] && boardState[a] === boardState[c]) {
                return boardState[a];
            }
        }
        return boardState.includes('') ? null : 'Tie';
    }

    function updateGameState(index) {
        if (isGameActive && !boardState[index]) {
            boardState[index] = currentPlayer;
            cells[index].textContent = currentPlayer;
            cells[index].classList.add(currentPlayer.toLowerCase());

            const winner = checkWinner();
            if (winner) {
                isGameActive = false;
                message.textContent = winner === 'Tie' ? "It's a Tie!" : `Player ${winner} Wins!`;
                return;
            }

            // Switch to AI turn
            currentPlayer = 'O';
            message.textContent = `Player ${currentPlayer}'s Turn`;
            setTimeout(aiMove, 500); // AI moves after a short delay
        }
    }

    function aiMove() {
        let emptyCells = boardState.map((value, index) => value === '' ? index : null).filter(index => index !== null);

        if (emptyCells.length === 0) return; // No moves available, should be handled already

        const randomIndex = emptyCells[Math.floor(Math.random() * emptyCells.length)];
        boardState[randomIndex] = 'O';
        cells[randomIndex].textContent = 'O';
        cells[randomIndex].classList.add('o');

        const winner = checkWinner();
        if (winner) {
            isGameActive = false;
            message.textContent = winner === 'Tie' ? "It's a Tie!" : `Player ${winner} Wins!`;
            return;
        }

        // Switch to Player X turn
        currentPlayer = 'X';
        message.textContent = `Player ${currentPlayer}'s Turn`;
    }

    function resetGame() {
        boardState = ['', '', '', '', '', '', '', '', ''];
        isGameActive = true;
        currentPlayer = 'X'; // Player starts first
        message.textContent = `Player ${currentPlayer}'s Turn`;
        cells.forEach(cell => {
            cell.textContent = '';
            cell.classList.remove('x', 'o');
        });
    }

    board.addEventListener('click', (event) => {
        const index = event.target.dataset.index;
        if (index !== undefined) {
            updateGameState(index);
        }
    });

    resetButton.addEventListener('click', resetGame);
});

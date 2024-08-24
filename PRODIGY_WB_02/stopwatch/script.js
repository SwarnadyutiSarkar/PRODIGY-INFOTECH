document.addEventListener('DOMContentLoaded', () => {
    const startButton = document.getElementById('start');
    const pauseButton = document.getElementById('pause');
    const resetButton = document.getElementById('reset');
    const lapButton = document.getElementById('lap');
    const timeDisplay = document.getElementById('time-display');
    const lapList = document.getElementById('lap-list');

    let startTime, updatedTime, difference, tInterval, running = false;
    let seconds = 0, minutes = 0, hours = 0;

    function startTimer() {
        if (!running) {
            running = true;
            startTime = new Date().getTime();
            tInterval = setInterval(getShowTime, 1);
        }
    }

    function pauseTimer() {
        if (running) {
            running = false;
            clearInterval(tInterval);
        }
    }

    function resetTimer() {
        running = false;
        clearInterval(tInterval);
        seconds = 0;
        minutes = 0;
        hours = 0;
        timeDisplay.textContent = '00:00:00';
        lapList.innerHTML = '';
    }

    function getShowTime() {
        updatedTime = new Date().getTime();
        difference = updatedTime - startTime;

        seconds = Math.floor((difference % (1000 * 60)) / 1000);
        minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
        hours = Math.floor(difference / (1000 * 60 * 60));

        seconds = (seconds < 10) ? "0" + seconds : seconds;
        minutes = (minutes < 10) ? "0" + minutes : minutes;
        hours = (hours < 10) ? "0" + hours : hours;

        timeDisplay.textContent = hours + ":" + minutes + ":" + seconds;
        updateClock();
    }

    function updateClock() {
        const now = new Date();
        const seconds = now.getSeconds();
        const minutes = now.getMinutes();
        const hours = now.getHours();

        document.querySelector('.hand.second').style.transform = `rotate(${seconds * 6}deg)`;
        document.querySelector('.hand.minute').style.transform = `rotate(${(minutes + seconds / 60) * 6}deg)`;
        document.querySelector('.hand.hour').style.transform = `rotate(${(hours + minutes / 60) * 30}deg)`;
    }

    function recordLap() {
        if (running) {
            const lapTime = timeDisplay.textContent;
            const lapItem = document.createElement('li');
            lapItem.textContent = lapTime;
            lapList.appendChild(lapItem);
        }
    }

    startButton.addEventListener('click', startTimer);
    pauseButton.addEventListener('click', pauseTimer);
    resetButton.addEventListener('click', resetTimer);
    lapButton.addEventListener('click', recordLap);
});

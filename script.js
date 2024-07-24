// Инициализация переменных
let coins = 0; // Количество монет
let level = 1; // Уровень игры
let progress = 0; // Текущий прогресс
let maxProgress = 10; // Максимальный прогресс для уровня

// Получаем элементы из DOM
const scoreElement = document.getElementById('score'); // Элемент счетчика
const levelElement = document.getElementById('level'); // Элемент уровня
const progressBarElement = document.getElementById('progress-bar'); // Элемент прогресс-бара
const messageElement = document.getElementById('message'); // Элемент сообщения

// Обработчик клика по монете
document.getElementById('coin').addEventListener('click', () => {
    coins += level; // Увеличиваем количество монет на уровень
    scoreElement.innerText = coins; // Обновляем текст счетчика

    progress++; // Увеличиваем прогресс
    
    // Проверяем, достигнут ли максимальный прогресс
    if (progress >= maxProgress) {
        level++; // Увеличиваем уровень
        maxProgress *= 2; // Увеличиваем максимальный прогресс в 2 раза
        progress = 0; // Сбрасываем прогресс
        levelElement.innerText = `Level ${level}`; // Обновляем текст уровня
    }

    // Обновляем ширину прогресс-бара
    const progressPercentage = (progress / maxProgress) * 100;
    progressBarElement.style.width = `${progressPercentage}%`;
});

// // Функция для отображения недоступных разделов
// function showSection(section) {
//     if (section === 'friends' || section === 'tasks') {
//         messageElement.innerText = "Этот раздел пока недоступен."; // Сообщение о недоступности раздела
//         showSection.classList.add('fade');
//     }
// }

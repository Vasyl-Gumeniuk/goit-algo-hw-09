## Жадібні алгоритми та динамічне програмування 

**Завдання 1: Функція жадібного алгоритму find_coins_greedy**. Ця функція повинна приймати суму, яку потрібно видати покупцеві, і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.

**Завдання 2: Функція динамічного програмування find_min_coins**. Ця функція також повинна приймати суму для видачі решти, але використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для формування цієї суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом. Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}.


### Результати роботи:
1. Ефективність за часом виконання:
- Жадібний алгоритм виконується досить швидко, оскільки просто перебирає доступні монети та обчислює відповідну кількість для кожної з них.
- Алгоритм динамічного програмування може бути більш повільним через рекурсивний підхід та мемоїзацію, але він гарантує знаходження оптимального рішення.

2. Робота з великими сумами:
- Жадібний алгоритм може показати гарні результати при малих сумах або в ситуаціях, де монети мають певні правила.
- Алгоритм динамічного програмування краще справляється з великими сумами, оскільки ефективно використовує мемоїзацію, уникненнячи зайвих обчислень.


### Висновки до роботи:

Жадібний алгоритм простий у реалізації та виконується досить швидко, але може давати неоптимальні результати у випадках з нестандартними номіналами монет або великими сумами.
Алгоритм динамічного програмування складніший у реалізації, але гарантує знаходження оптимального рішення та ефективно працює з великими сумами. Він особливо корисний у ситуаціях, де необхідно забезпечити найменшу кількість монет для видачі великих сум.
Загалом, обидва алгоритми мають свої переваги та недоліки і можуть бути використані в залежності від потреб конкретної задачі.

def boyer_moore_search(text, pattern):
    """
    Алгоритм Боєра-Мура для пошуку підрядка в тексті.
    """
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1

    # Таблиця зсувів
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    # Пошук
    shifts = 0
    while shifts <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shifts + j]:
            j -= 1

        if j < 0:
            return shifts  # Повертаємо позицію першого входження
        else:
            shifts += max(1, j - bad_char.get(text[shifts + j], -1))

    return -1
def kmp_search(text, pattern):
    """
    Алгоритм Кнута-Морріса-Пратта для пошуку підрядка.
    """
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1

    # Побудова таблиці префіксів
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j

    # Пошук
    i = 0
    j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j  # Повертаємо позицію першого входження
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1
def rabin_karp_search(text, pattern, prime=101):
    """
    Алгоритм Рабіна-Карпа для пошуку підрядка.
    """
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1

    base = 256  # Кількість символів у наборі ASCII
    pattern_hash = 0
    text_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i  # Повертаємо позицію першого входження

        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return -1
import timeit

# Зчитування файлів
with open("D:/GoIT/PROJECTS Python/vs - code - basics/стаття1.txt", "r", encoding="utf-8") as file1, \
     open("D:/GoIT/PROJECTS Python/vs - code - basics/стаття2.txt", "r", encoding="utf-8") as file2:
    text1 = file1.read()
    text2 = file2.read()


# Вибір підрядків
existing_pattern = "алгоритм"  # Слово, що існує в тексті
non_existing_pattern = "немаєтакогослова"  # Вигадане слово

# Функція для вимірювання часу виконання
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=1)

# Тестування
algorithms = {
    "Boyer-Moore": boyer_moore_search,
    "Knuth-Morris-Pratt": kmp_search,
    "Rabin-Karp": rabin_karp_search
}

for name, algo in algorithms.items():
    print(f"\nАлгоритм: {name}")
    for text, text_name in [(text1, "Стаття 1"), (text2, "Стаття 2")]:
        time_existing = measure_time(algo, text, existing_pattern)
        time_non_existing = measure_time(algo, text, non_existing_pattern)
        print(f"{text_name}:")
        print(f"  Існуючий підрядок: {time_existing:.6f} секунд")
        print(f"  Вигаданий підрядок: {time_non_existing:.6f} секунд")

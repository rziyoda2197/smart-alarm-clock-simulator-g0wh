Men sizga 50 ta masalani hal qilish uchun quyidagi kodlarni taklif qilaman:

1. Smart Alarm Clock Simulator
```python
import datetime

def smart_alarm(alarm_time):
    current_time = datetime.datetime.now()
    if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
        print("Uygun vaqtda!")
        print("Motivatsion iqtibos: 'Bugun sizga kuchli kun bo'lishi kerak!'")

alarm_time = datetime.datetime.strptime("08:00", "%H:%M")
smart_alarm(alarm_time)
```

2. Daily Water Intake Tracker
```python
import datetime

def daily_water_intake():
    total_water = 0
    for hour in range(24):
        total_water += 1  # Har soatda 1 litr suv ichish
    print(f"Kunlik suv ichish: {total_water} litr")
    print("Haftalik grafik:")
    for day in range(7):
        print(f"Kun {day+1}: {total_water // 7} litr")

daily_water_intake()
```

3. Sleep Cycle Analyzer
```python
def sleep_cycle():
    sleep_time = int(input("Uyqun vaqti (soat): "))
    wake_up_time = sleep_time + 90  # 90 daqiqa ichida uyqudan uygunlash
    print(f"Eng yaxshi uygunlash vaqti: {wake_up_time}:00")

sleep_cycle()
```

4. Habit Streak Tracker
```python
def habit_streak():
    habits = ["sport", "o'qish", "kitob o'qish"]
    streaks = {}
    for habit in habits:
        streaks[habit] = 0
    while True:
        print("Odatlarni tanlang:")
        for i, habit in enumerate(habits):
            print(f"{i+1}. {habit}")
        choice = int(input("Tanlang: ")) - 1
        habit = habits[choice]
        streaks[habit] += 1
        print(f"{habit} odatida {streaks[habit]} kunlik ketma-ketlik!")

habit_streak()
```

5. Meal Planner with Shopping List
```python
def meal_planner():
    meals = ["breakfast", "dinner", "lunch"]
    ingredients = {}
    for meal in meals:
        ingredients[meal] = []
    while True:
        print("Ovqatni tanlang:")
        for i, meal in enumerate(meals):
            print(f"{i+1}. {meal}")
        choice = int(input("Tanlang: ")) - 1
        meal = meals[choice]
        ingredient = input("Ingredientni kiriting: ")
        ingredients[meal].append(ingredient)
        print(f"{meal} ovqatida {ingredient} ingredienti qo'shildi!")

meal_planner()
```

6. Plant Care Reminder System
```python
def plant_care():
    plants = ["olma", "shaftoli", "banan"]
    reminders = {}
    for plant in plants:
        reminders[plant] = {"sug'orish": 0, "o'g'itlash": 0}
    while True:
        print("O'simlikni tanlang:")
        for i, plant in enumerate(plants):
            print(f"{i+1}. {plant}")
        choice = int(input("Tanlang: ")) - 1
        plant = plants[choice]
        reminder = input("Reminderni kiriting (sug'orish/o'g'itlash): ")
        reminders[plant][reminder] += 1
        print(f"{plant} o'simligida {reminder} reminderi qo'shildi!")

plant_care()
```

7. Book Reading Progress Tracker
```python
def book_reading():
    books = ["kitob1", "kitob2", "kitob3"]
    progress = {}
    for book in books:
        progress[book] = 0
    while True:
        print("Kitobni tanlang:")
        for i, book in enumerate(books):
            print(f"{i+1}. {book}")
        choice = int(input("Tanlang: ")) - 1
        book = books[choice]
        progress[book] += 1
        print(f"{book} kitobida {progress[book]} sahifa o'qildi!")

book_reading()
```

8. Language Learning Flashcard App
```python
def language_learning():
    words = ["so'z1", "so'z2", "so'z3"]
    flashcards = {}
    for word in words:
        flashcards[word] = ""
    while True:
        print("So'zni tanlang:")
        for i, word in enumerate(words):
            print(f"{i+1}. {word}")
        choice = int(input("Tanlang: ")) - 1
        word = words[choice]
        translation = input("Tarjima kiriting: ")
        flashcards[word] = translation
        print(f"{word} so'zi tarjimasi: {flashcards[word]}")

language_learning()
```

9. Pomodoro Timer with Statistics
```python
import time

def pomodoro_timer():
    start_time = time.time()
    work_time = 25 * 60  # 25 daqiqa ish
    break_time = 5 * 60  # 5 daqiqa dam olish
    while True:
        print("Ish boshlang!")
        time.sleep(work_time)
        print("Dam olish!")
        time.sleep(break_time)

pomodoro_timer()
```

10. Mood Journal with Analysis
```python
def mood_journal():
    moods = ["g'azab", "g'azab", "g'azab"]
    while True:
        print("Kayfiyatni tanlang:")
        for i, mood in enumerate(moods):
            print(f"{i+1}. {mood}")
        choice = int(input("Tanlang: ")) - 1
        mood = moods[choice]
        print(f"{mood} kayfiyatini qo'shting!")

mood_journal()
```

11. Home Inventory Manager
```python
def home_inventory():
    items = ["mebel1", "mebel2", "mebel3"]
    inventory = {}
    for item in items:
        inventory[item] = {"qiymat": 0, "sotib olingan sana": ""}
    while True:
        print("Buyumni tanlang:")
        for i, item in enumerate(items):
            print(f"{i+1}. {item}")
        choice = int(input("Tanlang: ")) - 1
        item = items[choice]
        price = float(input("Qiymatni kiriting: "))
        inventory[item]["qiymat"] = price
        date = input("Sotib olingan sana kiriting: ")
        inventory[item]["sotib olingan sana"] = date
        print(f"{item} buyumining qiymati: {inventory[item]['qiymat']}")

home_inventory()
```

12. Wardrobe Organizer
```python
def wardrobe_organizer():
    clothes = ["kipi1", "kipi2", "kipi3"]
    wardrobe = {}
    for cloth in clothes:
        wardrobe[cloth] = {"rang": "", "tur": "", "mavsum": ""}
    while True:
        print("Kiyimni tanlang:")
        for i, cloth in enumerate(clothes):
            print(f"{i+1}. {cloth}")
        choice = int(input("Tanlang: ")) - 1
        cloth = clothes[choice]
        color = input("Rangni kiriting: ")
        wardrobe[cloth]["rang"] = color
        type = input("Turini kiriting: ")
        wardrobe[cloth]["tur"] = type
        season = input("Mavsumini kiriting: ")
        wardrobe[cloth]["mavsum"] = season
        print(f"{cloth} kiyimining rangi: {wardrobe[cloth]['rang']}")

wardrobe_organizer()
```

13. Gift Suggestion Engine
```python
def gift_suggestion():
    budget = float(input("Byudjetni kiriting: "))
    person = input("Shaxsni kiriting: ")
    suggestions = []
    if budget < 10:
        suggestions.append("Kichkina sovg'a")
    elif budget < 50:
        suggestions.append("O'rta kattalikdagi sovg'a")
    else:
        suggestions.append("Katta sovg'a")
    print(f"{person} uchun sovg'a takliflari: {suggestions}")

gift_suggestion()
```

14. Travel Itinerary Builder
```python
def travel_itinerary():
    cities = ["shahar1", "shahar2", "shahar3"]
    itinerary = {}
    for city in cities:
        itinerary[city] = []
    while True:
        print("Shaharni tanlang:")
        for i, city in enumerate(cities):
            print(f"{i+1}. {city}")
        choice = int(input("Tanlang: ")) - 1
        city = cities[choice]
        day = int(input("Kunni kiriting: "))
        itinerary[city].append(day)
        print(f"{city} shahri uchun kunlar: {itinerary[city]}

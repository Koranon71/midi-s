import os

# Наша база известных треков (сверяется по чистому имени, без папок и .mid)
KNOWN_TRACKS = {
    "12 стульев": "х/ф «12 стульев»",
    "a real hero": "Electric Youth (Drive OST)",
    "a step forward into terror": "Guilty Gear Xrd",
    "addict": "Hazbin Hotel (Отель Хазбин)",
    "america fuck yeah": "Team America: World Police",
    "angel of doom": "Neon Genesis Evangelion",
    "bad apple": "Touhou Project",
    "benny hill": "Шоу Бенни Хилла (Yakety Sax)",
    "better call saul": "Лучше звоните Солу / Breaking Bad",
    "bitter choco decoration": "syudou feat. Hatsune Miku",
    "blood theme": "Декстер (Dexter OST)",
    "borderline case": "The End of Evangelion",
    "both of you dance like you want to win": "Neon Genesis Evangelion",
    "breaking bad ost": "Во все тяжкие",
    "come along with me": "Время Приключений (Adventure Time)",
    "cruel angel thesis": "Neon Genesis Evangelion (ТВ-опенинг)",
    "cruel angel thesis #2": "Neon Genesis Evangelion (ТВ-опенинг)",
    "daddy cop": "Сериал «Новичок» (The Rookie)",
    "decisive battle": "Neon Genesis Evangelion",
    "duvet": "Serial Experiments Lain (bôa)",
    "duvet #2": "Serial Experiments Lain (bôa)",
    "everything stays": "Время Приключений (Adventure Time)",
    "everything you've ever dreamed": "Neon Genesis Evangelion",
    "eye of the tiger": "Survivor (Рокки III)",
    "for the damage coda": "Рик и Морти (Злой Морти / Blonde Redhead)",
    "gonna fly": "Рокки (Rocky Theme)",
    "good, bad, the ugly": "Хороший, плохой, злой (Эннио Морриконе)",
    "goodbuy moonman": "Рик и Морти (Goodbye Moonmen)",
    "hedgehog's dilemma": "Neon Genesis Evangelion",
    "i really want to stay at your house": "Cyberpunk: Edgerunners / Сайберпанк",
    "i'll be there for you": "Сериал «Друзья» (The Rembrandts)",
    "komm, suesser tod": "The End of Evangelion",
    "merry go round of life": "Ходячий замок Хаула (Джо Хисаиси)",
    "misato": "Neon Genesis Evangelion",
    "misirlou": "Криминальное чтиво (Pulp Fiction)",
    "nightcall": "Kavinsky (Drive OST)",
    "one last kiss": "Evangelion: 3.0+1.0 Thrice Upon a Time",
    "rei ii": "Neon Genesis Evangelion",
    "space oddity": "David Bowie",
    "speak softly love": "Крёстный отец (The Godfather)",
    "stuck in the middle with you": "Бешеные псы (Stealers Wheel)",
    "take a look around": "Миссия невыполнима 2 (Limp Bizkit)",
    "take me out": "Franz Ferdinand",
    "thanatos": "Neon Genesis Evangelion",
    "the amazing digital circus": "Удивительный цифровой цирк",
    "the beast ii": "Neon Genesis Evangelion",
    "the chase": "Neon Genesis Evangelion",
    "the entertainer": "Скотт Джоплин (Рэгтайм)",
    "the lonely shepherd": "Убить Билла (Джеймс Ласт и Георге Замфир)",
    "the phantom of the opera": "Призрак Оперы",
    "the phantom of the opera #2": "Призрак Оперы",
    "this fffire": "Franz Ferdinand (Cyberpunk: Edgerunners)",
    "twisted nerve": "Убить Билла (Свист / Бернард Херрманн)",
    "una mattina": "1+1 / Неприкасаемые (Людовико Эйнауди)",
    "unravel": "Токийский гуль (Tokyo Ghoul)",
    "unwelcome school": "Blue Archive",
    "we are number one": "Лентяево (LazyTown)",
    "we both reached for a gun": "Мюзикл «Чикаго» (Chicago)",
    "where is my mind": "Бойцовский клуб (Pixies)",
    "you'll be okay": "Адский босс (Helluva Boss)",
    "your idol": "Звёздное дитя / Oshi no Ko (YOASOBI - Idol)",
    "your new home": "Удивительный цифровой цирк",
    "братья пилоты": "Следствие ведут Колобки",
    "бригада": "Сериал «Бригада» (главная тема)",
    "бумер": "х/ф «Бумер» (мобильник)",
    "в синем море,в белой пене": "м/ф «В синем море, в белой пене...»",
    "деревня дураков": "Каламбур (Деревня дураков)",
    "ночной дозор": "х/ф «Ночной дозор» (Уматурман)",
    "ну погоди": "м/ф «Ну, погоди!»",
    "песенка о вреде курения": "м/ф «Остров сокровищ»",
    "песня гениального сыщика": "м/ф «Бременские музыканты»",
    "песня капитана врунгеля": "м/ф «Приключения капитана Врунгеля»",
    "тайна третьей планеты": "м/ф «Тайна третьей планеты»",
    "another brick in the wall": "Pink Floyd",
    "back in black": "AC/DC",
    "bad to the bone": "George Thorogood (Терминатор 2)",
    "black hole sun": "Soundgarden",
    "bohemian rhapsody": "Queen",
    "bring me to life": "Evanescence",
    "can't stop": "Red Hot Chili Peppers",
    "carry on my wayward son": "Kansas (Сверхъестественное)",
    "come as you are": "Nirvana",
    "do the evolution": "Pearl Jam",
    "dream on": "Aerosmith",
    "engel": "Rammstein",
    "englishman in new york": "Sting",
    "enter sandman": "Metallica",
    "every breath you take": "The Police",
    "everybody wants to rule the world": "Tears for Fears",
    "exit music": "Radiohead (Exit Music For a Film)",
    "faint": "Linkin Park",
    "for whom the bell tolls": "Metallica",
    "fortunate son": "Creedence Clearwater Revival",
    "free bird": "Lynyrd Skynyrd",
    "hotel california": "Eagles",
    "house of the rising sun": "The Animals",
    "in the end": "Linkin Park",
    "it's my life": "Bon Jovi",
    "karma police": "Radiohead",
    "lemon tree": "Fools Garden",
    "livin' on a prayer": "Bon Jovi",
    "master of puppets": "Metallica",
    "numb": "Linkin Park",
    "paint it black": "The Rolling Stones",
    "paranoid": "Black Sabbath",
    "paranoid android": "Radiohead",
    "primo victoria": "Sabaton",
    "roundabout": "Yes (JoJo's Bizarre Adventure)",
    "seven nation army": "The White Stripes",
    "shut your mouth": "Pain",
    "smells like teen spirit": "Nirvana",
    "smoke on the water": "Deep Purple",
    "sonne": "Rammstein",
    "still loving you": "Scorpions",
    "sultans of swing": "Dire Straits",
    "the chain": "Fleetwood Mac",
    "the man who solds the world": "David Bowie / Nirvana",
    "thunderstruck": "AC/DC",
    "welcome to the black parade": "My Chemical Romance",
    "what i've done": "Linkin Park (Трансформеры OST)",
    "among us drip": "Амогус / Among Us Meme",
    "chipi chipi chapa chapa": "Boy interaction (Meme)",
    "close eyes": "DVRST (Мем с Мегамозгом)",
    "discord call": "Звук входящего звонка Discord",
    "entry of the gladiators": "Цирковой марш (Юлиус Фучик)",
    "nyan cat": "Нянкэт",
    "popipo": "Hatsune Miku (Meme)",
    "skype call": "Звук старого звонка Skype",
    "судно": "Молчат Дома",
    "atom bomb baby": "Fallout 4 (The Five Stars)",
    "beyond the sea": "BioShock / Bobby Darin",
    "big iron": "Fallout: New Vegas (Marty Robbins)",
    "blue moon": "Fallout: New Vegas (Frank Sinatra)",
    "feeling good": "Nina Simone / Muse",
    "hit the road jack": "Ray Charles",
    "i don't want to set the world on fire": "Fallout 3 (The Ink Spots)",
    "lone digger": "Caravan Palace (Electro Swing)",
    "mr.sandman": "The Chordettes",
    "sixteen tons": "Tennessee Ernie Ford",
    "505": "Arctic Monkeys",
    "blue monday": "New Order",
    "careless whisper": "George Michael",
    "charlie's inferno": "That Handsome Devil",
    "charlie's inferno #2": "That Handsome Devil",
    "gimme": "ABBA (Gimme! Gimme! Gimme!)",
    "never gonna give you up": "Рикролл / Rick Astley",
    "pumped up kicks": "Foster the People",
    "somebody that i used to know": "Gotye",
    "sweet dreams": "Eurythmics",
    "take on me": "A-ha",
    "video killed the radio star": "The Buggles",
    "virtual insanity": "Jamiroquai",
    "группа крови": "Кино (Виктор Цой)",
    "звезда по имени солнце": "Кино (Виктор Цой)",
    "батарейка": "Жуки",
    "белая ночь": "Форум / Виктор Салтыков",
    "белые розы": "Ласковый май / Юрий Шатунов",
    "владимирский централ": "Михаил Круг",
    "выхода нет": "Сплин",
    "как на войне": "Агата Кристи",
    "полковнику никто не пишет": "Би-2 (Брат 2 OST)",
    "трава у дома": "Земляне",
    "arstotzkan anthem": "Papers, Please",
    "attack of the killer queen": "Deltarune: Chapter 2",
    "bfg division": "DOOM (Мик Гордон)",
    "bonetrousle": "Undertale (Тема Папируса)",
    "cp violation": "Half-Life 2",
    "death by glamour": "Undertale (Тема Меттатона)",
    "in the pines": "Telltale's The Walking Dead",
    "it has to be this way": "Metal Gear Rising: Revengeance",
    "megalovania": "Undertale (Тема Санса)",
    "metro exodus": "Метро: Исход (Главная тема)",
    "right behind you": "Team Fortress 2 (Meet the Spy)",
    "rocket jump waltz": "Team Fortress 2",
    "soviet march": "Command & Conquer: Red Alert 3",
    "space asshole": "Спейс ассхолл (SS13 легенда)",
    "space station 14 ost": "Главная тема СС14",
    "spider dance": "Undertale (Тема Маффет)",
}

input_file = "tracks_list.txt"
output_file = "meta_info.txt"

if not os.path.exists(input_file):
    print(f"Ошибка: Файл '{input_file}' не найден!")
else:
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result_lines = []
    unknown_count = 0
    known_count = 0

    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        
        # Вытаскиваем чистое имя файла (без папки и без расширения .mid)
        track_name = cleaned_line.split('\\')[-1]
        track_name_clean = track_name.replace('.mid', '').replace('.MIDI', '').strip()
        
        lookup_key = track_name_clean.lower()

        if lookup_key in KNOWN_TRACKS:
            # Записываем в meta_info.txt именно чистое имя файла, чтобы generate_all.py его сопоставил
            result_lines.append(f"{track_name_clean} = {KNOWN_TRACKS[lookup_key]}\n")
            known_count += 1
        else:
            result_lines.append(f"{track_name_clean} = ???\n")
            unknown_count += 1

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(result_lines)

    print(f"Готово! Создан правильный файл '{output_file}'")
    print(f"Успешно размечено: {known_count}")
    print(f"Поставлено вопросов '???': {unknown_count}")
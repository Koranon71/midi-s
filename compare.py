# 1. Вставляешь сюда свой трек-лист с папками
track_list_raw = r"""
﻿Cinema_Anime_TV\12 стульев.mid
Cinema_Anime_TV\A real hero.mid
Cinema_Anime_TV\A step forward into terror.mid
Cinema_Anime_TV\Addict.mid
Cinema_Anime_TV\America fuck yeah.mid
Cinema_Anime_TV\Angel of doom.mid
Cinema_Anime_TV\Bad Apple.mid
Cinema_Anime_TV\Barefoot in the park.mid
Cinema_Anime_TV\Benny hill.mid
Cinema_Anime_TV\Better call Saul.mid
Cinema_Anime_TV\Bitter choco decoration.mid
Cinema_Anime_TV\Blood theme.mid
Cinema_Anime_TV\Borderline case.mid
Cinema_Anime_TV\Both of you dance like you want to win.mid
Cinema_Anime_TV\Breaking Bad OST.mid
Cinema_Anime_TV\Cantina.mid
Cinema_Anime_TV\Cell block tango.mid
Cinema_Anime_TV\Chikatto Chika Chika.mid
Cinema_Anime_TV\Come along with me.mid
Cinema_Anime_TV\Cooking by the book.mid
Cinema_Anime_TV\Cruel Angel Thesis #2.mid
Cinema_Anime_TV\Cruel Angel Thesis.mid
Cinema_Anime_TV\Daddy cop.mid
Cinema_Anime_TV\Decisive battle.mid
Cinema_Anime_TV\Duvet #2.mid
Cinema_Anime_TV\Duvet.mid
Cinema_Anime_TV\Edelweiss #2.mid
Cinema_Anime_TV\Edelweiss.mid
Cinema_Anime_TV\Escape to the beginning.mid
Cinema_Anime_TV\Everything stays.mid
Cinema_Anime_TV\Everything you've ever dreamed.mid
Cinema_Anime_TV\Expansion of blockade.mid
Cinema_Anime_TV\Eye of the tiger.mid
Cinema_Anime_TV\Far from any road.mid
Cinema_Anime_TV\Fate.mid
Cinema_Anime_TV\Fly me to the Moon.mid
Cinema_Anime_TV\For the damage coda.mid
Cinema_Anime_TV\Fugget about it.mid
Cinema_Anime_TV\Golden.mid
Cinema_Anime_TV\Gonna fly.mid
Cinema_Anime_TV\Good, bad, the ugly.mid
Cinema_Anime_TV\Goodbuy Moonmen #2.mid
Cinema_Anime_TV\Goodbye Moonmen.mid
Cinema_Anime_TV\Green hornet.mid
Cinema_Anime_TV\Hedgehog's dilemma.mid
Cinema_Anime_TV\How bad can i be.mid
Cinema_Anime_TV\I really want to stay at your house.mid
Cinema_Anime_TV\I'll be there for you.mid
Cinema_Anime_TV\Inferno.mid
Cinema_Anime_TV\Interference of others.mid
Cinema_Anime_TV\Komm suesser tod #2.mid
Cinema_Anime_TV\Komm susser tod.mid
Cinema_Anime_TV\Let us adore you.mid
Cinema_Anime_TV\Marking time, waiting for death.mid
Cinema_Anime_TV\Merry go round of life.mid
Cinema_Anime_TV\Misato.mid
Cinema_Anime_TV\Misirlou.mid
Cinema_Anime_TV\Mr.Cellophane.mid
Cinema_Anime_TV\Never meant to belong.mid
Cinema_Anime_TV\Nightcall.mid
Cinema_Anime_TV\Office.mid
Cinema_Anime_TV\One last kiss.mid
Cinema_Anime_TV\Opening of dream.mid
Cinema_Anime_TV\Razzle dazzle.mid
Cinema_Anime_TV\Rei II.mid
Cinema_Anime_TV\Renai circulation.mid
Cinema_Anime_TV\Round and round.mid
Cinema_Anime_TV\Running the show.mid
Cinema_Anime_TV\Shikanoko nokonoko koshitantan.mid
Cinema_Anime_TV\Skies of love.mid
Cinema_Anime_TV\Space oddity #2.mid
Cinema_Anime_TV\Space oddity.mid
Cinema_Anime_TV\Speak softly love #2.mid
Cinema_Anime_TV\Speak softly love #3.mid
Cinema_Anime_TV\Speak softly love.mid
Cinema_Anime_TV\Steve's lava chicken.mid
Cinema_Anime_TV\Stuck in the middle with you.mid
Cinema_Anime_TV\Substitute invasion.mid
Cinema_Anime_TV\Take a look around.mid
Cinema_Anime_TV\Take me out.mid
Cinema_Anime_TV\Thanatos.mid
Cinema_Anime_TV\The amazing digital circus.mid
Cinema_Anime_TV\The beast II.mid
Cinema_Anime_TV\The chase.mid
Cinema_Anime_TV\The entertainer.mid
Cinema_Anime_TV\The lion sleeps tonight.mid
Cinema_Anime_TV\The lonely shepherd.mid
Cinema_Anime_TV\The phantom of the opera #2.mid
Cinema_Anime_TV\The phantom of the opera.mid
Cinema_Anime_TV\This Fffire.mid
Cinema_Anime_TV\Twisted nerve.mid
Cinema_Anime_TV\Una mattina.mid
Cinema_Anime_TV\Unravel.mid
Cinema_Anime_TV\Unwelcome school.mid
Cinema_Anime_TV\We are number one.mid
Cinema_Anime_TV\We both reached fo the gun #2.mid
Cinema_Anime_TV\We both reached for the gun.mid
Cinema_Anime_TV\When you're good to mama.mid
Cinema_Anime_TV\Where is my mind.mid
Cinema_Anime_TV\Woo-hoo.mid
Cinema_Anime_TV\Yakko's world.mid
Cinema_Anime_TV\Yokoku.mid
Cinema_Anime_TV\You never can tell.mid
Cinema_Anime_TV\You'll be okay.mid
Cinema_Anime_TV\You're the best around.mid
Cinema_Anime_TV\You've got a friend in me.mid
Cinema_Anime_TV\Your idol.mid
Cinema_Anime_TV\Your new home.mid
Cinema_Anime_TV\Бандито #2.mid
Cinema_Anime_TV\Бандито.mid
Cinema_Anime_TV\Братья Пилоты #2.mid
Cinema_Anime_TV\Братья Пилоты.mid
Cinema_Anime_TV\Бригада.mid
Cinema_Anime_TV\Бумер.mid
Cinema_Anime_TV\В краю магнолий.mid
Cinema_Anime_TV\В синем море,в белой пене.mid
Cinema_Anime_TV\Ваше благородие, госпожа Удача.mid
Cinema_Anime_TV\Все хорошо, Прекрасная Маркиза.mid
Cinema_Anime_TV\Деревня дураков.mid
Cinema_Anime_TV\Завтра грабим короля.mid
Cinema_Anime_TV\Кин-дза-дза.mid
Cinema_Anime_TV\Колыбельная медведицы.mid
Cinema_Anime_TV\Кто первый богатырь на Руси.mid
Cinema_Anime_TV\Мой ласковый и нежный зверь.mid
Cinema_Anime_TV\Надежда.mid
Cinema_Anime_TV\Ночной дозор.mid
Cinema_Anime_TV\Ну погоди.mid
Cinema_Anime_TV\О мальчике Бобби.mid
Cinema_Anime_TV\Облака - белогривые лошадки.mid
Cinema_Anime_TV\Остров невезения.mid
Cinema_Anime_TV\Ох, рано встает охрана.mid
Cinema_Anime_TV\Падал прошлогодний снег (финальная тема).mid
Cinema_Anime_TV\Первым делом - самолеты.mid
Cinema_Anime_TV\Песенка о вреде курения.mid
Cinema_Anime_TV\Песня агента.mid
Cinema_Anime_TV\Песня атаманши.mid
Cinema_Anime_TV\Песня Василисы.mid
Cinema_Anime_TV\Песня Гениального Сыщика.mid
Cinema_Anime_TV\Песня капитана Врунгеля.mid
Cinema_Anime_TV\Песня о медведях.mid
Cinema_Anime_TV\Планета Шелезяка.mid
Cinema_Anime_TV\Постой, паровоз, не стучите колеса.mid
Cinema_Anime_TV\Поход.mid
Cinema_Anime_TV\Прекрасное далёко.mid
Cinema_Anime_TV\Про зайцев.mid
Cinema_Anime_TV\Проснись и пой.mid
Cinema_Anime_TV\Разговор со счастьем.mid
Cinema_Anime_TV\С чего начинается родина.mid
Cinema_Anime_TV\Султан.mid
Cinema_Anime_TV\Тёмная ночь.mid
Cinema_Anime_TV\Тайна Третьей Планеты.mid
Cinema_Anime_TV\Тема битвы.mid
Cinema_Anime_TV\Тема Цирка.mid
Cinema_Anime_TV\Тихий огонёк.mid
Cinema_Anime_TV\Три белых коня.mid
Cinema_Anime_TV\У природы нет плохой погоды.mid
Cinema_Anime_TV\Уно - Моменто.mid
Cinema_Anime_TV\Черное-белое.mid
Cinema_Anime_TV\Что такое С-О-С.mid
Cinema_Anime_TV\Я спросил у ясеня.mid
Classical_&_New_Year\Air.mid
Classical_&_New_Year\All i want for christmas.mid
Classical_&_New_Year\Besame mucho.mid
Classical_&_New_Year\Bolero.mid
Classical_&_New_Year\Canon.MID
Classical_&_New_Year\Cello Suite No. 1 in G Major, BWV 1007.mid
Classical_&_New_Year\Debussy Deux №1.mid
Classical_&_New_Year\Dies iræ 2b.mid
Classical_&_New_Year\Dis moi Lune.mid
Classical_&_New_Year\Eine kleine nachtmusik K. 525 1. Allegro.mid
Classical_&_New_Year\God rest ye merry gentlemen #2.mid
Classical_&_New_Year\God rest ye merry gentlemen.mid
Classical_&_New_Year\Grave march.mid
Classical_&_New_Year\Hungarian dance.mid
Classical_&_New_Year\Jesus bleibet meine Freude.mid
Classical_&_New_Year\Jew on Christmas.mid
Classical_&_New_Year\Jingle bells.mid
Classical_&_New_Year\La petite fille de la mer.mid
Classical_&_New_Year\Lacrimosa.mid
Classical_&_New_Year\Last christmas.mid
Classical_&_New_Year\Let it snow.mid
Classical_&_New_Year\Lohengrin, prelude to act 3.mid
Classical_&_New_Year\Love is blue.mid
Classical_&_New_Year\Mahler symphony No3.mid
Classical_&_New_Year\Minuet.mid
Classical_&_New_Year\Nocturne in E Flat Opus 9 No2.mid
Classical_&_New_Year\Nocturne in F sharp major Op. 15 No2.mid
Classical_&_New_Year\Nocturne No9 Op.32 No1 in B major.mid
Classical_&_New_Year\Nocturnes, Op.9 No1 in B-flat Minor.mid
Classical_&_New_Year\Ode to Joy.mid
Classical_&_New_Year\Rain.mid
Classical_&_New_Year\Sonata No8 in C Minor, Op. 13 Pathetique.mid
Classical_&_New_Year\Spring Waltz.mid
Classical_&_New_Year\Swan lake finalle.mid
Classical_&_New_Year\Swan lake valse.mid
Classical_&_New_Year\Symphony No.9 From new world.mid
Classical_&_New_Year\The Second Waltz.mid
Classical_&_New_Year\Waltz b minor.mid
Classical_&_New_Year\Waltz in C sharp minor 64 No2.mid
Classical_&_New_Year\Waltz No2 in B Minor.mid
Classical_&_New_Year\Waltz.mid
Classical_&_New_Year\Wedding march #2.mid
Classical_&_New_Year\Wedding march.mid
Classical_&_New_Year\Полёт шмеля.mid
Classical_&_New_Year\Танец рыцарей.mid
Classical_&_New_Year\Танец сахарной феи.mid
Classical_&_New_Year\Трепак.mid
Classic_Rock_Metal\99 luftballons #2.mid
Classic_Rock_Metal\99 Luftballons.mid
Classic_Rock_Metal\Another brick in the wall.mid
Classic_Rock_Metal\Back in black.mid
Classic_Rock_Metal\Bad to the bone.mid
Classic_Rock_Metal\Black hole sun.mid
Classic_Rock_Metal\Bodies.mid
Classic_Rock_Metal\Bohemian rhapsody.mid
Classic_Rock_Metal\Bring me to life.mid
Classic_Rock_Metal\Can't stop.mid
Classic_Rock_Metal\Carry on my wayward son.mid
Classic_Rock_Metal\Come as you are.mid
Classic_Rock_Metal\Do the evolution.mid
Classic_Rock_Metal\Down under #2.mid
Classic_Rock_Metal\Down under.mid
Classic_Rock_Metal\Dream on.mid
Classic_Rock_Metal\Engel.mid
Classic_Rock_Metal\Englishman in New York.MID
Classic_Rock_Metal\Enter Sandman.mid
Classic_Rock_Metal\Every breath you take #2.mid
Classic_Rock_Metal\Every breath you take.mid
Classic_Rock_Metal\Everybody wants to rule the world.mid
Classic_Rock_Metal\Exit music.mid
Classic_Rock_Metal\Faint.mid
Classic_Rock_Metal\Fell in love with a girl.mid
Classic_Rock_Metal\For whom the bell tolls.mid
Classic_Rock_Metal\Fortunate son.mid
Classic_Rock_Metal\Free bird.mid
Classic_Rock_Metal\Gay bar.mid
Classic_Rock_Metal\Here comes the Sun.mid
Classic_Rock_Metal\Hotel California.mid
Classic_Rock_Metal\Humanity #2.mid
Classic_Rock_Metal\Humanity.mid
Classic_Rock_Metal\I hate everything about you.mid
Classic_Rock_Metal\In the end.mid
Classic_Rock_Metal\It's my life.mid
Classic_Rock_Metal\Karma police.mid
Classic_Rock_Metal\La bamba.mid
Classic_Rock_Metal\Lemon tree.mid
Classic_Rock_Metal\Let down.mid
Classic_Rock_Metal\Livin' on a prayer.mid
Classic_Rock_Metal\Lucky.mid
Classic_Rock_Metal\Man of war.mid
Classic_Rock_Metal\Master of puppets.mid
Classic_Rock_Metal\Monster.mid
Classic_Rock_Metal\My iron lung.mid
Classic_Rock_Metal\Night witches.mid
Classic_Rock_Metal\Numb.mid
Classic_Rock_Metal\Nur getraeumt.mid
Classic_Rock_Metal\Omen.mid
Classic_Rock_Metal\One last breath.mid
Classic_Rock_Metal\Paint It black.mid
Classic_Rock_Metal\Paralyzer .MID
Classic_Rock_Metal\Paranoid android.mid
Classic_Rock_Metal\Paranoid.mid
Classic_Rock_Metal\Primo Victoria.mid
Classic_Rock_Metal\Rorkes drift.mid
Classic_Rock_Metal\Roundabout.mid
Classic_Rock_Metal\Run through the jungle.MID
Classic_Rock_Metal\Say it.mid
Classic_Rock_Metal\Seven nation army.mid
Classic_Rock_Metal\Shut your mouth.mid
Classic_Rock_Metal\Smells like teen spirit.mid
Classic_Rock_Metal\Smoke on the water.mid
Classic_Rock_Metal\Sonne.mid
Classic_Rock_Metal\Starman.mid
Classic_Rock_Metal\Still loving you.mid
Classic_Rock_Metal\Sultans of swing.mid
Classic_Rock_Metal\Surfin bird.mid
Classic_Rock_Metal\Teenagers.mid
Classic_Rock_Metal\Ten o'clock postman.mid
Classic_Rock_Metal\The chain.mid
Classic_Rock_Metal\The house of the rising Sun #2.mid
Classic_Rock_Metal\The house of the rising sun.mid
Classic_Rock_Metal\The man who solds the world.mid
Classic_Rock_Metal\The only.mid
Classic_Rock_Metal\Thunderstruck.mid
Classic_Rock_Metal\Voodo people.mid
Classic_Rock_Metal\Warcry of Salieri.mid
Classic_Rock_Metal\Welcome to the Black Parade.mid
Classic_Rock_Metal\What i've done.mid
Classic_Rock_Metal\White death.mid
Classic_Rock_Metal\Who can it be now.mid
Classic_Rock_Metal\You're gonna go far kid.mid
Dreams_Memes_Trash\100 Years.mid
Dreams_Memes_Trash\1000 doors.mid
Dreams_Memes_Trash\Aishu no karamatsuba yashi.mid
Dreams_Memes_Trash\Alberto balsalm.mid
Dreams_Memes_Trash\AMONG US DRIP.mid
Dreams_Memes_Trash\BL studio loop.mid
Dreams_Memes_Trash\Chicken dance.mid
Dreams_Memes_Trash\Chipi chipi chapa chapa.mid
Dreams_Memes_Trash\Close eyes.mid
Dreams_Memes_Trash\Cool vibes #2.mid
Dreams_Memes_Trash\Cool vibes.mid
Dreams_Memes_Trash\Die in a fire.mid
Dreams_Memes_Trash\Discord call.mid
Dreams_Memes_Trash\Discord.mid
Dreams_Memes_Trash\Drunk.mid
Dreams_Memes_Trash\El beeper funk.mid
Dreams_Memes_Trash\Entry of the gladiators.mid
Dreams_Memes_Trash\Girl hell 1999.mid
Dreams_Memes_Trash\Hatachi no Koi.mid
Dreams_Memes_Trash\Hello.mid
Dreams_Memes_Trash\I kiss your lips.mid
Dreams_Memes_Trash\It's not like i like you.mid
Dreams_Memes_Trash\Kerosene.mid
Dreams_Memes_Trash\Life letters.mid
Dreams_Memes_Trash\Local forecast.mid
Dreams_Memes_Trash\Meatball parade.mid
Dreams_Memes_Trash\Monitoring.mid
Dreams_Memes_Trash\My ordinary life.mid
Dreams_Memes_Trash\No mercy.mid
Dreams_Memes_Trash\Nokia.mid
Dreams_Memes_Trash\Nyan cat.mid
Dreams_Memes_Trash\Ochame kinou.mid
Dreams_Memes_Trash\PoPiPo.mid
Dreams_Memes_Trash\Schnappi.mid
Dreams_Memes_Trash\Skype call.mid
Dreams_Memes_Trash\Snowfall.mid
Dreams_Memes_Trash\Stronger than you.mid
Dreams_Memes_Trash\The fine print.mid
Dreams_Memes_Trash\The human shields.mid
Dreams_Memes_Trash\The perfect girl.mid
Dreams_Memes_Trash\Triple baka #2.mid
Dreams_Memes_Trash\Triple baka.mid
Dreams_Memes_Trash\Yamaguchi.mid
Dreams_Memes_Trash\Гимн НаноТрейзен.mid
Dreams_Memes_Trash\Гимн Синди.mid
Dreams_Memes_Trash\Мечты Blesstar.mid
Dreams_Memes_Trash\Мечты Куллер.mid
Dreams_Memes_Trash\Мечты Моримото.mid
Dreams_Memes_Trash\Мечты Саспенс.mid
Dreams_Memes_Trash\Мечты Сладкоежки.mid
Dreams_Memes_Trash\Мечты Спектра-71.mid
Dreams_Memes_Trash\Мечты Степчина.mid
Dreams_Memes_Trash\Мечты Такомур.mid
Dreams_Memes_Trash\Мечты Хиппель.mid
Dreams_Memes_Trash\РАФФАЕЛО.mid
Dreams_Memes_Trash\Сок 'Я'.mid
Dreams_Memes_Trash\Судно.mid
Folk_Anthems_Reggae_Tango\Angel.mid
Folk_Anthems_Reggae_Tango\Baby i love your way.mid
Folk_Anthems_Reggae_Tango\Bad boys.mid
Folk_Anthems_Reggae_Tango\Because i got high.mid
Folk_Anthems_Reggae_Tango\Bella Ciao.mid
Folk_Anthems_Reggae_Tango\Caravan.mid
Folk_Anthems_Reggae_Tango\Colonel Bogey.mid
Folk_Anthems_Reggae_Tango\Could you be loved.mid
Folk_Anthems_Reggae_Tango\Der offene aufmarsch.mid
Folk_Anthems_Reggae_Tango\England.mid
Folk_Anthems_Reggae_Tango\Germany.mid
Folk_Anthems_Reggae_Tango\Hava Nagila.mid
Folk_Anthems_Reggae_Tango\Hava shalom.mid
Folk_Anthems_Reggae_Tango\Hevenu shalom.mid
Folk_Anthems_Reggae_Tango\Its a long long way to Tipperary.mid
Folk_Anthems_Reggae_Tango\Jalousie.mid
Folk_Anthems_Reggae_Tango\La cumparsita.mid
Folk_Anthems_Reggae_Tango\La Verdine.mid
Folk_Anthems_Reggae_Tango\Lambada.mid
Folk_Anthems_Reggae_Tango\Levan polkka.mid
Folk_Anthems_Reggae_Tango\Mambo Italiano.mid
Folk_Anthems_Reggae_Tango\Mambo-Mambo.mid
Folk_Anthems_Reggae_Tango\Mazel tov.mid
Folk_Anthems_Reggae_Tango\Niet Molotoff.midi
Folk_Anthems_Reggae_Tango\Non je ne regrette rien.mid
Folk_Anthems_Reggae_Tango\O Canada.MID
Folk_Anthems_Reggae_Tango\Red red wine.mid
Folk_Anthems_Reggae_Tango\Red sun in the sky #2.mid
Folk_Anthems_Reggae_Tango\Red sun in the sky.mid
Folk_Anthems_Reggae_Tango\Ring a ring o roses.mid
Folk_Anthems_Reggae_Tango\Sakkijarven polkka.mid
Folk_Anthems_Reggae_Tango\Sambra.mid
Folk_Anthems_Reggae_Tango\Scotland the brave.mid
Folk_Anthems_Reggae_Tango\Seiben tage lang.mid
Folk_Anthems_Reggae_Tango\Serbia strong.mid
Folk_Anthems_Reggae_Tango\Shuckin the corn.mid
Folk_Anthems_Reggae_Tango\Smooth.mid
Folk_Anthems_Reggae_Tango\Soldiers march.mid
Folk_Anthems_Reggae_Tango\Spanish flea.mid
Folk_Anthems_Reggae_Tango\Sunshine reggae.mid
Folk_Anthems_Reggae_Tango\Take me home, country road.mid
Folk_Anthems_Reggae_Tango\Tango  #4.mid
Folk_Anthems_Reggae_Tango\Tango #1.mid
Folk_Anthems_Reggae_Tango\Tango #2.mid
Folk_Anthems_Reggae_Tango\Tango #3.mid
Folk_Anthems_Reggae_Tango\Tangos caminito.mid
Folk_Anthems_Reggae_Tango\The battle hymn of the republic.mid
Folk_Anthems_Reggae_Tango\The girl from Ipanema.mid
Folk_Anthems_Reggae_Tango\The star spangled banner #2.mid
Folk_Anthems_Reggae_Tango\The star spangled banner.mid
Folk_Anthems_Reggae_Tango\Three little birds.mid
Folk_Anthems_Reggae_Tango\Union Dixie.mid
Folk_Anthems_Reggae_Tango\When Johnny comes marching home.mid
Folk_Anthems_Reggae_Tango\You don't love me (no no no).mid
Folk_Anthems_Reggae_Tango\You gotta move.mid
Folk_Anthems_Reggae_Tango\Zundoko-bushi.mid
Folk_Anthems_Reggae_Tango\Боже Царя храни #2.mid
Folk_Anthems_Reggae_Tango\Боже Царя храни.mid
Folk_Anthems_Reggae_Tango\Гимн РФ 93.mid
Folk_Anthems_Reggae_Tango\Дорогой длинною.mid
Folk_Anthems_Reggae_Tango\Идёт солдат.mid
Folk_Anthems_Reggae_Tango\Калинка.mid
Folk_Anthems_Reggae_Tango\Красная Армия всех сильней.mid
Folk_Anthems_Reggae_Tango\Крейсер 'Аврора'.mid
Folk_Anthems_Reggae_Tango\Молдованка.mid
Folk_Anthems_Reggae_Tango\Нам нужна одна победа.mid
Folk_Anthems_Reggae_Tango\Последний бой.mid
Folk_Anthems_Reggae_Tango\Синий платочек.mid
Folk_Anthems_Reggae_Tango\Славься Русь.mid
Folk_Anthems_Reggae_Tango\Славянка.mid
Folk_Anthems_Reggae_Tango\Юный октябрь .mid
Jazz_Swing_Retro\A kiss to build a dream on.mid
Jazz_Swing_Retro\A little dream of me.mid
Jazz_Swing_Retro\A Smile and a Ribbon.mid
Jazz_Swing_Retro\Ain't Misbehavin'.mid
Jazz_Swing_Retro\All night.mid
Jazz_Swing_Retro\All you are going to want to do is get back there.mid
Jazz_Swing_Retro\Alligator crawl.mid
Jazz_Swing_Retro\Angela.mid
Jazz_Swing_Retro\Atom bomb baby.mid
Jazz_Swing_Retro\Bang bang.mid
Jazz_Swing_Retro\Beyond the sea.mid
Jazz_Swing_Retro\Big Iron.mid
Jazz_Swing_Retro\Big spender.mid
Jazz_Swing_Retro\Black betty.mid
Jazz_Swing_Retro\Blue Moon.mid
Jazz_Swing_Retro\Blue suede shoes.mid
Jazz_Swing_Retro\Boogie man.mid
Jazz_Swing_Retro\Booty swing .mid
Jazz_Swing_Retro\Catgroove.mid
Jazz_Swing_Retro\Chambermaid swing.mid
Jazz_Swing_Retro\Cheek to cheek.mid
Jazz_Swing_Retro\Close to you.mid
Jazz_Swing_Retro\Coin operated boy.mid
Jazz_Swing_Retro\Cry me a river.mid
Jazz_Swing_Retro\Dear hearts and gentle people.mid
Jazz_Swing_Retro\Dizzy fingers.mid
Jazz_Swing_Retro\Don't let the stars get in you eyes.mid
Jazz_Swing_Retro\Dramophone.mid
Jazz_Swing_Retro\Earth angel.mid
Jazz_Swing_Retro\Feeling good.mid
Jazz_Swing_Retro\Five hundred miles.mid
Jazz_Swing_Retro\Fly me to the Moon #2.mid
Jazz_Swing_Retro\Fly me to the moon.mid
Jazz_Swing_Retro\Glitz at the ritz.mid
Jazz_Swing_Retro\Heartaches by the number.mid
Jazz_Swing_Retro\Heartaches.mid
Jazz_Swing_Retro\Hey pachuco.mid
Jazz_Swing_Retro\Hit the road Jack.mid
Jazz_Swing_Retro\Hurt.mid
Jazz_Swing_Retro\I don't want to set the world on fire.mid
Jazz_Swing_Retro\I'm always chaising rainbow.mid
Jazz_Swing_Retro\In a sentimental mood.mid
Jazz_Swing_Retro\Into each life some rains must fall.mid
Jazz_Swing_Retro\It don't mean a thing.mid
Jazz_Swing_Retro\It's just a burning memory.mid
Jazz_Swing_Retro\Jazz around midnight.mid
Jazz_Swing_Retro\Jingle jangle jingle.mid
Jazz_Swing_Retro\Just the two of us.mid
Jazz_Swing_Retro\Kitten on the keys.mid
Jazz_Swing_Retro\La vie en rose.mid
Jazz_Swing_Retro\Life could be dream.mid
Jazz_Swing_Retro\LiraInfluencia do jazz.mid
Jazz_Swing_Retro\Lone digger.mid
Jazz_Swing_Retro\Lost in the rhythm.mid
Jazz_Swing_Retro\Love and marrige.mid
Jazz_Swing_Retro\Magic moments.mid
Jazz_Swing_Retro\Mein herr.mid
Jazz_Swing_Retro\Mr.Sandman.mid
Jazz_Swing_Retro\My way.mid
Jazz_Swing_Retro\NewYork.mid
Jazz_Swing_Retro\Olive Branch.mid
Jazz_Swing_Retro\Only you.mid
Jazz_Swing_Retro\Peeping Tom.mid
Jazz_Swing_Retro\Pistol packing mama.mid
Jazz_Swing_Retro\Put on your sunday clothe.mid
Jazz_Swing_Retro\Raindrops keep falling on my head.mid
Jazz_Swing_Retro\Rock around the clock.mid
Jazz_Swing_Retro\Rock it for me.mid
Jazz_Swing_Retro\Run rabbit run.mid
Jazz_Swing_Retro\Russian.mid
Jazz_Swing_Retro\Sixteen tons.mid
Jazz_Swing_Retro\Sixty minute man.mid
Jazz_Swing_Retro\Slowly jazz.mid
Jazz_Swing_Retro\Softly as in a morning sunrise.mid
Jazz_Swing_Retro\Some enchanted evening #2.mid
Jazz_Swing_Retro\Some enchanted evening.mid
Jazz_Swing_Retro\Something stupid.mid
Jazz_Swing_Retro\Southern nights.mid
Jazz_Swing_Retro\That's life.mid
Jazz_Swing_Retro\The end of the world.mid
Jazz_Swing_Retro\The very thought of you.mid
Jazz_Swing_Retro\The wanderer.mid
Jazz_Swing_Retro\Two of kind.mid
Jazz_Swing_Retro\Unfinished business.mid
Jazz_Swing_Retro\Vipers drag.mid
Jazz_Swing_Retro\Wash my hands.mid
Jazz_Swing_Retro\Way back home.mid
Jazz_Swing_Retro\What you won't do for love.mid
Jazz_Swing_Retro\Who gonna shack it night along.mid
Jazz_Swing_Retro\Why don't you do it right.mid
Jazz_Swing_Retro\Will meet again.mid
Jazz_Swing_Retro\Wonderful world.mid
Jazz_Swing_Retro\Young and foolish.mid
Pop_Music_International\505.mid
Pop_Music_International\A thousand miles.mid
Pop_Music_International\ABCDFU.mid
Pop_Music_International\Abracadabra.mid
Pop_Music_International\Accidentally in love.mid
Pop_Music_International\Adult education.mid
Pop_Music_International\Adventure of a Lifetime.mid
Pop_Music_International\After dark.mid
Pop_Music_International\Alright.mid
Pop_Music_International\American idiot.mid
Pop_Music_International\American pie.mid
Pop_Music_International\Angel of the morning #2.mid
Pop_Music_International\Angel of the morning.mid
Pop_Music_International\Animals .mid
Pop_Music_International\Another day In paradise.mid
Pop_Music_International\Another love.mid
Pop_Music_International\Applause.mid
Pop_Music_International\Around the world.mid
Pop_Music_International\As it was.mid
Pop_Music_International\As the world caves in.mid
Pop_Music_International\Baby one more time.mid
Pop_Music_International\Bad girls.mid
Pop_Music_International\Bailando.mid
Pop_Music_International\Ballin.mid
Pop_Music_International\Bambalailo.mid
Pop_Music_International\Barbie girl.mid
Pop_Music_International\Beach parade.mid
Pop_Music_International\Beautiful life.mid
Pop_Music_International\Better off alone.mid
Pop_Music_International\Big and chunky.mid
Pop_Music_International\Big city life.mid
Pop_Music_International\Big in Japan.mid
Pop_Music_International\Bimbo doll.mid
Pop_Music_International\Bitter sweet symphony.mid
Pop_Music_International\Black black heart.mid
Pop_Music_International\Blue monday.mid
Pop_Music_International\Boom-Boom-Boom.mid
Pop_Music_International\Breakfast in America.mid
Pop_Music_International\Brother Louie.mid
Pop_Music_International\Build a bitch.mid
Pop_Music_International\Cake by the ocean.mid
Pop_Music_International\California dreaming.mid
Pop_Music_International\Call me maybe.mid
Pop_Music_International\Call me.mid
Pop_Music_International\Camel by camel.mid
Pop_Music_International\Can't hold us.mid
Pop_Music_International\Caramell dansen.mid
Pop_Music_International\Careless whisper.mid
Pop_Music_International\Celebrate the love.mid
Pop_Music_International\Charlie's Inferno #2.mid
Pop_Music_International\Charlie's inferno.mid
Pop_Music_International\Cheri lady #2.mid
Pop_Music_International\Cheri lady.mid
Pop_Music_International\Children #2.mid
Pop_Music_International\Children.mid
Pop_Music_International\Cigarettes out the Window.mid
Pop_Music_International\Circle in the Sand.mid
Pop_Music_International\Coca Jambo.mid
Pop_Music_International\Come a little bit closer.mid
Pop_Music_International\Come and get your love.mid
Pop_Music_International\Cooler than me.mid
Pop_Music_International\Creep.mid
Pop_Music_International\Crimewave.mid
Pop_Music_International\Criminal.mid
Pop_Music_International\Crucified.mid
Pop_Music_International\Cupid.mid
Pop_Music_International\D.I.S.C.O.mid
Pop_Music_International\Dancin'.mid
Pop_Music_International\Dancin.MID
Pop_Music_International\Dancing in the Moon light.mid
Pop_Music_International\Denise.mid
Pop_Music_International\Destination Calabria.mid
Pop_Music_International\Die for you.mid
Pop_Music_International\Do ya think i'm sexy.mid
Pop_Music_International\Don't cry tonight.mid
Pop_Music_International\Don't stop me now.mid
Pop_Music_International\Don't wanna fall in love.mid
Pop_Music_International\Don't worry be happy.mid
Pop_Music_International\Du bist gut genug #2.mid
Pop_Music_International\Du bist gut genug.mid
Pop_Music_International\Dumb dumb.mid
Pop_Music_International\Egoist #2.mid
Pop_Music_International\Egoist.mid
Pop_Music_International\Eleanor Rigby.mid
Pop_Music_International\Electric avenue.mid
Pop_Music_International\Empty.mid
Pop_Music_International\Escape (The Pina Colada song).mid
Pop_Music_International\Estrelar.mid
Pop_Music_International\ET.mid
Pop_Music_International\Every time we touch.mid
Pop_Music_International\Everything at once #2.mid
Pop_Music_International\Everything at once.mid
Pop_Music_International\Everything in the right place.mid
Pop_Music_International\Everything she wants.MID
Pop_Music_International\Fairytale.mid
Pop_Music_International\Fergie glamorous.mid
Pop_Music_International\Finale coutdown.mid
Pop_Music_International\Firework.mid
Pop_Music_International\Fliday chinatown.mid
Pop_Music_International\Forget me nots.mid
Pop_Music_International\From the start.mid
Pop_Music_International\Fun tonight.mid
Pop_Music_International\Funkytown.mid
Pop_Music_International\Gangstas Paradise.mid
Pop_Music_International\Gas gas gas.mid
Pop_Music_International\Get around town.mid
Pop_Music_International\Get low.mid
Pop_Music_International\Get lucky.mid
Pop_Music_International\Gimme.mid
Pop_Music_International\Giorgio.mid
Pop_Music_International\Glamorous.mid
Pop_Music_International\Go west #2.mid
Pop_Music_International\Go west.MID
Pop_Music_International\Golden brown #2.mid
Pop_Music_International\Golden brown.mid
Pop_Music_International\Guten tag liebes glück.mid
Pop_Music_International\Gypsy woman.mid
Pop_Music_International\Hafanana.mid
Pop_Music_International\Happiest year.mid
Pop_Music_International\Headlock #2.mid
Pop_Music_International\Headlock.mid
Pop_Music_International\Heaven knows i'm miserable now.mid
Pop_Music_International\Hooked on a feeling.mid
Pop_Music_International\Hot stuff.mid
Pop_Music_International\HotNCold.mid
Pop_Music_International\Hurt.mid
Pop_Music_International\I can't stop the loneliness.mid
Pop_Music_International\I just died in your arms.mid
Pop_Music_International\I kissed a girl.mid
Pop_Music_International\I like the way kiss me.mid
Pop_Music_International\I love it.mid
Pop_Music_International\I love you so.mid
Pop_Music_International\I need some sleep.mid
Pop_Music_International\I want it that way.mid
Pop_Music_International\I want to know what love is.mid
Pop_Music_International\I will survive #2.mid
Pop_Music_International\I will survive.mid
Pop_Music_International\I'm a believer.mid
Pop_Music_International\I'm just a kid.mid
Pop_Music_International\In and out of love #2.mid
Pop_Music_International\In and out of love.mid
Pop_Music_International\In da club.mid
Pop_Music_International\In the navy.mid
Pop_Music_International\In the summertime.mid
Pop_Music_International\Industry baby.mid
Pop_Music_International\Instant crush.mid
Pop_Music_International\It doesn't have to be this way.mid
Pop_Music_International\It was a good day.mid
Pop_Music_International\Jen ai marre.mid
Pop_Music_International\Jocelyn flores.mid
Pop_Music_International\Jodellavitanonhocapitouncazzo.mid
Pop_Music_International\Kids.mid
Pop_Music_International\Knew you were trouble .mid
Pop_Music_International\Lady.mid
Pop_Music_International\Lay all your love on me.mid
Pop_Music_International\Leni (vs GoodBooks).mid
Pop_Music_International\Let it happen.mid
Pop_Music_International\Let's go.mid
Pop_Music_International\Let's groove.mid
Pop_Music_International\Lets go to bed.mid
Pop_Music_International\Life goes on.mid
Pop_Music_International\Lily was here #2.mid
Pop_Music_International\Lily was here.mid
Pop_Music_International\Little dark age.mid
Pop_Music_International\Livin la vida loca.mid
Pop_Music_International\Lollipop.mid
Pop_Music_International\Lose yourself.mid
Pop_Music_International\Love is a long road.mid
Pop_Music_International\Lovers on the sun.mid
Pop_Music_International\Macarena.mid
Pop_Music_International\Magic spells.mid
Pop_Music_International\Major Tom.mid
Pop_Music_International\Make your own kind of music.mid
Pop_Music_International\Mamma Maria.MID
Pop_Music_International\Maniac #2.mid
Pop_Music_International\Maniac.mid
Pop_Music_International\Maria Magdalena.mid
Pop_Music_International\Maria.mid
Pop_Music_International\Me and the birds.mid
Pop_Music_International\Me gustas tu.mid
Pop_Music_International\Meet me halfway.mid
Pop_Music_International\Messages from the stars #2.mid
Pop_Music_International\Messages from the stars.mid
Pop_Music_International\Midnight city.mid
Pop_Music_International\Military fashion showe.mid
Pop_Music_International\Miss Jackson.mid
Pop_Music_International\Miss the Rage.mid
Pop_Music_International\Moi lolita.mid
Pop_Music_International\Moonlighting.mid
Pop_Music_International\More then a filling.mid
Pop_Music_International\Moves like jagger.mid
Pop_Music_International\Mr.Blue Sky.mid
Pop_Music_International\Mr.Bombastic.mid
Pop_Music_International\Mr.Saxobeat .mid
Pop_Music_International\Mr.Vain.mid
Pop_Music_International\Music sounds better with you.mid
Pop_Music_International\Natural.mid
Pop_Music_International\Never gonna give you up.mid
Pop_Music_International\New jeans.mid
Pop_Music_International\New sensation.mid
Pop_Music_International\No Surprises #2.mid
Pop_Music_International\No surprises.mid
Pop_Music_International\Nothing breaks like a heart.mid
Pop_Music_International\On melancholy hill.mid
Pop_Music_International\One thing #2.mid
Pop_Music_International\One thing.mid
Pop_Music_International\One way or another.mid
Pop_Music_International\One.mid
Pop_Music_International\Only girl.mid
Pop_Music_International\Only time will tell.mid
Pop_Music_International\Out of touch.mid
Pop_Music_International\Papaoutai.mid
Pop_Music_International\Piano man.mid
Pop_Music_International\Play that funky music.mid
Pop_Music_International\Playing dead.mid
Pop_Music_International\Pompeii #2.mid
Pop_Music_International\Pompeii.mid
Pop_Music_International\Pretty woman.mid
Pop_Music_International\Promises, promises.mid
Pop_Music_International\Psycho killer.mid
Pop_Music_International\Pumped up kicks.mid
Pop_Music_International\Pure shores.mid
Pop_Music_International\Push it to the limit.mid
Pop_Music_International\Radio.mid
Pop_Music_International\Relaxed scene.mid
Pop_Music_International\Replay.mid
Pop_Music_International\Revenge.mid
Pop_Music_International\Rhythm is a dancer.mid
Pop_Music_International\Ride It.mid
Pop_Music_International\Ridin dirty.mid
Pop_Music_International\Riptide.mid
Pop_Music_International\Roar.mid
Pop_Music_International\Run away baby.mid
Pop_Music_International\Running in 90s.mid
Pop_Music_International\Running up that hill.mid
Pop_Music_International\Sadness #2.mid
Pop_Music_International\Sadness.mid
Pop_Music_International\Safe and sound.mid
Pop_Music_International\Sailor song.mid
Pop_Music_International\Save your kisses for me.mid
Pop_Music_International\Sayonara.mid
Pop_Music_International\Scatman.MID
Pop_Music_International\Scatmans world.mid
Pop_Music_International\Send me an angel.mid
Pop_Music_International\September.mid
Pop_Music_International\Sexy eyes.mid
Pop_Music_International\Shake it off.mid
Pop_Music_International\Shape of my heart.mid
Pop_Music_International\Short dick man.mid
Pop_Music_International\Sinking town #2.mid
Pop_Music_International\Sinking town.mid
Pop_Music_International\Six undeground.mid
Pop_Music_International\Skyfall.mid
Pop_Music_International\Small town boys.mid
Pop_Music_International\Smalltown boys #2.mid
Pop_Music_International\Smooth operator #2.mid
Pop_Music_International\Smooth operator.mid
Pop_Music_International\So far so good.mid
Pop_Music_International\So klingt liebe.mid
Pop_Music_International\Somebody that i used to know.mid
Pop_Music_International\Somebody to love.mid
Pop_Music_International\Something about us.mid
Pop_Music_International\Somthing got me started.mid
Pop_Music_International\Song 2.mid
Pop_Music_International\Space song.mid
Pop_Music_International\Stan.mid
Pop_Music_International\Stay.mid
Pop_Music_International\Stayin alive.mid
Pop_Music_International\Stereo heart.mid
Pop_Music_International\Still DRE.mid
Pop_Music_International\Stolen dance.mid
Pop_Music_International\Stressed out.mid
Pop_Music_International\Stromae alors on danse.mid
Pop_Music_International\Stumblin' in.mid
Pop_Music_International\Sugar sugar.MID
Pop_Music_International\Sunny.mid
Pop_Music_International\Supergirl #2.mid
Pop_Music_International\Supergirl.mid
Pop_Music_International\Supersonic rocket ship.mid
Pop_Music_International\Sweet dreams.mid
Pop_Music_International\Sweety sweety.mid
Pop_Music_International\Tek it.mid
Pop_Music_International\Tell It to my heart.mid
Pop_Music_International\Thank you.mid
Pop_Music_International\The bidding.mid
Pop_Music_International\The dream.mid
Pop_Music_International\The lost song.mid
Pop_Music_International\The rhythm of the night.mid
Pop_Music_International\The sign.mid
Pop_Music_International\The winner takes it all.mid
Pop_Music_International\They call me Sonic.mid
Pop_Music_International\Tick Tock.mid
Pop_Music_International\Time to say goodbye.mid
Pop_Music_International\Titanic.mid
Pop_Music_International\Titanium.mid
Pop_Music_International\Tom's diner.mid
Pop_Music_International\Tonight.mid
Pop_Music_International\Tous les memes.mid
Pop_Music_International\Twilight.mid
Pop_Music_International\Ulterior motives.mid
Pop_Music_International\Veridis Quo #2.mid
Pop_Music_International\Veridis Quo.mid
Pop_Music_International\Video killed the radio star.mid
Pop_Music_International\Virtual Insanity.mid
Pop_Music_International\Viva la Vida.mid
Pop_Music_International\Wake me up before you go go.mid
Pop_Music_International\Wake me up.mid
Pop_Music_International\Wannabe.mid
Pop_Music_International\Washing machine heart.mid
Pop_Music_International\West end girls.mid
Pop_Music_International\What is love.mid
Pop_Music_International\When we stand together.mid
Pop_Music_International\Wicked game #2.mid
Pop_Music_International\Wicked game.mid
Pop_Music_International\Wish you were here.mid
Pop_Music_International\Wolf in sheeps clothing.mid
Pop_Music_International\Wonderful tonight.mid
Pop_Music_International\Words.mid
Pop_Music_International\World hold on #2.mid
Pop_Music_International\World hold on.mid
Pop_Music_International\Wouldn't it be nice.mid
Pop_Music_International\Write this down.mid
Pop_Music_International\X gona give it to ya.mid
Pop_Music_International\Yeah.mid
Pop_Music_International\You can't touch this.mid
Pop_Music_International\You speen me round.mid
Pop_Music_International\You're my soul.mid
Pop_Music_International\Your lucky day in hell.mid
Pop_Music_International\Your woman.mid
Pop_Music_Russian\Yes future.mid
Pop_Music_Russian\Алиса.mid
Pop_Music_Russian\Альпинист.mid
Pop_Music_Russian\Ариведерчи.mid
Pop_Music_Russian\Арлекино #2.mid
Pop_Music_Russian\Арлекино.mid
Pop_Music_Russian\Батарейка.mid
Pop_Music_Russian\Белая ночь.mid
Pop_Music_Russian\Белые розы.mid
Pop_Music_Russian\Бродяга.mid
Pop_Music_Russian\Букет.mid
Pop_Music_Russian\Вечно молодой.mid
Pop_Music_Russian\Владимирский централ.mid
Pop_Music_Russian\Восточные сказки.mid
Pop_Music_Russian\Всё, что тебя касается.mid
Pop_Music_Russian\Выхода нет.mid
Pop_Music_Russian\Гимнастика.mid
Pop_Music_Russian\Главное.mid
Pop_Music_Russian\Голая.mid
Pop_Music_Russian\Город которого нет.mid
Pop_Music_Russian\Девочка-видение.mid
Pop_Music_Russian\До свидания.mid
Pop_Music_Russian\До скорой встречи.mid
Pop_Music_Russian\Дождь.mid
Pop_Music_Russian\Дорога.mid
Pop_Music_Russian\Ева, я любила.mid
Pop_Music_Russian\Железо поёт.mid
Pop_Music_Russian\Звёздное лето.mid
Pop_Music_Russian\Звёзды нас ждут.mid
Pop_Music_Russian\Как бы всё.mid
Pop_Music_Russian\Как на войне.mid
Pop_Music_Russian\Комарово.mid
Pop_Music_Russian\Косил Ясь конюшину.mid
Pop_Music_Russian\Кто ты.mid
Pop_Music_Russian\Кто.mid
Pop_Music_Russian\Любочка #2.mid
Pop_Music_Russian\Любочка.mid
Pop_Music_Russian\Люди встречаются.mid
Pop_Music_Russian\Мало тебя.mid
Pop_Music_Russian\Мальчик-гей.mid
Pop_Music_Russian\Мама Люба.mid
Pop_Music_Russian\Моё сердце.mid
Pop_Music_Russian\Мой друг.mid
Pop_Music_Russian\Моя любовь.mid
Pop_Music_Russian\Музыка нас связала.mid
Pop_Music_Russian\Мы сидели и курили.mid
Pop_Music_Russian\На белом покрывале января.mid
Pop_Music_Russian\На седьмом этаже.mid
Pop_Music_Russian\Нас не догонят.mid
Pop_Music_Russian\Наше лето.mid
Pop_Music_Russian\Не волнуйтесь, тётя.mid
Pop_Music_Russian\Не танцую.mid
Pop_Music_Russian\Опера#2.mid
Pop_Music_Russian\Отпускаю.mid
Pop_Music_Russian\Поворот.mid
Pop_Music_Russian\Поезд в огне.mid
Pop_Music_Russian\Позови меня с собой.mid
Pop_Music_Russian\Прасковья.mid
Pop_Music_Russian\Привет.mid
Pop_Music_Russian\Прованс.mid
Pop_Music_Russian\Просвистела.mid
Pop_Music_Russian\Прости, прощай, привет.mid
Pop_Music_Russian\Ромашки.mid
Pop_Music_Russian\Снег.mid
Pop_Music_Russian\Солнышко.mid
Pop_Music_Russian\СПИД.mid
Pop_Music_Russian\Тёплые коты.mid
Pop_Music_Russian\Тополиный пух.mid
Pop_Music_Russian\Трава у дома.mid
Pop_Music_Russian\Убили негра.mid
Pop_Music_Russian\Улыбки cфинксов.mid
Pop_Music_Russian\Уматурман.mid
Pop_Music_Russian\Фаина.mid
Pop_Music_Russian\Фантазёр.mid
Pop_Music_Russian\Формалин.mid
Pop_Music_Russian\Хали-гали.mid
Pop_Music_Russian\Хочешь.mid
Pop_Music_Russian\Чёрный кот .mid
Pop_Music_Russian\Человек и кошка.mid
Pop_Music_Russian\Шарманка .mid
Pop_Music_Russian\Эй толстый.mid
Pop_Music_Russian\Я солдат.mid
Pop_Music_Russian\Я сошла с ума.mid
Pop_Music_Russian\Январская вьюга.mid
Russian_Rock_&_Alternative\1100.mid
Russian_Rock_&_Alternative\2000 баксов за сигарету.mid
Russian_Rock_&_Alternative\Алюминиевые огурцы .mid
Russian_Rock_&_Alternative\Андердог.mid
Russian_Rock_&_Alternative\Беспечный ангел.mid
Russian_Rock_&_Alternative\Восьмиклассница.mid
Russian_Rock_&_Alternative\Гибралтар - лабрадор.mid
Russian_Rock_&_Alternative\Группа крови.mid
Russian_Rock_&_Alternative\Два вора и монета.mid
Russian_Rock_&_Alternative\Джокер.mid
Russian_Rock_&_Alternative\Закрой за мной дверь.mid
Russian_Rock_&_Alternative\Звезда по имени Солнце.mid
Russian_Rock_&_Alternative\Капитал.mid
Russian_Rock_&_Alternative\Когда твоя девушка больна.mid
Russian_Rock_&_Alternative\Кончится лето.mid
Russian_Rock_&_Alternative\Кукушка.mid
Russian_Rock_&_Alternative\Мороз по коже.mid
Russian_Rock_&_Alternative\Мы лёд.mid
Russian_Rock_&_Alternative\Орбит без сахара.mid
Russian_Rock_&_Alternative\ПММЛ.mid
Russian_Rock_&_Alternative\Полковнику никто не пишет.mid
Russian_Rock_&_Alternative\Последний герой.mid
Russian_Rock_&_Alternative\Потерянный рай.mid
Russian_Rock_&_Alternative\Прогулки по воде.mid
Russian_Rock_&_Alternative\Романс.mid
Russian_Rock_&_Alternative\Северный ветер.mid
Russian_Rock_&_Alternative\Сентябрь.mid
Russian_Rock_&_Alternative\Скованные одной цепью.mid
Russian_Rock_&_Alternative\Трасса Е-95.mid
Russian_Rock_&_Alternative\Устрой дестрой.mid
Russian_Rock_&_Alternative\Фантом.mid
Russian_Rock_&_Alternative\Я на тебе как на войне.mid
Russian_Rock_&_Alternative\Я хочу быть с тобой.mid
SS14_&_Game_OST\A little heart to heart.mid
SS14_&_Game_OST\A promise from distant days.mid
SS14_&_Game_OST\About her.mid
SS14_&_Game_OST\Absolute territory.mid
SS14_&_Game_OST\Arstotzkan Anthem.mid
SS14_&_Game_OST\Attack of the Killer Queen.mid
SS14_&_Game_OST\Baka mitai.mid
SS14_&_Game_OST\Battle against a true hero.mid
SS14_&_Game_OST\Battle without honor or humanity.mid
SS14_&_Game_OST\Beneath The Mask.mid
SS14_&_Game_OST\BFG Division.mid
SS14_&_Game_OST\Bonetrousle.mid
SS14_&_Game_OST\Boombox.mid
SS14_&_Game_OST\Claw finger.mid
SS14_&_Game_OST\Coalescence.mid
SS14_&_Game_OST\Coconut mail.mid
SS14_&_Game_OST\Color your night.mid
SS14_&_Game_OST\CP Violation.mid
SS14_&_Game_OST\Death by glamour.mid
SS14_&_Game_OST\Detroit become human(главная тема).mid
SS14_&_Game_OST\Dream BBQ.mid
SS14_&_Game_OST\Eirin's clinic that people line up for.mid
SS14_&_Game_OST\Elevator jam.mid
SS14_&_Game_OST\Every light is blinking at once.mid
SS14_&_Game_OST\Everylasting summer.mid
SS14_&_Game_OST\Fairy fountain.mid
SS14_&_Game_OST\Fallen.mid
SS14_&_Game_OST\Farewell to the past.mid
SS14_&_Game_OST\Flip-Flap.mid
SS14_&_Game_OST\Forest maiden.mid
SS14_&_Game_OST\FUNKY MODE.mid
SS14_&_Game_OST\Goat chill.mid
SS14_&_Game_OST\Gourmet race concert.mid
SS14_&_Game_OST\Greateful love.mid
SS14_&_Game_OST\Head revolutionary.mid
SS14_&_Game_OST\Heartache.mid
SS14_&_Game_OST\Help me Erinnnnnn.mid
SS14_&_Game_OST\Henry stickman dance.mid
SS14_&_Game_OST\Hip shop #2.mid
SS14_&_Game_OST\Hip Shop.mid
SS14_&_Game_OST\Ice cream song.mid
SS14_&_Game_OST\In the pines.mid
SS14_&_Game_OST\It has to be this way.mid
SS14_&_Game_OST\It's pizza time.mid
SS14_&_Game_OST\Just asking at day.mid
SS14_&_Game_OST\Just asking at night.mid
SS14_&_Game_OST\Last Surpise.mid
SS14_&_Game_OST\Let's be friends.mid
SS14_&_Game_OST\Little trinketry#2.mid
SS14_&_Game_OST\Little trinketry.mid
SS14_&_Game_OST\Live to forget.mid
SS14_&_Game_OST\Make it bun dem.mid
SS14_&_Game_OST\Mannrobics.mid
SS14_&_Game_OST\Maybe we can win this.mid
SS14_&_Game_OST\Metal сrusher.mid
SS14_&_Game_OST\Meteor.MID
SS14_&_Game_OST\Metro exodus.mid
SS14_&_Game_OST\Miku`s song.mid
SS14_&_Game_OST\Mond, Mond! Ja, Ja!.mid
SS14_&_Game_OST\Nine thou superstars.mid
SS14_&_Game_OST\O cara mia, addio.mid
SS14_&_Game_OST\Pandora palace.mid
SS14_&_Game_OST\Phoron will make us rich.mid
SS14_&_Game_OST\Pizza delux.mid
SS14_&_Game_OST\Pizza theme.mid
SS14_&_Game_OST\Power of NEO.mid
SS14_&_Game_OST\Promise reprise.mid
SS14_&_Game_OST\Queen.mid
SS14_&_Game_OST\Razormind.mid
SS14_&_Game_OST\Resident evil.mid
SS14_&_Game_OST\Right behind you.mid
SS14_&_Game_OST\Rocket jump waltz.mid
SS14_&_Game_OST\Running out.mid
SS14_&_Game_OST\Scarlet forest.mid
SS14_&_Game_OST\Self isolation at night.mid
SS14_&_Game_OST\Shop.mid
SS14_&_Game_OST\Soilder of dance.mid
SS14_&_Game_OST\Song that may play when you fight Sans.mid
SS14_&_Game_OST\Soviet march.mid
SS14_&_Game_OST\Space asshole.mid
SS14_&_Game_OST\Space Station 14 OST.mid
SS14_&_Game_OST\Spider dance.mid
SS14_&_Game_OST\The death that I deservioli.mid
SS14_&_Game_OST\The end.mid
SS14_&_Game_OST\The finale flash of existence.mid
SS14_&_Game_OST\The last of us.mid
SS14_&_Game_OST\The only thing that scares me.mid
SS14_&_Game_OST\The rebel path.mid
SS14_&_Game_OST\The world revolving.mid
SS14_&_Game_OST\The zombie threat.mid
SS14_&_Game_OST\Tin-tin on the moon.mid
SS14_&_Game_OST\Ugh.mid
SS14_&_Game_OST\Upgrade station.mid
SS14_&_Game_OST\Victory theme.mid
SS14_&_Game_OST\Vitality.mid
SS14_&_Game_OST\Want you gone.mid
SS14_&_Game_OST\Welcome to Silent Hill.mid
SS14_&_Game_OST\What was lost.mid
SS14_&_Game_OST\Whirling in rags, 8AM.mid
SS14_&_Game_OST\Xenophobia.mid
Гимн Империи.mid
Гимн Республики Элизиум.mid
Гимн Свободных Планет.mid
Гимн СССП.mid
Гимн ТСФ.mid
Спонсированно Мисс Хаус.mid
"""

# 2. Вставляешь сюда свою мету
meta_list_raw = r"""
﻿Гимн Империи = SS14 Империя Миртана
Гимн Свободных Планет = SS14 СНК
Гимн СССП = SS14 СССП
Гимн ТСФ = SS14 ТСФ
Спонсированно Мисс Хаус = The House Always Wins (The Stupendium) очень незакончено
12 стульев = х/ф «12 стульев»
A real hero = Electric Youth (Drive OST)
A step forward into terror = Guilty Gear Xrd
Addict = Hazbin Hotel (Отель Хазбин)
America fuck yeah = Team America: World Police
Angel of doom = Neon Genesis Evangelion
Bad Apple = Touhou Project
Barefoot in the park = Neon Genesis Evangelion
Benny hill = Шоу Бенни Хилла (Yakety Sax)
Better call Saul = Сериал «Лучше звоните Солу» / «Во все тяжкие»
Bitter choco decoration = syudou feat. Hatsune Miku
Blood theme = Сериал «Декстер» (Dexter OST)
Borderline case = The End of Evangelion
Both of you dance like you want to win = Neon Genesis Evangelion
Breaking Bad OST = Сериал «Во все тяжкие»
Cantina = Звёздные войны (Star Wars)
Cell block tango = Мюзикл «Чикаго»
Come along with me = Время Приключений (Adventure Time)
Cruel Angel Thesis = Neon Genesis Evangelion (ТВ-опенинг)
Daddy cop = Сериал «Новичок» (The Rookie)
Decisive battle = Neon Genesis Evangelion
Duvet = Serial Experiments Lain (bôa)
Edelweiss = х/ф «Звуки музыки»
Escape to the beginning = The End of Evangelion
Everything stays = Время Приключений (Adventure Time)
Everything you've ever dreamed = Neon Genesis Evangelion
Expansion of blockade = The End of Evangelion
Eye of the tiger = Survivor (Рокки III)
Far from any road = Сериал «Настоящий детектив» (The Handsome Family)
Fate = Evangelion: 2.0 You Can (Not) Advance
Fly me to the Moon = Neon Genesis Evangelion (ТВ-эндинг)
For the damage coda = Рик и Морти (Злой Морти / Blonde Redhead)
Golden = KPop Demon Hunters
Gonna fly = Рокки (Rocky Theme)
Good, bad, the ugly = Хороший, плохой, злой (Эннио Морриконе)
Goodbuy Moonman = Рик и Морти (Goodbye Moonmen)
Green hornet = Убить Билла (Al Hirt)
Hedgehog's dilemma = Neon Genesis Evangelion
How bad can i be = м/ф «Лоракс»
I really want to stay at your house = Cyberpunk: Edgerunners (Rosa Walton)
I'll be there for you = Сериал «Друзья» (The Rembrandts)
Inferno = Пламенный отряд кошек (Fire Force Opening)
Interference of others = The End of Evangelion
Komm suesser tod = The End of Evangelion
Marking time, waiting for death = The End of Evangelion
Merry go round of life = Ходячий замок Хаула (Джо Хисаиси)
Misato = Neon Genesis Evangelion
Misirlou = Криминальное чтиво (Pulp Fiction)
Mr.Cellophane = Мюзикл «Чикаго»
Never meant to belong = Аниме «Блич» (Bleach OST)
Nightcall = Kavinsky (Drive OST)
Office = Сериал «Офис» (The Office Theme)
One last kiss = Evangelion: 3.0+1.0 Thrice Upon a Time (Hikaru Utada)
Opening of dream = Neon Genesis Evangelion
Razzle dazzle = Мюзикл «Чикаго»
Rei II = Neon Genesis Evangelion
Running the show = Удивительный цифровой цирк
Skies of love = Легенда о героях Галактики (Mitchie M)
Space oddity = David Bowie
Speak softly love = Крёстный отец (The Godfather)
Stuck in the middle with you = Бешеные псы (Stealers Wheel)
Substitute invasion = The End of Evangelion
Take a look around = Миссия невыполнима 2 (Limp Bizkit)
Take me out = Franz Ferdinand
Thanatos = Neon Genesis Evangelion
The amazing digital circus = Удивительный цифровой цирк
The beast II = Neon Genesis Evangelion
The chase = Neon Genesis Evangelion
The entertainer = Скотт Джоплин (Рэгтайм)
The lonely shepherd = Убить Билла (Джеймс Ласт и Георге Замфир)
The phantom of the opera = Призрак Оперы
This Fffire = Franz Ferdinand (Cyberpunk: Edgerunners)
Twisted nerve = Убить Билла (Свист / Бернард Херрманн)
Una mattina = 1+1 / Неприкасаемые (Людовико Эйнауди)
Unravel = Токийский гуль (Tokyo Ghoul)
Unwelcome school = Blue Archive
We are number one = Лентяево (LazyTown)
We both reached for a gun = Мюзикл «Чикаго»
When you're good to mama = Мюзикл «Чикаго»
Where is my mind = Бойцовский клуб (Pixies)
Woo-hoo = Убить Билла (The 5.6.7.8's)
Yokoku = Neon Genesis Evangelion (Анонс следующей серии)
You'll be okay = Адский босс (Helluva Boss)
You've got a friend in me = История игрушек (Toy Story)
Your idol = KPop Demon Hunters
Your new home = Удивительный цифровой цирк
Бандито = м/ф «Приключения капитана Врунгеля»
Братья Пилоты = Следствие ведут Колобки
Бригада = Сериал «Бригада» (главная тема)
Бумер = х/ф «Бумер» (мобильник)
В краю магнолий = х/ф «Груз 200» (Ариэль)
В синем море,в белой пене = м/ф «В синем море, в белой пене...»
Деревня дураков = Каламбур (Деревня дураков)
Завтра грабим короля = м/ф «Бременские музыканты»
Колыбельная медведицы = м/ф «Умка»
Надежда = Анна Герман
Ночной дозор = х/ф «Ночной дозор» (Уматурман)
Ну погоди = м/ф «Ну, погоди!»
О мальчике Бобби = м/ф «Остров сокровищ»
Облака - белогривые лошадки = м/ф «Трям! Здравствуйте!»
Остров невезения = х/ф «Бриллиантовая рука»
Падал прошлогодний снег = м/ф «Падал прошлогодний снег» (финальная тема)
Песенка о вреде курения = м/ф «Остров сокровищ»
Песня агента = м/ф «Приключения капитана Врунгеля»
Песня Василисы = м/ф «Бременские музыканты»
Песня Гениального Сыщика = м/ф «Бременские музыканты»
Песня капитана Врунгеля = м/ф «Приключения капитана Врунгеля»
Песня о медведях = х/ф «Кавказская пленница»
Планета Шелезяка = м/ф «Тайна третьей планеты»
Поход = х/ф «Сибириада» (Эдуард Артемьев)
Прекрасное далёко = х/ф «Гостья из будущего»
Про зайцев = х/ф «Бриллиантовая рука»
Проснись и пой = д/ф «Джентльмены удачи» (Лариса Мондрус)
Разговор со счастьем = х/ф «Иван Васильевич меняет профессию»
Султан = х/ф «Кавказская пленница»
Тёмная ночь = х/ф «Два бойца» (Марк Бернес)
Тайна Третьей Планеты = м/ф «Тайна третьей планеты»
Тема битвы = х/ф «Приключения Буратино»
Тема Цирка = х/ф «Приключения Буратино»
Тихий огонёк = Сериал «Дальнобойщики» (Високосный Год)
У природы нет плохой погоды = х/ф «Служебный роман» (Алиса Фрейндлих)
Уно - Моменто = х/ф «Формула любви»
Что такое С-О-С = м/ф «Приключения капитана Врунгеля»
Air = Иоганн Себастьян Бах («Воздух» / Оркестровая сюита №3)
All i want for christmas = Mariah Carey (Новогодний хит)
Besame mucho = Консуэло Веласкес (Мексиканское болеро)
Bolero = Морис Равель («Болеро»)
Canon = Иоганн Пахельбель («Канон в ре мажор»)
Cello Suite No. 1 in G Major, BWV 1007 = Иоганн Себастьян Бах (Сюита для виолончели №1)
Debussy Deux №1 = Клод Дебюсси («Два арабеска» / Arabesque No. 1)
Dies iræ 2b = День гнева (Средневековый католический гимн)
Dis moi Lune = Мельница / Лолита (Кавер на песню группы Mecano — Hijo de la Luna)
Eine kleine nachtmusik K. 525 1. Allegro = Вольфганг Амадей Моцарт («Маленькая ночная серенада»)
Grave march = Похоронный марш (Традиционная траурная музыка)
Hungarian dance = Иоганнес Брамс («Венгерский танец №5»)
Jesus bleibet meine Freude = Иоганн Себастьян Бах (Хорал «Иисус моя радость остаётся»)
Jew on Christmas = South Park (Песня Кайла «The Lonely Jew on Christmas»)
La petite fille de la mer = Vangelis (Из альбома L'Apocalypse des animaux)
Lacrimosa = Вольфганг Амадей Моцарт («Реквием» — Лакримоза)
Last christmas = Wham! (Джордж Майкл)
Let it snow = Фрэнк Синатра / Дин Мартин (Новогодний хит)
Lohengrin, prelude to act 3 = Рихард Вагнер (Опера «Лоэнгрин» / Вступление к 3 акту)
Love is blue = Поль Мориа (Оркестр Поля Мориа — L'Amour Est Bleu)
Mahler symphony No3 = Густав Малер (Симфония №3)
Minuet = Луиджи Боккерини (Знаменитый «Менуэт»)
Nocturne in E Flat Opus 9 No2 = Фредерик Шопен (Ноктюрн ми-бемоль мажор)
Nocturne in F sharp major Op. 15 No2 = Фредерик Шопен (Ноктюрн фа-диез мажор)
Nocturne No9 Op.32 No1 in B major = Фредерик Шопен (Ноктюрн си мажор)
Nocturnes, Op.9 No1 in B-flat Minor = Фредерик Шопен (Ноктюрн си-бемоль минор)
Ode to Joy = Людвиг ван Бетховен («Ода к радости» / Симфония №9)
Rain = Иоганн Себастьян Бах («Дождь»)
Sonata No8 in C Minor, Op. 13 Pathetique = Людвиг ван Бетховен (Патетическая соната)
Spring Waltz = Фредерик Шопен («Весенний вальс» / Ошибочно приписываемый)
Swan lake finalle = Пётр Чайковский (Балет «Лебединое озеро» — Финал)
Swan lake valse = Пётр Чайковский (Балет «Лебединое озеро» — Вальс)
Symphony No.9 From new world = Антонин Дворжак (Симфония №9 «Из Нового Света»)
The Second Waltz = Дмитрий Шостакович (Вальс №2)
Waltz b minor = Фредерик Шопен (Вальс си минор, Op. 69 No. 2)
Waltz in C sharp minor 64 No2 = Фредерик Шопен (Вальс до-диез минор)
Waltz No2 in B Minor = Фредерик Шопен (Вальс си минор)
Waltz = Евгений Дога (Вальс из х/ф «Мой ласковый и нежный зверь»)
Wedding march = Феликс Мендельсон (Свадебный марш)
Полёт шмеля = Николай Римский-Корсаков (Опера «Сказка о царе Салтане»)
Танец рыцарей = Сергей Прокофьев (Балет «Ромео и Джульетта»)
Танец сахарной феи = Пётр Чайковский (Балет «Щелкунчик»)
Трепак = Пётр Чайковский (Балет «Щелкунчик» — Русский танец)
99 Luftballons = Nena
Another brick in the wall = Pink Floyd
Back in black = AC/DC
Bad to the bone = George Thorogood
Black hole sun = Soundgarden
Bodies = Drowning Pool
Bohemian rhapsody = Queen
Bring me to life = Evanescence
Can't stop = Red Hot Chili Peppers
Carry on my wayward son = Kansas
Come as you are = Nirvana
Do the evolution = Pearl Jam
Down under = Men at Work
Dream on = Aerosmith
Engel = Rammstein
Englishman in New York = Sting
Enter Sandman = Metallica
Every breath you take = The Police
Everybody wants to rule the world = Tears for Fears
Exit music = Radiohead
Faint = Linkin Park
Fell in love with a girl = The White Stripes
For whom the bell tolls = Metallica
Fortunate son = Creedence Clearwater Revival
Free bird = Lynyrd Skynyrd
Hotel California = Eagles
House of the rising Sun = The Animals
I hate everything about you = Three Days Grace
In the end = Linkin Park
It's my life = Bon Jovi
Karma police = Radiohead
La bamba = Los Lobos
Lemon tree = Fools Garden
Let down = Radiohead
Livin' on a prayer = Bon Jovi
Lucky = Radiohead
Man of war = Radiohead
Master of puppets = Metallica
Monster = Skillet
My iron lung = Radiohead
Night witches = Sabaton
Numb = Linkin Park
Nur getraeumt = Nena
Omen = The Prodigy
One last breath = Creed
Paint It black = The Rolling Stones
Paralyzer = Finger Eleven
Paranoid android = Radiohead
Paranoid = Black Sabbath
Primo Victoria = Sabaton
Roundabout = Yes
Run through the jungle = Creedence Clearwater Revival
Seven nation army = The White Stripes
Shut your mouth = Pain
Smells like teen spirit = Nirvana
Smoke on the water = Deep Purple
Sonne = Rammstein
Still loving you = Scorpions
Sultans of swing = Dire Straits
Surfin bird = The Trashmen
Teenagers = My Chemical Romance
Ten o'clock postman = Secret Service
The chain = Fleetwood Mac
The house of the rising sun = The Animals
The man who solds the world = David Bowie / Nirvana
The only = Static-X
Thunderstruck = AC/DC
Voodo people = The Prodigy
Warcry of Salieri = Warmen
Welcome to the Black Parade = My Chemical Romance
What i've done = Linkin Park
White death = Sabaton
Who can it be now = Men at Work
You're gonna go far kid = The Offspring
100 Years = OR3O
1000 doors = The Living Tombstone
Aishu no karamatsuba yashi = muship ft. Kasane Teto
Alberto balsalm = Aphex Twin
AMONG US DRIP = Амогус / Among Us Meme
BL studio loop = Backrooms Meme
Chipi chipi chapa chapa = Boy interaction
Close eyes = DVRST
Die in a fire = The Living Tombstone
Discord call = Звук входящего звонка Discord
Discord = The Living Tombstone
Drunk = The Living Tombstone
El beeper funk = Dj Paulinho Mondi
Entry of the gladiators = Цирковой марш (Юлиус Фучик)
Girl hell 1999 = Femtanyl
Hatachi no Koi = Taiyou Someya
Hello = OMFG
It's not like i like you = Static-P
Kerosene = Crystal Castles
Life letters = Never Get Used To People
Local forecast = Kevin MacLeod
My ordinary life = The Living Tombstone
No mercy = The Living Tombstone
Nokia = Звук звонка Nokia
Nyan cat = Нянкэт
Ochame kinou = Kasane Teto
PoPiPo = Hatsune Miku (Meme)
Skype call = Звук звонка Skype
Snowfall = Reidenshi
Stronger than you = Estelle (Steven Universe)
The fine print = The Stupendium
The human shields = The Stringini Bros
The perfect girl = Mareux
Yamaguchi = Yoshiko Yamaguchi
Гимн НаноТрейзен = SS14 NT
Гимн Синди = SS14 Синдикат
Мечты Blesstar = перс Koranon'a (лоровая херня)
Мечты Куллер = перс Koranon'a (лоровая херня)
Мечты Моримото = перс Koranon'a (лоровая херня)
Мечты Саспенс = перс Koranon'a (лоровая херня)
Мечты Сладкоежки = перс Koranon'a (лоровая херня)
Мечты Спектра-71 = перс Koranon'a (лоровая херня)
Мечты Степчина = перс Koranon'a (лоровая херня)
Мечты Такомур = перс Koranon'a (лоровая херня)
Мечты Хиппель = перс Koranon'a (лоровая херня)
РАФФАЕЛО = Реклама Раффаело
Сок 'Я' = Реклама Сока 'Я'
Судно = Молчат Дома
Angel = Shaggy (Рэгги-поп)
Baby i love your way = Big Mountain (Рэгги)
Bad boys = Inner Circle (Рэгги / Тема из х/ф «Плохие парни»)
Because i got high = Afroman (Рэгги-рэп / Хип-хоп)
Bella Ciao = Итальянская народная (Песня партизан)
Caravan = Хуан Тизол и Дюк Эллингтон (Джазовый стандарт)
Could you be loved = Bob Marley (Рэгги)
Der offene aufmarsch = Ганс Эйслер (Немецкая антифашистская песня)
England = Гимн Великобритании (God Save the King)
Germany = Гимн Германии (Песнь немцев)
Hava Nagila = Еврейская народная (Клезмер)
Hava shalom = Еврейская народная (Клезмер)
Hevenu shalom = Еврейская народная (Клезмер)
Its a long long way to Tipperary = Британская военная песня (Марш Первой мировой)
Jalousie = Якоб Гаде (Цыганское танго «Ревность»)
La cumparsita = Херардо Родригес (Уругвайское танго)
La Verdine = Latcho Drom (Цыганский джаз-мануш)
Lambada = Kaoma (Латино-поп)
Levan polkka = Финская народная полька (Полька Евы)
Mambo Italiano = Розмари Клуни / Розина (Итало-американский шлягер)
Mambo-Mambo = Lou Bega (Мамбо)
Mazel tov = Еврейская народная (Поздравительная клезмер-песня)
Niet Molotoff = Финская военная песня (Песня Зимней войны)
Non je ne regrette rien = Эдит Пиаф (Французский шансон)
Red red wine = UB40 (Рэгги-поп кавер)
Red sun in the sky = Китайская патриотическая песня (Ода Мао Цзэдуну)
Sakkijarven polkka = Финская народная полька (Полька Сяккиярви)
Sambra = Традиционная латиноамериканская самба
Seiben tage lang = Bots (Голландская/Немецкая народная песня)
Serbia strong = Сербская патриотическая песня (Ремзија)
Shuckin the corn = Американская народная (Блюграсс / Кантри)
Smooth = Santana feat. Rob Thomas (Латино-рок)
Soldiers march = Роберт Шуман («Марш солдат» из Альбома для юношества)
Spanish flea = Herb Alpert (Поп-джаз)
Sunshine reggae = Laid Back (Рэгги / Поп-хит 80-х)
Take me home, country road = John Denver (Кантри-фолк)
Tangos caminito = Хуан де Диос Филиберто (Аргентинское танго)
The battle hymn of the republic = Американский патриотический гимн
The girl from Ipanema = Аструд Жилберту (Босса-нова / Джаз)
The star spangled banner = Гимн США
Three little birds = Bob Marley (Рэгги)
When Johnny comes marching home = Американская военная песня (Времён Гражданской войны)
You don't love me (no no no) = Dawn Penn (Регги / Рокстеди)
You gotta move = Mississippi Fred McDowell (Традиционный спиричуэлс / Блюз)
Zundoko-bushi = Японская народная песня (The Drifters версии)
Гимн РФ 93 = Патриотическая песня (Михаил Глинка / Гимн РФ в 1993-2000 гг.)
Дорогой длинною = Борис Фомин (Русский романс)
Идёт солдат = Советская песня (ВИА «Пламя» — Идёт солдат по городу)
Калинка = Иван Ларионов (Русская народная песня)
Крейсер 'Аврора' = м/ф «Ка things» (Владимир Шаинский / Эдуард Хиль)
Молдованка = Анатолий Новиков (Советская вальс-песня)
Последний бой = х/ф «Освобождение» (Михаил Ножкин)
Синий платочек = Клавдия Шульженко (Советская вальс-песня)
Славься Русь = Жанна Бичевская (Патриотическая песня)
Славянка = Василий Агапкин (Марш «Прощание славянки»)
Юный октябрь = Советская песня (Иосиф Кобзон — И вновь продолжается бой)
A kiss to build a dream on = Louis Armstrong (Джазовый стандарт / Fallout 2 OST)
A little dream of me = The Mamas & the Papas (Джаз-поп шлягер / Dream a Little Dream of Me)
Ain't Misbehavin' = Fats Waller (Классический страйд-джаз)
All night = Parov Stelar (Электросвинг)
All you are going to want to do is get back there = The Caretaker (Проект Лейланда Кирби)
Alligator crawl = Fats Waller (Классический джаз-пианизм)
Angela = Bob James (Тема из сериала «Такси»)
Atom bomb baby = Fallout 4 (The Five Stars)
Bang bang = Nancy Sinatra (х/ф «Убить Билла»)
Beyond the sea = BioShock / Bobby Darin
Big Iron = Fallout: New Vegas (Marty Robbins)
Big spender = Shirley Bassey (Мюзикл «Милая Чарити» / Sweet Charity)
Black betty = Ram Jam (Рок-хит на основе народной песни)
Blue Moon = Fallout: New Vegas (Frank Sinatra)
Blue suede shoes = Elvis Presley (Рокабилли / Рок-н-ролл)
Boogie man = Caravan Palace (Электросвинг)
Booty swing = Parov Stelar (Электросвинг)
Catgroove = Parov Stelar (Электросвинг)
Chambermaid swing = Parov Stelar (Электросвинг)
Cheek to cheek = Fred Astaire / Ella Fitzgerald & Louis Armstrong (Джазовый стандарт)
Close to you = The Carpenters (Поп-классика 70-х)
Coin operated boy = The Dresden Dolls (Дарк-кабаре / Панк-кабаре)
Cry me a river = Julie London (Классический джазовый блюз)
Dear hearts and gentle people = Bob Crosby / Bing Crosby (Fallout 3 OST)
Dizzy fingers = Zez Confrey (Регтайм)
Don't let the stars get in you eyes = Perry Como (Поп-стандарт 50-х / Fallout: New Vegas OST)
Dramophone = Caravan Palace (Электросвинг)
Earth angel = The Penguins (Ду-воп классика / х/ф «Назад в будущее»)
Feeling good = Nina Simone / Muse
Five hundred miles = Hedy West / Peter, Paul and Mary (Фолк-классика / 500 Miles)
Fly me to the moon = Frank Sinatra (Легендарный джазовый стандарт)
Glitz at the ritz = Jules Gaia (Электросвинг)
Heartaches by the number = Fallout: New Vegas (Guy Mitchell)
Heartaches = Ted Weems & His Orchestra (Поп-хит 30-х / Прообраз треков The Caretaker)
Hey pachuco = Royal Crown Revue (Свинг / х/ф «Маска»)
Hit the road Jack = Ray Charles
I don't want to set the world on fire = Fallout 3 (The Ink Spots)
I'm always chaising rainbow = Perry Como / Judy Garland (Поп-стандарт / I'm Always Chasing Rainbows)
In a sentimental mood = Duke Ellington & John Coltrane (Джазовая классика)
Into each life some rains must fall = The Ink Spots & Ella Fitzgerald (Fallout 3 OST)
It don't mean a thing = Duke Ellington (Эра свинга / Джазовый стандарт)
It's just a burning memory = The Caretaker (Проект Everywhere at the End of Time)
Jazz around midnight = Традиционный полуночный джаз-сборник
Jingle jangle jingle = Fallout: New Vegas (Kay Kyser)
Just the two of us = Grover Washington Jr. feat. Bill Withers (Смут-джаз / R&B)
Kitten on the keys = Zez Confrey (Новинка-регтайм)
La vie en rose = Edith Piaf / Louis Armstrong (Французский классический шлягер)
Life could be dream = The Chords (Ду-воп классика / Sh-Boom)
LiraInfluencia do jazz = Carlos Lyra (Бразильская босса-нова / Influência do Jazz)
Lone digger = Caravan Palace (Electro Swing)
Lost in the rhythm = Jamie Berry feat. Octavia Rose (Электросвинг)
Love and marrige = Frank Sinatra (Сериал «Женаты… с детьми»)
Mein herr = Мюзикл «Кабаре» (Лайза Миннелли)
Mr.Sandman = The Chordettes
My way = Frank Sinatra (Эстрадная классика)
NewYork = Frank Sinatra (Theme from New York, New York)
Olive Branch = Lackadaisy
Only you = The Platters (Ду-воп / Романтический хит 50-х)
Peeping Tom = Jamie Berry feat. Rosie Harte (Электросвинг)
Pistol packing mama = Fallout 4 (Bing Crosby & The Andrews Sisters)
Put on your sunday clothe = Мюзикл «Хелло, Долли!» (х/ф «ВАЛЛ-И» OST)
Raindrops keep falling on my head = B.J. Thomas (х/ф «Буч Кэссиди и Сандэнс Кид»)
Rock around the clock = Bill Haley & His Comets (Рок-н-ролл)
Rock it for me = Caravan Palace (Электросвинг)
Russian = Традиционный цыганский или русский романс в джазовой обработке
Sixteen tons = Tennessee Ernie Ford
Sixty minute man = Fallout 4 (The Dominoes)
Slowly jazz = Традиционный медленный джаз / Лаунж
Softly as in a morning sunrise = Джазовый стандарт (Арт Шоу / Сонни Роллинз)
Something stupid = Frank Sinatra & Nancy Sinatra (Поп-дуэт)
Southern nights = Glen Campbell (х/ф «Стражи Галактики 2» OST)
The end of the world = Skeeter Davis (Поп-кантри / Fallout 4 OST)
The very thought of you = Billie Holiday / Nat King Cole (Джазовый стандарт)
The wanderer = Fallout 4 (Dion)
Two of kind = Свинг-дуэт (Фрэнк Синатра и Бинг Кросби / Two of a Kind)
Unfinished business = Традиционный блюз / Джазовый инструментал
Vipers drag = Fats Waller (Страйд-пианино / Джаз)
Wash my hands = Традиционный спиричуэлс / Госпел-блюз
What you won't do for love = Bobby Caldwell (Блюз / Соул / R&B)
Who gonna shack it night along = Традиционный блюз-рок / Ритм-энд-блюз
Why don't you do it right = Peggy Lee / Lil Green (х/ф «Кто подставил кролика Роджера»)
Will meet again = Vera Lynn (Песня времён Второй мировой / х/ф «Доктор Стрейнджлав»)
Wonderful world = Louis Armstrong (What a Wonderful World)
Young and foolish = Джазовый стандарт (Билл Эванс / Тони Беннетт)
505 = Arctic Monkeys
A thousand miles = Vanessa Carlton (Поп-классика 2000-х)
ABCDFU = GAYLE (Поп-рок / ТикТок хит)
Abracadabra = Steve Miller Band (Классический рок)
Accidentally in love = Counting Crows (м/ф «Шрек 2» OST)
Adult education = Hall & Oates (Поп-рок 80-х / GTA Vice City OST)
Adventure of a Lifetime = Coldplay (Поп-рок)
After dark = Mr.Kitty (Синти-поп / Дарквейв)
Alright = Supergrass (Брит-поп / х/ф «Бестолковые»)
American idiot = Green Day (Поп-панк)
American pie = Don McLean / Madonna (Фолк-рок классика)
Angel of the morning = Juice Newton (х/ф «Дэдпул» OST)
Animals = Maroon 5 (Поп-рок)
Another love = Tom Odell (Инди-поп / Фортепианная баллада)
Applause = Lady Gaga (Электропоп)
Around the world = Daft Punk (Хаус / Электроника)
As it was = Harry Styles (Инди-поп)
As the world caves in = Matt Maltese (Инди-рок / Апокалиптическая баллада)
Baby one more time = Britney Spears (Поп-хит 90-х)
Bad girls = Donna Summer (Диско-классика / GTA Grand Theft Auto OST)
Bailando = Enrique Iglesias (Латино-поп)
Ballin = Mustard feat. Roddy Ricch (Рэп / Мем с Аниманом)
Bambalailo = Gipsy Kings (Фламенко-поп / Bamboléo)
Barbie girl = Aqua (Евродэнс 90-х)
Beach parade = Armando Trovajoli (Легкомысленная ретро-мелодия)
Beautiful life = Ace of Base (Евродэнс 90-х)
Better off alone = Alice Deejay (Евротранс 90-х)
Big city life = Mattafix (Трип-хоп / Регги-фьюжн)
Big in Japan = Alphaville (Синти-поп 80-х)
Bimbo doll = Tila Tequila / Tami (Поп-хит 2000-х)
Bitter sweet symphony = The Verve (Брит-поп / Симфонический рок)
Blue monday = New Order
Boom-Boom-Boom = Vengaboys (Евродэнс 90-х)
Breakfast in America = Supertramp (Прогрессивный поп-рок)
Brother Louie = Modern Talking (Евродиско 80-х)
Cake by the ocean = DNCE (Фанк-поп)
California dreaming = The Mamas & the Papas (Фолк-рок 60-х)
Call me maybe = Carly Rae Jepsen (Поп-хит 2010-х)
Call me = Blondie (Нью-вейв / х/ф «Американский жиголо»)
Camel by camel = Sandy Marton (Итало-диско / Мем с танцующей кошкой Анхой)
Can't hold us = Macklemore & Ryan Lewis (Хип-хоп / Поп-рэп)
Caramell dansen = Caramell (Шведский поп-евродэнс / Аниме-мем)
Careless whisper = George Michael
Charlie's inferno = That Handsome Devil[cite: 1]
Cheri lady = Modern Talking (Евродиско 80-х)
Cigarettes out the Window = TV Girl (Инди-поп / ТикТок хит)
Circle in the Sand = Belinda Carlisle (Поп-рок 80-х)
Coca Jambo = Mr. President (Евродэнс / Регги-поп / Coco Jamboo)
Come a little bit closer = Jay & The Americans (х/ф «Стражи Галактики 2» OST)
Come and get your love = Redbone (х/ф «Стражи Галактики» OST)
Cooler than me = Mike Posner (Электропоп)
Creep = Radiohead (Альтернативный рок)
Crimewave = Crystal Castles vs. HEALTH (8-bit / Электроника / Электропоп)
Criminal = Fiona Apple (Альтернативный поп-рок)
Crucified = Army of Lovers (Евродэнс / Шведский поп)
Cupid = FIFTY FIFTY (K-Pop / ТикТок хит)
D.I.S.C.O = Ottawan (Диско 80-х)
Dancin = Aaron Smith (KRONO Remix / Электро-хаус)
Dancing in the Moon light = King Harvest / Toploader (Поп-рок классика)
Denise = Blondie (Нью-вейв 70-х)
Die for you = The Weeknd (R&B / Поп)
Do ya think i'm sexy = Rod Stewart (Диско-рок)
Don't cry tonight = Savage (Итало-диско 80-х)
Don't wanna fall in love = Jane Child (Синти-поп 90-х)
Don't worry be happy = Bobby McFerrin (Регги-акапелла)
Dumb dumb = Red Velvet (K-Pop)
Egoist = Шамиль (Кавказский поп-хит / Эгоист)
Eleanor Rigby = The Beatles (Барокко-поп / Классический рок)
Escape (The Pina Colada song) = Rupert Holmes (Яхт-рок / х/ф «Стражи Галактики»)
Estrelar = Marcos Valle (Бразильский фанк / Буги 80-х)
ET = Katy Perry (Электропоп)
Every time we touch = Cascada (Евротранс 2000-х)
Everything at once = Lenka (Инди-поп / Реклама Windows 8)
Everything in the right place = Radiohead (Экспериментальный рок / IDM)
Everything she wants = Wham! (Синти-поп / Джордж Майкл)
Fairytale = Александр Рыбак (Победитель Евровидения 2009)
Fergie glamorous = Fergie feat. Ludacris (R&B / Хип-хоп 2000-х)
Finale coutdown = Europe (Глэм-метал / The Final Countdown)
Firework = Katy Perry (Поп-хит)
Fliday chinatown = Yasuha (Японский сити-поп 80-х / Friday Chinatown)
From the start = Laufey (Джаз-поп / Босса-нова)
Fun tonight = Lady Gaga (Танцевальный поп)
Funkytown = Lipps Inc. (Диско / Синти-поп)
Gangstas Paradise = Coolio (Легендарный хип-хоп / х/ф «Опасные умы»)
Gas gas gas = Manuel (Евробит / Аниме «Initial D»)
Get around town = Revolting Cocks (Индастриал-рок)
Get low = Lil Jon & The East Side Boyz (Кранк / NFS Underground OST)
Get lucky = Daft Punk feat. Pharrell Williams (Диско-фанк)
Gimme = ABBA (Gimme! Gimme! Gimme!)
Giorgio = Daft Punk (Электроника / Посвящение Джорджо Мородеру)
Glamorous = Fergie (R&B / Поп)
Golden brown = The Stranglers (Нью-вейв / х/ф «Большой куш»)
Guten tag liebes glück = Max Raabe (Немецкий ретро-поп / Кабаре)
Gypsy woman = Crystal Waters (Хаус-хит 90-х)
Hafanana = Afric Simone (Афро-диско 70-х)
Happiest year = Jaymes Young (Инди-поп баллада)
Heaven knows i'm miserable now = The Smiths (Инди-рок / Дангл-поп)
Hooked on a feeling = Blue Swede (х/ф «Стражи Галактики» OST)
Hot stuff = Donna Summer (Диско-рок)
HotNCold = Katy Perry (Поп-рок хит)
Hurt = Nine Inch Nails / Johnny Cash (Альтернативный рок / Кантри)
I can't stop the loneliness = Anri (Японский сити-поп 80-х)
I just died in your arms = Cutting Crew (Поп-рок 80-х / GTA Vice City OST)
I kissed a girl = Katy Perry (Поп-рок хит)
I like the way kiss me = Artemas (Дарк-синти / ТикТок хит)
I love it = Icona Pop feat. Charli XCX (Электропоп)
I love you so = The Walters (Инди-рок)
I need some sleep = Eels (м/ф «Шрек 2» OST)
I want it that way = Backstreet Boys (Бой-бэнд поп-классика)
I want to know what love is = Foreigner (Рок-баллада 80-х)
I will survive = Gloria Gaynor (Диско-гимн)
I'm a believer = The Monkeys / Smash Mouth (м/ф «Шрек» OST)
I'm just a kid = Simple Plan (Поп-панк 2000-х)
In da club = 50 Cent (Хип-хоп классика)
In the navy = Village People (Диско-хит 70-х)
In the summertime = Mungo Jerry (Скиффл / Поп-рок)
Industry baby = Lil Nas X feat. Jack Harlow (Поп-рэп)
Instant crush = Daft Punk feat. Julian Casablancas (Синти-поп / Электро-рок)
It doesn't have to be this way = The Blow Monkeys (Софисти-поп 80-х)
It was a good day = Ice Cube (Джи-фанк / Хип-хоп)
Jen ai marre = Alizée (Французский поп-хит / J'en ai marre!)
Jocelyn flores = XXXTentacion (Эмо-рэп / Лоу-фай)
Jodellavitanonhocapitouncazzo = Caparezza (Итальянский альтернативный рэп)
Kids = MGMT (Инди-поп / Электропоп)
Knew you were trouble = Taylor Swift (Поп / Дабстеп-поп)
Lady = Modjo (Французский хаус / Lady - Hear Me Tonight)
Lay all your love on me = ABBA (Евродиско)
Let it happen = Tame Impala (Психоделический поп / Инди-рок)
Let's go = Stuck in the Sound (Инди-рок)
Let's groove = Earth, Wind & Fire (Диско-фанк 80-х)
Lets go to bed = The Cure (Нью-вейв / Пост-панк)
Life goes on = Oliver Tree (Инди-поп / Альтернатива)
Lily was here = Candy Dulfer & David A. Stewart (Легендарное соло на саксофоне)
Little dark age = MGMT (Синти-поп / Дарквейв / Мем)
Livin la vida loca = Ricky Martin (Латино-поп)
Lollipop = The Chordettes (Поп-классика 50-х)
Lose yourself = Eminem (Хип-хоп / х/ф «8 миля» OST)
Love is a long road = Tom Petty (Классический рок / Трейлер GTA VI)
Lovers on the sun = David Guetta (Электро-хаус / Дэнс-поп)
Macarena = Los Del Rio (Латино-танцевальный хит 90-х)
Magic spells = Crystal Castles (8-bit / Электроника)
Major Tom = Peter Schilling (Синти-поп / Немецкая «Новая волна»)
Make it bun dem = Skillet feat. Damian Marley (Дабстеп / Регги / Far Cry 3 OST)
Make your own kind of music = Cass Elliot (х/ф «Free Guy» / Сериал «LOST» OST)
Maniac = Michael Sembello (х/ф «Танец-вспышка» / Синема-синти)
Maria Magdalena = Sandra (Евродиско 80-х)
Me and the birds = Duster (Слоукор / Мем с Сизифом)
Me gustas tu = Manu Chao (Латино-поп / Регги)
Meet me halfway = Black Eyed Peas (Поп-рэп / Электропоп)
Messages from the stars = The Rah Band (Синти-фанк 80-х / ТикТок хит)
Midnight city = M83 (Инди-поп / Дрим-поп)
Military fashion showe = And One (EBM / Синти-поп / Military Fashion Show)
Miss Jackson = Panic! At The Disco (Альтернативный рок)
Miss the Rage = Trippie Redd feat. Playboi Carti (Рэйдж-рэп)
Moi lolita = Alizée (Французский поп-хит)
More then a filling = Boston (Классический рок / More Than a Feeling)
Moves like jagger = Maroon 5 feat. Christina Aguilera (Поп-фанк)
Mr.Blue Sky = Electric Light Orchestra (Симфо-рок / х/ф «Стражи Галактики 2»)
Mr.Bombastic = Shaggy (Регги-поп / Boombastic)
Mr.Saxobeat = Alexandra Stan (Евродэнс / Дэнс-поп)
Mr.Vain = Culture Beat (Евродэнс 90-х)
Music sounds better with you = Stardust (Французский хаус 90-х)
Natural = Imagine Dragons (Альтернативный рок)
Never gonna give you up = Рикролл / Rick Astley
New sensation = INXS (Поп-рок / Фанк-рок 80-х)
No surprises = Radiohead (Альтернативный рок / Меланхолия)
Nothing breaks like a heart = Mark Ronson feat. Miley Cyrus (Диско-поп / Кантри-поп)
One thing = One Direction (Поп / Бой-бэнд)
One way or another = Blondie (Нью-вейв / Панк-рок)
One = Metallica (Хэви-метал / Трэш-метал)
Only girl = Rihanna (Электропоп / Европоп)
Only time will tell = Asia (Прогрессивный рок 80-х / Metal Gear Solid V OST)
Out of touch = Hall & Oates (Синти-поп / фанк / GTA Vice City OST)
Papaoutai = Stromae (Электропоп / Хип-хоп)
Play that funky music = Wild Cherry (Фанк-рок классика)
Playing dead = CHVRCHES (Синти-поп)
Pompeii = Bastille (Инди-поп)
Pretty woman = Roy Orbison (Рок-н-ролл классика / Oh, Pretty Woman)
Promises, promises = Naked Eyes (Синти-поп 80-х)
Psycho killer = Talking Heads (Нью-вейв / Арт-понк)
Pumped up kicks = Foster the People
Pure shores = All Saints (х/ф «Пляж» OST / Дрим-поп)
Push it to the limit = Paul Engemann (х/ф «Лицо со шрамом» OST)
Relaxed scene = Лаунж / Традиционная фоновая музыка для расслабления
Replay = Iyaz (Поп / R&B 2010-х)
Revenge = XXXTentacion (Инди-поп / Акустический рэп)
Rhythm is a dancer = Snap! (Евродэнс 90-х)
Ride It = Jay Sean / Regard (Диско-хаус ремикс)
Ridin dirty = Chamillionaire (Хип-хоп / Мем «They see me rollin'»)
Riptide = Vance Joy (Инди-фолк / Укулеле-поп)
Roar = Katy Perry (Поп-хит)
Run away baby = Bruno Mars (Фанк-поп / Соул)
Running in 90s = Max Coveri (Евробит / Аниме «Initial D»)
Running up that hill = Kate Bush (Синти-поп / Сериал «Очень странные дела»)
Sadness = Enigma (Нью-эйдж / Энигматика / Этно-эмбиент)
Safe and sound = Capital Cities (Инди-поп / Синти-поп)
Sailor song = Gigi Perez (Инди-фолк / ТикТок хит)
Sayonara = Дискотека Авария / Танцевальный поп
Scatman = Scatman John (Евродэнс / Скэт)
Scatmans world = Scatman John (Евродэнс / Скэт)
Send me an angel = Real Life / Scorpions (Синти-поп 80-х или Рок-баллада)
September = Earth, Wind & Fire (Диско-фанк)
Sexy eyes = Dr. Hook / Whigfield (Поп-диско хит)
Shake it off = Taylor Swift (Поп-хит)
Sinking town = Инди-поп / Меланхоличный фолк
Six undeground = Sneaker Pimps (Трип-хоп / 6 Underground)
Skyfall = Adele (х/ф «007: Координаты „Скайфолл“»)
Smalltown boy = Bronski Beat (Синти-поп / Гей-гимн 80-х)
Smooth operator = Sade (Софисти-поп / Смут-джаз)
So far so good = Bryan Adams / Sheena Easton (Поп-рок)
So klingt liebe = 50 Hertz / Немецкий поп-трек
Somebody that i used to know = Gotye
Somebody to love = Queen / Jefferson Airplane (Классический рок)
Something about us = Daft Punk (Синти-фанк / Хаус)
Somthing got me started = Simply Red (Поп-соул / Данс-поп)
Song 2 = Blur (Альтернативный рок / Брит-поп)
Space oddity = David Bowie
Space song = Beach House (Дрим-поп / Инди-поп)
Stan = Eminem feat. Dido (Хип-хоп баллада)
Stay = The Kid LAROI & Justin Bieber (Синти-поп)
Stayin alive = Bee Gees (Диско-классика / х/ф «Лихорадка субботнего вечера»)
Stereo heart = Gym Class Heroes feat. Adam Levine (Поп-рэп)
Still DRE = Dr. Dre feat. Snoop Dogg (Хип-хоп классика)
Stolen dance = Milky Chance (Инди-поп / Фольктроника)
Stressed out = Twenty One Pilots (Альтернативный хип-хоп / Инди-поп)
Stromae alors on danse = Stromae (Евродэнс / Хип-хаус)
Sunny = Boney M. (Диско-классика)
Supersonic rocket ship = The Kinks (Классический рок / х/ф «Мстители: Финал»)
Sweet dreams = Eurythmics
Sweety sweety = Поп-шлягер / Кавай-поп мелодия
Tell It to my heart = Taylor Dayne (Дэнс-поп 80-х)
The bidding = Tally Hall (Инди-рок)
The dream = Ветро-синти / Трэк в стиле саундтреков 80-х
The lost song = The Cat Empire (Ска-джаз / Латино-рок)
The rhythm of the night = Corona (Евродэнс 90-х)
The sign = Ace of Base (Европоп 90-х)
They call me Sonic = Reset (Евробит / Мем про Соника)
Tick Tock = Joji (R&B / Мем со стражами из TF2)
Titanic = Celine Dion (My Heart Will Go On / х/ф «Титаник»)
Titanium = David Guetta feat. Sia (Электропоп / Хаус)
Tom's diner = Suzanne Vega (Акапелла / Инди-поп классика)
Tous les memes = Stromae (Электропоп / Французский хип-хоп)
Twilight = Electric Light Orchestra (Синти-рок / Аниме Daicon IV)
Ulterior motives = Christopher Saint Booth (Потерянная песня 80-х / Everyone Knows That)
Veridis Quo = Daft Punk (Электроника / Синти-вейв)
Video killed the radio star = The Buggles
Virtual Insanity = Jamiroquai
Viva la Vida = Coldplay (Барокко-поп / Альтернативный рок)
Wake me up before you go go = Wham! (Поп-хит 80-х / Джордж Майкл)
Wake me up = Avicii (Фольктроника / Дэнс-поп)
Washing machine heart = Mitski (Инди-рок / Синти-поп)
What is love = Haddaway (Евродэнс 90-х / Мем с качанием головой)
When we stand together = Nickelback (Пост-гранж / Альтернативный рок)
Wicked game = Chris Isaak (Меланхоличный поп-рок)
Wish you were here = Pink Floyd / Avril Lavigne (Рок-классика)
Wolf in sheeps clothing = Set It Off (Альтернативный рок / Поп-панк)
Wonderful tonight = Eric Clapton (Классическая рок-баллада)
Words = F.R. David (Синти-поп / Евродиско 80-х)
World hold on = Bob Sinclar (Хаус / Электронный хит 2000-х)
Wouldn't it be nice = The Beach Boys (Поп-рок 60-х / Fallout 76 OST)
Write this down = Soulchef (Хип-хоп / Лоу-фай рэп-инструментал)
X gona give it to ya = DMX (Хардкор-рэп / х/ф «Дэдпул»)
Yeah = Usher feat. Lil Jon (R&B / Кранк 2000-х)
You can't touch this = MC Hammer (Хип-хоп 90-х / U Can't Touch This)
You speen me round = Dead or Alive (Синти-поп 80-х / You Spin Me Round)
You're my soul = Modern Talking (You're My Heart, You're My Soul / Диско 80-х)
Yes future = Noize MC (Альтернативный хип-хоп)
Алиса = Секрет (Поп-рок)
Альпинист = Маша и Медведи (Альтернативный рок)
Ариведерчи = Земфира (Рок / Поп-рок)
Арлекино = Алла Пугачёва (Эстрадная классика)
Батарейка = Жуки
Белая ночь = Форум / Виктор Салтыков
Белые розы = Ласковый май / Юрий Шатунов
Бродяга = Эльбрус Джанмирзоев (Поп / Кавказский хит)
Букет = Александр Барыкин (Советский поп-рок)
Вечно молодой = Смысловые Галлюцинации (х/ф «Брат 2» OST)
Владимирский централ = Михаил Круг
Восточные сказки = Блестящие feat. Arash (Поп)
Всё, что тебя касается = Звери (Поп-рок)
Выхода нет = Сплин
Гимнастика = Владимир Высоцкий (Утренняя гимнастика)
Главное = Мара / Город 312 (Рок / Поп-рок)
Голая = Градусы (Поп-рок)
Город которого нет = Игорь Корнелюк (Сериал «Бандитский Петербург» OST)
Девочка-видение = Максим Леонидов (Поп-рок)
До свидания = Земфира (До свиданья...)
До скорой встречи = Звери (Поп-рок)
Дождь = ДДТ (Юрий Шевчук)
Дорога = АукцЫон (х/ф «Брат 2» OST)
Ева, я любила = Винтаж (Поп / Посвящение Еве Польне)
Железо поёт = Советский индустриальный марш / Электронный трек
Звёздное лето = Алла Пугачёва (Советская эстрада)
Звёзды нас ждут = Мираж (Евродиско 80-х)
Как бы всё = Ноль (Русский рок)
Как на войне = Агата Кристи
Комарово = Игорь Скляр / Atomic Heart OST
Косил Ясь конюшину = Песняры (Белорусская народная песня / ВИА)
Кто ты = Децл (Хип-хоп 2000-х)
Кто = Ноль (Человек и кошка) / Децл
Любочка = Маша и Медведи (Альтернативный рок)
Люди встречаются = Весёлые Ребята (Советский ВИА-шлягер)
Мало тебя = SEREBRO (Поп-хит)
Мальчик-гей = t.A.T.u. (Поп / Европоп)
Мама Люба = SEREBRO (Поп-хит / Mama Lover)
Моё сердце = Сплин (Поп-рок)
Мой друг = Машина Времени / Игорь Крутой
Моя любовь = Владимир Кузьмин / Би-2
Музыка нас связала = Мираж (Евродиско 80-х)
Мы сидели и курили = Сплин (Рок)
На седьмом этаже = Лера Массква (Поп-рок)
На белом покрывале января = Сладкий сон (Поп 90-х)
Нас не догонят = t.A.T.u. (Поп / Европоп)
Наше лето = Валентин Стрыкало (Инди-поп / Яхта, парус)
Не волнуйтесь, тётя = Весёлые Ребята (Советский ВИА)
Не танцую = Quest Pistols Show (Поп / Танцевальный)
Опера#2 = Витас (Поп / Фирменный фальцет)
Отпускаю = МакSим (Поп-баллада нулевых)
Поворот = Машина Времени (Классика русского рока)
Поезд в огне = Аквариум (Борис Гребенщиков)
Позови меня с собой = Алла Пугачёва (Татьяна Снежина)
Прасковья = Uma2rman (Поп-рок)
Привет = Секрет / Юлия Савичева (Поп-рок)
Прованс = Ёлка (Поп-хит)
Просвистела = ДДТ (Юрий Шевчук)
Прости, прощай, привет = Ранетки / Поп-рок
Ромашки = Земфира (Рок)
Снег = Николай Носков / Филипп Киркоров / Машина Времени
Солнышко = Демо (Евродэнс 90-х / Солнышко в руках)
СПИД = Земфира (Рок)
Тёплые коты = Flëur (Кардиовейв / Инди-фолк)
Тополиный пух = Иванушки International (Поп-хит 90-х)
Трава у дома = Земляне
Убили негра = Запрещённые Барабанщики (Поп-рок / Ска)
Улыбки cфинксов = Ретро-электроника / Советский синти-поп
Уматурман = Uma2rman (Ночной дозор OST)
Фаина = На-На (Поп-хит 90-х)
Фантазёр = Ярослав Евдокимов (Эстрадный шлягер)
Формалин = Flëur (Кардиовейв / Дарк-фолк)
Хали-гали = Леприконсы (Хали-гали, паратрупер / Ска-поп)
Хочешь = Земфира (Рок)
Чёрный кот = Тамара Миансарова / Браво (Советский твист)
Человек и кошка = Ноль (Фёдор Чистяков)
Шарманка = Николай Басков (Эстрада)
Эй толстый = Дискотека Авария (Танцевальный рэп)
Я солдат = 5'nizza (Регги-акустика)
Я сошла с ума = t.A.T.u. (Поп / Европоп)
Январская вьюга = Нина Бродская (х/ф «Иван Васильевич меняет профессию» OST)
1100 = Ария (Хэви-метал)
2000 баксов за сигарету = Торба-на-Круче (Альтернативный рок)
Алюминиевые огурцы = Кино (Виктор Цой)
Андердог = Ляпис Трубецкой (Панк-рок)
Беспечный ангел = Ария (Хэви-метал кавер на Golden Earring)
Восьмиклассница = Кино (Виктор Цой)
Гибралтар - лабрадор = Вячеслав Бутусов (х/ф «Брат 2» OST)
Группа крови = Кино (Виктор Цой)
Два вора и монета = Король и Шут (Хоррор-панк)
Джокер = Король и Шут / Сплин (Рок)
Закрой за мной дверь = Кино (Виктор Цой)
Звезда по имени Солнце = Кино (Виктор Цой)
Капитал = Ляпис Трубецкой (Ска-панк)
Когда твоя девушка больна = Кино (Виктор Цой)
Кончится лето = Кино (Виктор Цой)
Кукушка = Кино (Виктор Цой)
Мороз по коже = Сплин (Рок)
Мы лёд = Гражданская Оборона (Егор Летов)
Орбит без сахара = Сплин (Рок)
ПММЛ = Земфира (Прости меня моя любовь)
Полковнику никто не пишет = Би-2 (Брат 2 OST)
Последний герой = Кино (Виктор Цой)
Потерянный рай = Ария (Рок-баллада)
Прогулки по воде = Наутилус Помпилиус (Рок)
Романс = Сплин (И лампа не горит...)
Северный ветер = Сектор Газа / Рок-хит
Сентябрь = Stigmata (Металкор / Мем про «Сентябрь горит»)
Скованные одной цепью = Наутилус Помпилиус (Рок)
Трасса Е-95 = Алиса (Константин Кинчев)
Устрой дестрой = Noize MC feat. Чача (Альтернативный рок / Рэп-рок)
Фантом = Чиж & Co (Рок-кавер на советскую дворовую песню)
Я на тебе как на войне = Агата Кристи
Я хочу быть с тобой = Наутилус Помпилиус (Рок)A little heart to heart = ???
A promise from distant days = Бесконечное лето OST (Everlasting Summer)
About her = Бесконечное лето OST (Everlasting Summer)
Absolute territory = Ken Ashcorp
Arstotzkan Anthem = Papers, Please
Attack of the Killer Queen = Deltarune: Chapter 2
Baka mitai = Yakuza 0
Battle against a true hero = Undertale (Тема Бессмертной Андайн)
BFG Division = DOOM (Мик Гордон)
Bonetrousle = Undertale (Тема Папируса)
Boombox = Lethal Company
Claw finger = Silent Hill 2 OST (Акира Ямаока)
Coalescence = Risk of Rain OST (Крис Христодулу)
Coconut mail = Mario Kart Wii (Coconut Mall)
CP Violation = Half-Life 2
Death by glamour = Undertale (Тема Меттатона)
Dream BBQ = ENAENAENAENAENAENAENAENAENA
Eirin's clinic that people line up for = Touhou Project (IOSYS)
Elevator jam = Roblox
Every light is blinking at once = Portal 2 OST
Everylasting summer = Бесконечное лето OST (Everlasting Summer)
Fairy fountain = The Legend of Zelda OST (Тема Великих Фей)
Fallen = Undertale OST
Farewell to the past = Бесконечное лето OST (Everlasting Summer)
Flip-Flap = SS13
Forest maiden = Бесконечное лето OST (Everlasting Summer)
Goat chill = Undertale OST (Размеренная тема Ториэль)
Gourmet race concert = Kirby Super Star (Гурмэ-гонка / Трэп и оркестровые ремиксы)
Greateful love = Аниме-трек / J-Pop
Head revolutionary = SS13
Heartache = Undertale (Тема Ториэль)
Help me Erinnnnnn = Touhou Project
Henry stickman dance = The Henry Stickmin Collection (Мем с отвлекающим танцем)
Hip Shop = Deltarune: Chapter 1 (Тема магазина Руулса Каарда)
Ice cream song = Невинная ретро-мелодия фургончика с мороженым
In the pines = Telltale's The Walking Dead
It has to be this way = Metal Gear Rising: Revengeance
It's pizza time = Pizza Tower OST
Just asking at day = No, I'm not a human
Just asking at night = No, I'm not a human
Last Surpise = Persona 5 (Тема боя / Last Surprise)
Let's be friends = Бесконечное лето OST (Everlasting Summer)
Little trinketry = Valiant hearts
Live to forget = Сталкер
Make it bun dem = Skrillex & Damian Marley (Far Cry 3 OST)
Mannrobics = Team Fortress 2
Maybe we can win this = Project Zomboid
Metal сrusher = Undertale (Первая встреча с Меттатоном)
Meteor = SS13
Metro exodus = Метро: Исход (Главная тема)
Miku`s song = Бесконечное лето OST (Everlasting Summer)
Mond, Mond! Ja, Ja! = Wolfenstein: The New Order OST
Nine thou superstars = Need for Speed: Most Wanted (Styles of Beyond - Nine Thou)
O cara mia, addio = Portal 2 (Турельная опера)
Pandora palace = Deltarune: Chapter 2 (Тема дворца Королевы)
Phoron will make us rich = SS13
Pizza delux = Pizza Tower OST
Pizza theme = Spider-Man 2: The Game
Power of NEO = Undertale (Тема Меттатона НЕО)
Promise reprise = Silent Hill 2 OST (Акира Ямаока)
Queen = Deltarune: Chapter 2 (Тема Королевы)
Razormind = PAYDAY 2 (Simon Viklund)
Resident evil = Resident Evil OST
Right behind you = Team Fortress 2 (Meet the Spy)
Rocket jump waltz = Team Fortress 2
Running out = SS14
Scarlet forest = Deltarune: Chapter 1
Self isolation at night = No, I'm not a human
Shop = Undertale OST
Soilder of dance = Team Fortress 2
Song that may play when you fight Sans = Undertale (Секретный трек из саундтрека)
Soviet march = Command & Conquer: Red Alert 3
Space asshole = Спейс ассхолл
Space Station 14 OST = Главная тема СС14
Spider dance = Undertale (Тема Маффет)
The death that I deservioli = Pizza Tower OST (Тема побега на ранг S)
The finale flash of existence = SCP: Secret Laboratory OST
The last of us = The Last of Us (Густаво Сантаолалья)
The only thing that scares me = DOOM Eternal OST (Мик Гордон)
The rebel path = Cyberpunk 2077 OST
The world revolving = Deltarune: Chapter 1 (Тема Джевила)
The zombie threat = Project Zomboid
Tin-tin on the moon = Тинтин на Луне (NES / Чиптюн классика)
Ugh = Friday Night Funkin' (Неделя 7 / Танкмен)
Upgrade station = Team Fortress 2
Victory theme = Слава Колечии!
Vitality = Helltaker OST (Mittsies)
Want you gone = Portal 2 (Финальная песня GLaDOS)
What was lost = Project Zomboid
Whirling in rags, 8AM = Disco Elysium OST (British Sea Power)
Xenophobia = Stellaris (Мемная фанатская песня)
Zombie thread = Project Zomboid
"""

track_list = []
for line in track_list_raw.strip().split("\n"):
    if line.strip():
        # Берем часть после последнего слэша, если он есть
        filename = line.split("\\")[-1] if "\\" in line else line
        # Убираем .mid и лишние пробелы по краям
        clean_track = filename.replace(".mid", "").strip().lower()
        track_list.append((line, clean_track))

# Очищаем мету: берем то, что до знака "="
meta_list = set()
for line in meta_list_raw.strip().split("\n"):
    if line.strip() and "=" in line:
        clean_meta = line.split("=")[0].strip().lower()
        meta_list.add(clean_meta)

# Сравниваем
missing_tracks = []
for original, clean in track_list:
    if clean not in meta_list:
        missing_tracks.append(original)

print(f"Осталось описать треков: {len(missing_tracks)}")
print("--- Список потеряшек: ---")
for track in missing_tracks:
    print(track)
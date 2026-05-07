# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define na = Character("Narrator", what_italic=True)
define mc = Character("You")
define cwc = Character("Cat wearing a strange cap")
define cs = Character("Cat Servant")
define cp = Character("Cat Princess")
define cq = Character("Cat Queen")
define rs = Character("Rat Servant")
define rp = Character("Rat Princess")
define rm = Character("Rat Maid")
define rkn = Character("Rat Knight")
define rk = Character("Rat King")
define gg = Character("Cat guarding the door")
define s = Character("Steve")


# The game starts here.

label start:

    scene bg black screen

    na "You wake up to the sound of meowing. The annoying sun is shining through your closed eyelids, and the grass under your body is making your skin itch - ."

    show bg castle with fade

    menu:
        "Huh?":
            pass

    na "From where you are lying down, you can see a castle in the distance, surrounded by a large city of smaller houses and other buildings. The castle proudly displays a few flags on its stone walls, depicting what looks like… a cat?"

    menu:
        "Wait... Am I still dreaming?":
            pass 

    show cat servant 

    na "Suddenly, a dark figure appears in your line of sight, leaning over your face to get a closer look."

    menu:
        na "Suddenly, a dark figure appears in your line of sight, leaning over your face to get a closer look."
        
        "Sit up calmly.":
            jump scene2

        "AHHHHHHHH!!!!!!":
            jump panic
   

label panic:
    na "You sit up abruptly, slamming your head into the poor cat’s face. The cat stumbles back from the impact, yowling in pain." with vpunch

    show cat servant with hpunch

    cwc "MEOWWWWWW!!!"
    
    mc "AAHHHHHHHH!!!"

    na "The both of you catch your breath, warily staring each other down."
    jump scene2


label scene2:

    na "As you take in the entity in front of you, you realize what you're looking at: A cat wearing what looks like a medieval servant's hat. It's a little ill-fitting on him, as if forced upon him by an overly-adoring owner." 

    menu: 
        na "You reach out to pet the cat."

        "Awwwwww little kitty so cute":
            jump angry
        
        "What the hell are you wearing.":
            jump offended

    
label angry:

    show cat servant with vpunch

    cs "MROWWWWW!!!! Don't touch me!!"

    jump scene3

label offended:
    cs "This is the uniform for those of my station."

    menu:
        "Your... station?":
            pass
    jump scene3
    
label scene3:

    na "The cat sniffs in disdain."

    cs "I am an esteemed servant of the Cat Kingdom, loyal to the Royal Cat Family."

    cs "This hat was bestowed upon me along with my duties when I was first employed in the castle. Do not lay your ugly sausage paws on it."

    menu: 
        "Rude...":
            pass 

    na "Suddenly, something very important occurs to you."

    menu:
        "YOU CAN TALK?":
            pass 

    cs "Of course I can talk, meow! What a rude question. Are all humans as mannerless as you?"

    menu: 
        "Where am I???":
            pass
        "Who are you?????":
            pass
        "How do I get back home???????????":
            pass
    
    cs "Alright, calm down."

    na "The cat peers at you again, scrutinizing your limbs and your ears."

    cs "The Princess had a dream about a human coming to Cat Planet just last night and announced that any humans we found while scavenging for food should be brought back to her."  
    
    cs "Why she would dream about such a clumsy looking animal is beyond me. But perhaps this means that Her Highness can help you get back to wherever you came from."
    
    na "The cat turns, motioning for you to follow him."

    cs "Come on!"

    hide cat servant
    show bg black screen with dissolve
    show bg sewers with fade

    na "The cat servant leads you into a old looking and very stinky sewer. It's hard to believe royalty, much less any self-respecting living being, would choose to reside here."

    menu:
        "This is where the Cat Princess lives?":
            pass

    show cat servant

    cs "Not by choice. Her Highness, the poor young lady, was forced to take refuge here along with the rest of our people."

    cs "The Cats used to live above ground. We were a great nation that lived in great prosperity and harmony! Our enemies, the Rats, lived in the sewers and were very much less successful in, well, everything."

    cs "Naturally, they were very jealous. And one day, they just suddenly attacked our kingdom. They infiltrated the main city through our sewers and potholes. A dishonorable move - as expected of a Rat, mrow!"

    cs "After the Rats took over our kingdom, they left their sewers empty. It was the only place we could hide without them finding us."

    cs "After all, they probably wouldn’t expect us to hide in their old territory! They're not very smart. After all, Cats have always been the superior animals." 

    menu: 
        "(You guys were the ones who got invaded though.)":
            pass

    na "You decide to keep that thought to yourself."
    
    cs "Cats usually hate the sewers. The water gets all in my fur, it smells terrible, and the food is gross, meow. But we have nowhere else to go."

    hide cat servant

    na "You walk for a bit longer, following the cat servant as he navigates the twisting and turning tunnels of the sewers." 
    
    na "Each step you take echoes in the darkness, and the only sound aside from the two of you is the constant dripping of water from some leak in the distance." 

    na "The sewer system seems to be incredibly complicated, and you have a feeling that if you took your eyes off the cat servant for even a second, you would be lost in here forever."
    
    na "After what feels like forever, the cat servant leads you to a giant wooden door with a large banner of a cat on it."

    menu:
        "...This is very conspicuous.": 
            pass

        "LOL I wonder where the cats are hiding.":
            pass

    show cat servant

    na "The cat servant side-eyes you, glaring as much as a cat can glare."

    cs "It would be good for you to hold in this disrespect when we are having an audience with her Highness."

    na "This shuts you up."

    na "The cat servant clears his throat, and begins what seems to be a random bout of mewling, trilling and hissing."

    mc "Um."

    na "At the bottom of the wooden door, a flap you didn't notice beforehand flips open to reveal a pair of narrowed eyes. After a few tense seconds, an approving meow comes from the one guarding the door." 

    hide cat servant 

    show cat soldier 

    gg "Welcome back, Steve."

    menu:
        "Your name is Steve?":
            jump pissed

        "I thought your name was Cat Servant.":
            jump exasperated
    
    hide cat soldier 

label pissed:
    show cat servant at center

    cs "Yes it is. And?"
    jump meetprincess

label exasperated:
    show cat servant at center

    s "You are the stupidest human I've ever met. Not that I've met any before you, so you're doing a terrible job at representing your species."
    jump meetprincess

hide cat knight
hide cat servant

label meetprincess:
    na "The wooden door inches open, and the both of you enter."

    na "The sight that greets your eyes is something you could never have imagined: Hundreds of cats mingling about in the large hall, chatting with each other, drinking, eating and dancing."
    
    na "It's almost as if they weren't a persecuted race of animals, but rather a bunch of cats gathering in some unknown underground hangout."

    na "At the very end of the room, you see a pretty looking cat lounging on a throne on the dais. On her head is some kind of headdress - And from the way that she's leisurely looking out over all the cats in the room, you can tell..."

    menu:
        "Is that the Cat Princess?":
            pass

    show cat servant 

    s "It is indeed. Her Highness has been acting regent ever since her poor mother, Her Majesty the Cat Queen was taken hostage by the horrible Rats."

    mc "I see..."

    hide cat servant

    na "The Cat Princess seems to notice you and the Cat Servant (Steve) enter, and she immediately perks up, suddenly sitting upright on her throne."

    na "The moment she moves, all the cats in the hall stop what they're doing and slowly turn to stare at you. You hear them whispering to each other behind their paws, eyeing you up and down in suspicion."

    
    show cat princess

    cp "Welcome! It's been ages since the Rats took our kingdom and kidnapped our queen. I've prayed everyday for you, our savior, to come rescue us from our plight. What took you so long?"

    menu:
        "Your what now?":
            jump willyou

        "I... Right. I'm your lord and savior.":
            jump pleased


label pleased:
    na "The Cat Princess purrs, satisfied."

    jump demoend

 
label willyou:

    scene bg sewers
    show cat princess

    na "The Cat Princess and all her subjects stare at you impatiently. You can feel the hundreds of eyes on you."

    menu:
        cp "Will you help us?"

        "Of course!":
            jump ofcourse

        "Hell no.":
            jump hellno

label hellno: 

    cp "I see..."
    
    cp "Of course, I totally understand being confused and fearful for your own wellbeing! I would have done the same. However, since you now know where we're hiding, I can’t trust you not to sell us out to the Rats, meow."
    
    cp "GUARDS, GET THEM!!!!!"
    
    show cat knight with hpunch

    na "You try to flee, but the armoured cats are too fast and pounce on you before you can even take a step. As you are mauled to death by feline rage, you wonder if making a different choice could have prevented this…"
    
    hide cat knight 
    show bg black screen 
    with fade
    
    "YOU ARE DEAD."

label deathvoid:
    
    na "How unfortunate."
    
    na "If you choose to do so, I can rewind time and help you prevent this untimely end."
    
    menu: 
        na "Will you reconsider?"
        
        "Yes yes yes please take me back!!!!!":
            na "Don't waste this chance."
            jump willyou
            
        "Absolutely not.":
            na "Alright."
            return 

label ofcourse:
    
    cp "Really??? Thank you, meow!!!"

label demoend:

    hide cat princess
    show cat servant

    s "I knew you were the one!!"

    s "I knew you would be the one to complete the demo!"

    mc "What?"

    na "It seems Steve lied to you about helping you get home. Oh well, you might as well save the cats while you're at it."

    hide cat servant 
    show bg black screen 
    with fade

    "Thanks for finishing the demo lol"

    # This ends the game.

    return

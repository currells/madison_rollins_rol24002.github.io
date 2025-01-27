"""
        Madison Rollins Game Adventure. 

        Half of this story was written by me a LONG time ago but after strugling with the code for AGES
        I decided to use AI to generate some of the endings based on my ideas.  Some are edited some are not :)

        There are 4 endings in total with 9 seperate choices.

        I showed my design to my Grandma and my Bothter and explained how the code works.  My grandma said it 
        gave her a headache to theink about all  of it.  My little brother said it was 'cool' which is high praise 
        coming from him.

"""
print('-----------')
print()
#Title
print('The Gods Tragedienne')
print()
print('-----------')
print()
print()

"""
This is the Prolouge
"""
#p1 diolouge
print("""
        Konstant couldn’t see.  It was as if every light in the cosmos burnt out leaving only the smell of ashes 
    in a damp vat of darkness.  To say he was frightened would be an understatement, he was terrified.  
    Swimming in an inky black pool was not where he imagined his night would go.  
    Thoughts swam through his mind.  “How did I get here?”, “Where am I?”, and “How long have I been here?” 
    were only a few.  He was drowning in the thick star-less void and his own mind.  
      
        “Konstant.”  Came a whisper.

        Konstant froze letting his fears overcome him.
      
        “Konstant Ignatius.”  the voice reapeated with slight shake as though it was cold.
      
        Konstant began to grow more and more afraid.  He couldn’t move, his thoughts set on his inevitable death.
    
        “Die,”  the voice laughed “You are not ready for death child.”
    
        “Dying now would be unfortunate.  The Gods need your help young Konstant.”

	    “The Gods need me?”  Konstant thought.  He couldn't understand why they needed him, afterall, 
    Konstant was an average 16-year-old greek boy.  Standing a few inches above five feet, with olive skin, 
    black hair, and eyes, he fit the very definition of Greek.  The only thing that set him apart was
    his naturally curly hair that stuck out at all sorts of angles.  He was simply unremarkable.

      “Uniqueness,” The voice said as if it could read Konstant’s mind, “does not equate to heroism.”

      Konstant was sure the voice had no idea what they were talking about.  All of the stories he had been told
    of greek heroes involved unique and special children of the gods. Konstant kept thinking 
    “I have no special power nor do I have gifts from gods.”

      “No power from the gods!”  The voice echoed.  Konstant was starting to think the voice could read minds.  
      “You know so little of who you truly are." 
      
      "Now you must choose to accept this path, a DESTINY OF DANGER, or a MUNDANE END."
""")

"""  This is all of the prompts   """


print()
print('-----------')
print()
#opt 1 question
print('Which do you choose a destiny of DANGER or a mundane END?')
print()
#opt 1 input
optI = input('Type your answer here: ')
print()
print('-----------')    
print()

"""
This is all of the if, elif, else statements.
"""



#option 1 if, else  DESTINY OF DANGER
if optI.lower() == "danger":
    print("""
        "You have chosen well..."
        
        The voice echoed its final words before fading into the void surrounding Konstant.  
    The void itself seemed to stretch and bend sucking every last particle of oxygen away 
    from the mortal boy.  He gasped and turned desperately trying to breathe.  
    His eyes wouldn’t open, his body stopped moving, his head stopped thinking.  
    It was as If he was dead.
           

        Konstant awoke in fear.  He was breathing heavily trying to shake the feeling of uneasiness.  
    His dream left him feeling uneasy, with a fervrent desire to visit a small marble shrine deep in the woods.  
        “Konstant,”  His mother yelled from the other side of his small bedroom breking his thoughts. 
    “Hurry and get up the boys are already out in the field.”  
        Quickly, he got up, put on his work clothes, and headed to the field grumbling the whole way.  
    Konstant loathed farm work.  He found no pleasure in the tilling and harvesting of crops, 
    or the picking of grapes to make wine;  the only thing he took pleasure in was fixing the broken tools.  
    Form carts to sicles Konstant could fix it all.  His skills hadn’t gone unnoticed.  Neighbors would 
    search him out to help fix wagons, tools, doors, and anything of the like.
           
        When He arived at the large Barley field he was greated by his father.
        “There you are, Konstant,” Hebdad said. “I've got a job for you.”
        Hebdad was Konstants father, a kind an gentle man, who Konstant admired.  Breifly Konstant 
    wondered if he should SHARE HIS DREAM with his father.
""")
    print('-----------')
    print()
#opt A question
    print('Should Konstant share his dream?')
    print()
#opt 2a input
    optA = input('Type Yes or No: ')
    print()
    print('-----------')
    print()
#opt 1 else MUNDANE END
else:
    print("""
        "So it shall be..."
        
        The voice echoed its final words before fading into the void surrounding Konstant.  
    The void itself seemed to stretch and bend sucking every last particle of oxygen away 
    from the mortal boy.  He gasped and turned desperately trying to breathe.  
    His eyes wouldn’t open, his body stopped moving, his head stopped thinking.  
    It was as If he was dead.
          
    
        Konstant awoke in fear.  He was breathing heavily trying to shake the feeling of uneasiness.  
    His dream left him feeling uneasy, with a fervrent desire to visit a small marble shrine deep in the woods.  
        “Konstant,”  His mother yelled from the other side of his small bedroom breking his thoughts. 
    “Hurry and get up the boys are already out in the field.”  
        Quickly, he got up, put on his work clothes, and headed to the field grumbling the whole way.  
    Konstant loathed farm work.  He found no pleasure in the tilling and harvesting of crops, 
    or the picking of grapes to make wine;  the only thing he took pleasure in was fixing the broken tools.  
    Form carts to sicles Konstant could fix it all.  His skills hadn’t gone unnoticed.  Neighbors would 
    search him out to help fix wagons, tools, doors, and anything of the like.
        
          As expected The sun beat down on Konstant's back as he bent over, his hands gnarled and calloused from
    hours of toil. The rich, earthy scent of freshly turned soil filled his nostrils. He had spent the morning tending 
    to the vegetable patch, weeding the rows of tomatoes, peppers, and cucumbers. The afternoon was reserved for the 
    livestock - a herd of cows that needed milking and a small flock of chickens that required daily feeding and egg collection.

        The work was physically demanding, yet for the first time Konstant found a strange sort of satisfaction in it. 
    There was a rhythm to the labor, a connection to the land and its cycles. As he worked, his mind would wander, contemplating
    the vastness of the universe and the smallness of his existence. Yet, in this simple act of tending to the earth, he felt a 
    profound sense of purpose.
        Konstant returned home as the sun dipped below the horizon, casting long shadows across the quiet feilds. Konstant stood at 
    the window, his reflection a stark silhouette against the twilight. He had spent countless hours contemplating the extraordinary, 
    the infinite possibilities of the universe. But now, as he gazed out at the ordinary world, a strange sense of peace 
    washed over him.
        He thought of his life, a series of mundane moments strung together. The daily commute, the repetitive tasks, the familiar
    faces. It was a life far removed from the cosmic wonders he had once dreamed of. Yet, in this very ordinariness, he found a 
    profound beauty.
        A gentle smile crept across his lips. Perhaps the extraordinary wasn't found in distant galaxies or supernatural occurrences, 
    but in the quiet moments of human existence. The love shared between friends and family, the small acts of kindness, the simple 
    joy of a warm meal. These were the true wonders of the universe.
        With a newfound acceptance, Konstant turned away from the window. He would embrace the mundane, not as a limitation, but as an 
    opportunity. He would find meaning in the everyday, and in doing so, discover the extraordinary within the ordinary.

          Ending Unlocked: True Freedom!.....At least for now.
""")
    
#DOES NOT SHARE HIS DREAM   2b
if optA.lower() =='no':
    print("""
     Having made his choice, Konstant was on the road to Itea, the nearest town, to help an old family friend,
Mr. Ganes, with a few repairs.  Konstant had never met him, but he was to spend the night at his home.


    Konstant walked a few miles down the dusty road.  He had packed his sandals, some lamb jerky,
a cloth of cheese and olives, and his himation in a small bag made of sheep leather.  He should have
strode confidently, having traveled the road on foot many times before, although this time Konstant grew
anxious with every step he made away from the safety of his home.  There was a sinking feeling that he had
felt in the void except it was tantalizing.  He wanted to find the source of this feeling, everything else
was irrelevant.  He walked entranced by the feeling into the thick dense forest of cypress and oak.  
    Branches scraped against his body creating new noticeable scratches and tears in both flesh and cloth
but he could not feel them.  All he could feel was the enthralling feeling of doom.  The forest seemed
immobile as if everything in the world had stopped to let him pursue the strange emotion.  
    Konstant happened to be walking toward the very hill he remembered in his dream.  On top of that hill
stood a small marble edifice that resembled the Acropolis of Athens.  Gold and silver murals glistened in
the sunlight bathing the temple and the hill in angelic light that would blind anyone who beheld it.  
    He kept walking up the hill and onto the steps of the temple.  No one was there.  Konstant found that
incredibly odd because temples were almost always bustling with visitors who came to worship the gods.  
He crept forward trying to see what was going on inside of the temple.  The marble walls were covered in
depictions of the Titans.  Above the entrance to the shrine was a beautiful ornate carving cast in gold
that depicted Kronos swallowing his children.  Konstant felt odd staring at the image glorifying Cronus’s
terrible deed.  To the sides were pillars of marble with veins of gold and silver that rested upon the backs
of two large serpents whose Jaws were open wide as if stopped mid-hunt.  A cool breeze blew from the open
doorway and gave Konstant a shiver that ran from his head to his toes.  Fear itched his bones and he felt like
running, yet, the engravings were drawing him closer, begging him to reach out and feel the cold stone. 
""")
    print()
    print('-----------')
    print()
#opt 3a question
    print('Should Konstant TOUCH the Carving or should he RUN away?')
    print()
#opt 3a input
    optAB = input('Type your choice here: ')
    print()
    print('-----------')
    print()

#If stone touch
    if optAB.lower() == 'touch':
        print("""
            Drawn by the dark glimmer of the snake's emerald eyes, Konstant reached out to touch its cold, smooth
        scales. As his fingertips brushed against the serpent's head, a surge of energy coursed through him, and a 
        vision unfolded before his mind's eye.
            He saw a world ravaged by darkness, a world on the brink of destruction. And he saw himself, a figure of
        light, standing against the encroaching shadows. A sense of power, a power he had never known, surged within him.
            When the vision faded, Konstant pulled his hand away from the serpent, his heart pounding. He had been 
        chosen, marked by the gods for a great destiny. But with this newfound power came a heavy burden.  He was no
        longer just a simple farm boy; the gods would make him a guardian of light, a protector of humanity. His 
        journey had just begun, and the fate of the world rested in his hands.
            As he left the temple Konstant's mind was racing, he was left with two choices: embrace his role as a hero
        and confront the darkness, or let the darkness consume the world.

              Ending Unlocked: CONFUSION
        """)
    

#SHARE HIS DREAM
else:
    print("""
    Konstant hesitated, his heart pounding in his chest. He had never shared such a strange and unsettling dream with anyone before. 
    Yet, there was something about his father that made him feel he could confide in him. Taking a deep breath, he began to speak.
    “Father, I had a strange dream last night,” he started, his voice barely a whisper. “I was in a dark place, a void, and a voice spoke 
to me. It said that the gods need my help.”
    Hebdad listened intently, his expression turning thoughtful. He knew his son was a quiet boy, often lost in his thoughts. But this was
different. This was a revelation, a calling, perhaps.
    “A dream, you say?” Hebdad mused. “Well, dreams can be mysterious things, Konstant. They can sometimes reveal hidden truths or future 
possibilities. Perhaps the gods do have a plan for you.”
    Konstant was surprised by his father’s reaction. He had expected skepticism or dismissal, but instead, he found understanding.
    “But Father, I’m just a simple farm boy. I have no special powers or abilities,” Konstant confessed, feeling a wave of self-doubt.
    Hebdad smiled warmly. “Remember, my son, even the greatest heroes were once ordinary people. It is often those who are humble and 
unassuming who are chosen for great things. Perhaps the gods see something in you that we cannot.”
    Konstant was touched by his father’s words. He felt a sense of hope and purpose that he had never experienced before.
    “Thank you, Father,” he said, his voice filled with gratitude. “I will think about what you’ve said.”
    As Konstant returned to his work, he couldn’t shake the feeling that his life was about to change forever. The dream, the voice, and 
his father’s words had ignited a spark within him, a spark that would soon set his destiny in motion. He pondered his options: should he 
travel to the mysterious temple, consult the enigmatic Oracle of Delphi, or run away from the responsibility?

    The choice was his, and the fate of the world might depend on his choice.
""")   
    print()
    print('-----------')
    print()
#opt 3a question
    print('Should Konstant find the TEMPLE, visit the ORACLE, or RUN away from his fate?')
    print()
#opt 3a input
    optAA = input('Type your choice here: ')
    print()
    print('-----------')
    print()


if optAA.lower() == 'temple':
    print("""
     Having made his choice, Konstant was on the road to Itea, the nearest town, to help an old family friend,
Mr. Ganes, with a few repairs.  Konstant had never met him, but he was to spend the night at his home.


    Konstant walked a few miles down the dusty road.  He had packed his sandals, some lamb jerky,
a cloth of cheese and olives, and his himation in a small bag made of sheep leather.  He should have
strode confidently, having traveled the road on foot many times before, although this time Konstant grew
anxious with every step he made away from the safety of his home.  There was a sinking feeling that he had
felt in the void except it was tantalizing.  He wanted to find the source of this feeling, everything else
was irrelevant.  He walked entranced by the feeling into the thick dense forest of cypress and oak.  
    Branches scraped against his body creating new noticeable scratches and tears in both flesh and cloth
but he could not feel them.  All he could feel was the enthralling feeling of doom.  The forest seemed
immobile as if everything in the world had stopped to let him pursue the strange emotion.  
    Konstant happened to be walking toward the very hill he remembered in his dream.  On top of that hill
stood a small marble edifice that resembled the Acropolis of Athens.  Gold and silver murals glistened in
the sunlight bathing the temple and the hill in angelic light that would blind anyone who beheld it.  
    He kept walking up the hill and onto the steps of the temple.  No one was there.  Konstant found that
incredibly odd because temples were almost always bustling with visitors who came to worship the gods.  
He crept forward trying to see what was going on inside of the temple.  The marble walls were covered in
depictions of the Titans.  Above the entrance to the shrine was a beautiful ornate carving cast in gold
that depicted Kronos swallowing his children.  Konstant felt odd staring at the image glorifying Cronus’s
terrible deed.  To the sides were pillars of marble with veins of gold and silver that rested upon the backs
of two large serpents whose Jaws were open wide as if stopped mid-hunt.  A cool breeze blew from the open
doorway and gave Konstant a shiver that ran from his head to his toes.  Fear itched his bones and he felt like
running, yet, the engravings were drawing him closer, begging him to reach out and feel the cold stone. 
""")
    print()
    print('-----------')
    print()
#opt 3a question
    print('Should Konstant TOUCH the Carving or should he RUN away?')
    print()
#opt 3a input
    optAB = input('Type your choice here: ')
    print()
    print('-----------')
    print()

elif optAA.lower() or optAB.lower() == 'run':
    print("""
    Fear gripped Konstant as his thoughts turned to the disturbing voice in his dream. The weight of the unknown, 
his duties, his parent's expectation, and he couldn't help but feel as though someone or something was watching him.
It was too much to bear. He turned and fled, his heart pounding in his chest.
    As he ran, the world around him began to distort, the colors fading into a monochromatic blur. A chilling voice 
echoed in his mind. 
    "You have failed, Konstant. You have turned away from your destiny."
    Panic surged through him as he found himself back in the inky blackness of his dream. The voice, cold and 
unforgiving, continued. 
    "You were given a chance, a chance to rise above the ordinary. But you chose fear over courage."
    A sense of dread washed over him as the darkness closed in. He struggled against the suffocating void, but it was 
futile. The darkness consumed him, leaving behind only an echo of his once hopeful spirit.
    
Konstant's story ended not with glory and triumph, but with the chilling realization of a life unfulfilled, ac destiny denied.
	
          Ending Unlocked:  You can not run away from the God’s

""")
else:
    print("""
    Konstant's heart pounded in his chest as he made his decision. The voice in his dream, the enigmatic words of 
the Oracle, and the stirring within his own soul pulled him towards a path unknown. He would seek the Oracle's 
counsel, no matter the cost.

With a heavy heart, he bid farewell to his family, explaining his unusual dream and his intention to visit the 
Oracle. His parents, though concerned, respected his decision. His father, with a knowing look, offered him a small
pouch filled with gold coins and a heartfelt blessing.

The journey to Delphi was arduous. Konstant traversed treacherous mountain paths, crossed raging rivers, and endured
the scorching sun. But with each step, his determination grew stronger. He was no longer just a simple farm boy; he 
was a seeker of truth, a potential hero.

Upon reaching the sacred site of Delphi, he was awestruck by its grandeur. The towering cliffs, the ancient ruins, 
and the serene atmosphere filled him with a sense of reverence. He ascended the winding path to the Oracle's temple,
 his heart filled with anticipation and trepidation.

Inside the temple, the air was thick with incense and the low murmur of prayers. He approached the Pythia, the Oracle's
priestess, who sat on a tripod, her face obscured by a veil. As she uttered her prophetic words, Konstant listened 
intently, his mind racing.

The Oracle's prophecy was cryptic and enigmatic, filled with symbols and riddles. It spoke of a great darkness looming 
over the land, a threat that only a chosen one could defeat. The prophecy hinted at a hidden power within Konstant, a 
power that could save the world.

With a newfound purpose, Konstant left Delphi, his heart heavy with responsibility. He knew that his journey had just
begun. The road ahead was uncertain, but he was ready to face whatever challenges lay in wait. His destiny, it seemed, 
was intertwined with the fate of the world.
          
        ENDING UNLOCKED: A NEW START
""")
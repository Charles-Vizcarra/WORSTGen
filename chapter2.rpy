label chapter2:
    hide screen objective_text
    show screen chapter_title_text("Chapter 2: The Fool")
    pause 3.0
    hide screen chapter_title_text

    Ethan "Another floor..."
    Ethan "That key card was just for one floor above? "
    Ethan "...but I have to keep moving... even if every part of me wants to turn back."
    Ethan "I swear, this place will make me go insane."

    "rummaging sfx loop"

    Ethan "What's that noise?"
    Ethan "It's coming from that room..."
    Ethan "Is someone there?"
    Ethan "They might be able to help me find the way out."
    "You reached out for the door knob, but..."
    Ethan "Wait... what if they're... dangerous?"
    Ethan "I have to be careful."
    "stop rummaging sfx"
    Ethan "It stopped..."
    Ethan "Did they hear me?"
    "fast hearbeat sfx"
    "door opening sfx"

    scene bg darkroom with fade
    Noah "Ethan?!"
    Ethan "No... Noah? But you..."
    Noah "Dude! It's been forever!"
    Noah "What's it been—like a year? Two?"
    Noah "Man, I can't tell you how good it feels to see a familiar face in a place like this!"
    Ethan "Ye… Yeah."
    Noah "What's up? You look pale."
    Ethan "N-no, it's nothing. Its just… this place is… insane."
    Ethan "How did you even get here?"
    Noah "I honestly have no clue. I just woke up in this room. "
    Noah "The last thing I remember… I was in bed, trying to sleep. My parents were fighting again—screaming at each other. Couldn't shut it out."
    Ethan "I guess were in the same boat. I woke up one floor below this one."
    Ethan "The last thing I remember is that I was going out to grab some food. Then… I saw a bright light and suddenly… I was here."
    Noah "...So what, you think we got kidnapped or something?"
    Ethan "I don't know. But whatever this place is—it's crazy. We have to get out of here as soon as possible."
    
    Ethan "...Hey, this room…"
    Ethan "Don't you think it looks like Genesis? You know, the old studio we used to practice at?"
    Noah "...Whoa. Now that you mention it—Yeah. Damn, dude, it really does."
    Noah "This feels nostalgic, but creepy as hell at the same time."
    Ethan "It is. This whole facility IS creepy."
    Ethan "...Come on. Lets go check the other rooms."

    jump f2_p1

label elevator2:
    scene black with fade
    if not key_card2_acquired:
        "Access Denied. F2 Key Card Required."
        Ethan "I need the key card."
    elif not objective_go_elevator2:
        Ethan "I need to find Noah first."
    else:
        hide screen objective_text
        "You ran towards the elevator, desperately trying to escape the scene..."
        Ethan "Please... let me out... let me out..."
        jump chapter3

label f2_p1:
    if not from_locked_room:
        scene bg f2p1 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        Ethan "The elevator..."

    $ from_locked_room = False

    if not objective_find_main_key_shown:
        Ethan "We need to get out of here, but there's no exit below. Someone wrote on the walls that the only way is up."
        Ethan "For that, we need to access the elevator. If this plays out like it did for me earlier, we'll need a key card to use it."
        Ethan "But before that, we need to find the key to the main room or something. I'm guessing that's where the key card is."
        Noah "Gotcha."
        call screen objective_text(chap2_objective_find_main_key)
        show screen objective_text(chap2_objective_find_main_key, 0.98, 0.1)
        $ objective_find_main_key_shown = True

    call set_back_btn_clicked(False)
    while True:
        show screen f2_p1_buttons
        pause

label f2_p2:
    if not from_locked_room:
        scene bg f2p2 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        Ethan "Hurry..."
    
    $ from_locked_room = False
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p2_buttons
        pause
    jump f2_p1

label f2_p3:
    if not from_locked_room:
        scene bg f2p3 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        Ethan "Please... Let me get out of here..."
    $ from_locked_room = False
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p3_buttons
        pause
    jump f2_p2

label f2_p4:
    if not from_locked_room:
        scene bg f2p4 with fade

    if objective_go_elevator2 and not from_locked_room:
        Ethan "No... Noah..."
    $ from_locked_room = False
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p4_buttons
        pause
    jump f2_p3

label f2_p5:
    if not from_locked_room:
        scene bg f2p5 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        Ethan "W-why is this happening to me?"
    $ from_locked_room = False
    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p5_buttons
        pause
    jump f2_p4

label f2_p6:
    if not from_locked_room:
        scene bg f2p6 with fade
    
    if objective_go_elevator2 and not from_locked_room:
        Ethan "Please let me out of here..."

    $ from_locked_room = False

    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen f2_p6_buttons
        pause
    jump f2_p5

label room201:
    if objective_go_elevator2:
        Ethan "I don't have time for this..."
        $ from_locked_room = True
        window hide
        jump f2_p1
    scene bg darkroom with fade

    if objective_find_noah:
        Ethan "He's not here..."
        
    else:
        Ethan "It's scary how accurate this room is to the real thing."
        Noah "Yeah... even the guitars, drumset, and keyboard—this place is messing with us."

    call set_back_btn_clicked(False)
    show screen back_btn
    while not back_btn_clicked:
        pause
    
    hide screen back_btn
    jump f2_p1

label room202:
    if objective_go_elevator2:
        Ethan "I don't have time for this..."
        $ from_locked_room = True
        window hide
        jump f2_p3
    
    scene bg darkroom with fade

    if objective_find_noah or main_key2_acquired or ladder_acquired:
        if objective_find_noah:
            Ethan "He's not here..."
        elif main_key2_acquired:
            Ethan "Nothing much to do here. We already got the key."
        elif ladder_acquired:
            Ethan "We already got the ladder. Let's go back to your room."
            Noah "Yeah, that's definitely tall enough."
        call set_back_btn_clicked(False)
        show screen back_btn
        while not back_btn_clicked:
            pause
        hide screen back_btn
        jump f2_p3
    if not find_tall_evt_flag:
        show screen ladder_inactive
        Ethan "…This time, it's our old classroom. Back in high school."
        Noah "There's no way this is a coincidence. This place… it's like it's digging into our memories on purpose."
        Noah "It {i}wants{i} to mess with us."

    else:
        show screen ladder_active
        Ethan "These school chairs won't help us much. We need something taller."

    call set_back_btn_clicked(False)
    call set_ladder_clicked(False)
    
    while not back_btn_clicked and not ladder_acquired:
        show screen back_btn
        if not ladder_acquired and ladder_clicked and find_tall_evt_flag:
            Noah "There! We can use that ladder."
            Ethan "That's perfect. Let's take it back to my room."
            $ ladder_acquired = True
            hide screen ladder_active
            call screen objective_text(chap2_objective_go_dorm_room)
            show screen objective_text(chap2_objective_go_dorm_room, 0.98, 0.1)
        pause
        
    hide screen back_btn
    hide screen ladder_active
    hide screen ladder_inactive
    
    jump f2_p3

label room20X:
    "door locked sfx"
    if objective_go_elevator2:
        Ethan "I don't have time for this..."
    else:
        Ethan "It's locked. I wonder what's inside..."
    $ from_locked_room = True
    window hide
    jump f2_p4

label room203:
    if objective_go_elevator2:
        Ethan "I don't have time for this..."
        $ from_locked_room = True
        window hide
        jump f2_p5

    if not (objective_find_noah and not noah_revelation_done):
        scene bg darkroom with fade
    if not find_tall_evt_flag:
        Noah "Dude! This is…"
        Ethan "Your dorm room."
        Noah "No way… This is insane. Why does this place look exactly like my dorm? Down to the mess on the desk, even?"
        Ethan "I told you—this place is crazy. Logic doesn't belong here."
        Ethan "...I've only been in your dorm once, but it stuck with me so much that I still remember exactly what it looks like. "

        Noah "Wait… look up. Hey, is that the key you were talking about?"
        Noah "It's just hanging over there on the ceiling."
        Ethan "Yeah, I think that's it."
        Ethan "Tch, too high though. We need something tall to stand on."

        Noah "This desk won't do it for sure, even the chair. We need something taller."
        Noah "Hmm... there's nothing useful here. Let's check the other rooms. There's gotta be something." 

        call screen objective_text(chap2_objective_find_tall)
        show screen objective_text(chap2_objective_find_tall, 0.98, 0.1)
        $ find_tall_evt_flag = True

    if objective_find_noah or main_key2_acquired or ladder_acquired:
        if objective_find_noah:
            jump Noah_revelation

        elif main_key2_acquired:
            Ethan "We already got the key. Let's go to the main room."
        
        elif ladder_acquired:
            call room203_cutscene
    
    else:  
        Noah "We still need to find something taller than a chair or a desk."

    call set_back_btn_clicked(False)
    while not back_btn_clicked:
        show screen back_btn
        pause
    
    hide screen back_btn
    jump f2_p5

label room203_cutscene:
    "GETTING THE MAIN KEY USING THE LADDER CUTSCENE"

    Noah "Got it! Let's move on."
    Ethan "Ye... yeah, let's go."
    call screen objective_text(chap2_objective_go_main_room)
    show screen objective_text(chap2_objective_go_main_room, 0.98, 0.1)
    $ main_key2_acquired = True
    return

label Noah_revelation:
    hide screen objective_text
    scene black with fade
    Ethan "Noah? Are you there?"
    "(cutscene)"
    "(door opening sfx)"
    "(background Best Friend hanged on the ceiling, dead)"
    "(horror shock sfx)"
    "(voice acting NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO"
    "(end cutscene)"

    Ethan "I… I knew it."
    Ethan "I knew this place wasn't kind enough to just let me relive our high school memories."
    Ethan "The moment I saw him on this floor… I knew."
    "(quick flashback to \"Noah? But you…\" line)"
    Ethan "I knew I wasn't allowed to be happy. Not after everything I've done."
    Ethan "Noah... took his life a year ago."
    Ethan "He never told me the full story—only that things at home were falling apart."
    Ethan "His parents were fighting. The house itself felt like it was crumbling."
    Ethan "And he was stuck in the middle."

    Ethan "He left their house… and started staying in a dormitory. "
    Ethan "He stopped going to school…"
    Ethan "I thought it was just another rough patch… something he'd laugh off the next day."
    Ethan "...But he didn't."
    Ethan "After a week, I tried to visit him at his place..."
    Ethan "...then I saw... {b}this{/b}."

    Ethan "I should've noticed."
    Ethan "The way he forced his smile."
    Ethan "The way his eyes always looked tired, even when he swore he was fine."
    Ethan "I should've asked. I should've stayed. I should've done something."
    Ethan "...But I didn't."
    Ethan "I was too busy. Too wrapped up in my own world. Too blind to see he was drowning."
    Ethan "And now—he's gone."

    "(lines with voice acting), angry at self"
    Ethan "He needed me, and I WASN'T THERE!"
    Ethan "DON'T TELL ME IT WASN'T MY FAULT—"
    Ethan "BECAUSE IT IS!"
    Ethan "DON'T TELL ME THERE WAS NOTHING I COULD'VE DONE—"
    Ethan "BECAUSE THERE WAS!"
    Ethan "I WAS THE CLOSEST PERSON TO HIM!"
    Ethan "I SHOULD'VE SAVED HIM!"
    Ethan "I'M THE ONE TO BLAME!"
    "(pause, anger breaking down into grief)"
    Ethan "I... I didn't even go to his funeral..."
    Ethan "...couldn't even talk to his family."
    Ethan "I had no right."
    Ethan "I... I didn't do anything for him."

    $ Noah_revelation_done = True
    call screen objective_text(chap2_objective_go_elevator)
    show screen objective_text(chap2_objective_go_elevator, 0.98, 0.1)
    $ objective_go_elevator2 = True
    jump f2_p5

label main_room2:
    if objective_go_elevator2:
        Ethan "I don't have time for this..."
        $ from_locked_room = True
        window hide
        jump f2_p6
    if not main_key2_acquired:
        "door locked sfx"
        $ from_locked_room = True
        Noah "You're right—it's locked."
        Ethan "Yeah, this is the main room. There's one just like this before."
        Ethan "We need the key."
        window hide
        jump f2_p6

    if not past_travel_done:
        hide screen objective_text
        scene black with fade
        "door unlocking sfx"
        Ethan "I'll go first."
        "You slowly entered the main room..."
        "SLAM!"
        "The door crashed shut behind you, echoing through the room."
        scene bg f2p6 with fade
        Noah "Ethan! Are you good?"
        Ethan "Yeah, I'm fine!"
        Ethan "...but the door's stuck."
        Noah "That's fine. Can you see the key card?"
        Ethan "Yeah, it's here!"
        Noah "Just grab the card. I'll find a way to open the door."

        scene bg darkroom with fade
        Ethan "I see it… the key card."
        Ethan "But… am I really going to go through that nightmare again?"
        Ethan "I-I'm scared. But if we ever want to get out of here…"

        show screen f2_keycard
        call set_keycard_clicked(False)
        while not keycard_clicked:
            "Take the Key Card"
        
        hide screen f2_keycard
        hide screen objective_text
        jump past_travel

    else: # past travel done
        if not objective_find_noah:
            scene bg darkroom with Fade(1.0, 1.0, 1.0, color="#fff")
            Ethan "I-I'm... back?"  
            Ethan "That's it? It's over?"  
            Ethan "Hah... maybe it wasn't as bad as I thought."
            Ethan "I got the key card for the elevator."
            "Key Card Acquired."
            $ key_card2_acquired = True
            Ethan "I need to find Noah. He's probably worried sick."  
            "Your eyes fall on the door—left wide open."
            Ethan "Wait... the door's wide open."  
            Ethan "Did he manage to unlock it while I was out?"  
            Ethan "But... where did he go?"  

            call screen objective_text(chap2_objective_find_noah)
            show screen objective_text(chap2_objective_find_noah, 0.98, 0.1)
            $ objective_find_noah = True

        else:
            scene bg darkroom with fade
            Ethan "I need to find Noah."

        jump f2_p6

label past_travel:
    Ethan "P-please... don't make me see {i}that{/i} again—"

    scene black with Fade(1.0, 1.0, 1.0, color="#fff")
    scene white with fade
    Ethan "Ah, too bright"
    scene bg_run with fade
    Ethan "Where am I?"
    scene ethan_running2 with fade
    Ethan "Is this outside?"
    Ethan "We're running?"
    scene black with fade
    pause 0.5
    scene ethannoah_running with fade
    Noah "DUDE, STOP DAYDREAMING! WE'RE RUNNING LATE"
    Ethan "What?!"
    scene ethannoah_running2 with fade
    Ethan "Noah, I thought you couldn't enter the room.. Thank God you're here"
    Noah "Uhh, room? What are you talking about? Dude, are you still asleep?"
   
    play sound "smack.ogg"
    "*SMACK*"
    scene black
    pause 1.0

    scene bg_run
    show ethan_smacked_unif at left
    "A dull thud of pain spreads across your back"
    show noah_laughing at right with fade
    Noah "HAHAHA! Did that wake you up?"
    hide noah_laughing
    show noah_leftlook at right
    Ethan "..."
    hide ethan_smacked_unif
    hide noah_laughing
    hide noah_leftlook
    show ethan_confused_unif at center with dissolve
    "Ethan's inner thoughts"
    Ethan "No, he's not the one I was with in the facility"
    Ethan "..."
    Ethan "I guess he's the Noah of this time. I'm back in our high school days"
    
    scene black with fade
    pause 1.0

    Noah "JUST FIVE MRORE MINUTES! DUDE, HURRY UP!"

    scene black with fade
    pause 1.0

    jump classroom

label classroom:
    scene classroom2 with fade
    pause 2.0
    scene classroom1 with fade
    show ethan_observing at center with dissolve
    show ethan_observing at left with move
    Ethan "We just attended the lecture for the first period. Nothing strange has happened yet." 
    hide ethan_observing
    show ethan_default_unif at left
    show noah_bored at right with dissolve
    Noah "Ughh, that was boring. Why do we gotta learn about a bunch of dead guys?"
    Noah "They're not coming back anyway"
    hide ethan_default_unif
    show ethan_talking at left
    Ethan "Maybe, but it's still important"
    hide noah_bored
    show noah_talking at right
    Ethan "The world is messed up-or not messed up-because of what they all did back then."
    Noah "Yeah, but it's boring right?"
    hide noah_talking
    show noah_leftlook at right
    Ethan "It sure is, Noah"
    hide noah_leftlook
    hide ethan_talking
    show ethan_laughing at left
    show noah_laughing at right
    Ethan "HAHAHA."
    hide noah_laughing
    hide ethan_laughing

    scene black with fade
    jump musicclubroom
label musicclubroom:
    scene afterschool with fade
    "Ethan's inner thoughts."   
    Ethan "After class, we met with our bandmates and went to this music studio near our school." 
    scene music_studio with fade 
    Ethan "I play the guitar. Noah's our vocalist. He goes absolutely crazy at the mic."
    scene black with fade
    pause 1.0

    scene bg_arcade
    "transition to arcade"
    Ethan "After that, we went to the arcade."
    hide ethan_talking
    scene playarc with fade
    show ethan_laughing at left with dissolve
    Ethan "This guy really sucks at video games, but he's fun to play with."
    scene playarc2
    hide ethan_laughing

    scene black with fade
    pause 1.0 

    scene bg_house with fade
    "transition to house"
    show ethan_observing at right with dissolve
    Ethan "Then, we went to his house to play this murder mystery visual novel about a group of extraordinary high school kids killing each other."
    hide ethan_observing
    show vn_closeup at center with dissolve
    Ethan "I really liked this VN series"
    hide vn_closeup
    scene play2 with fade
    "(Ethan and Noah): Whaaaat???"
    pause 5.0
    scene play
    pause 5.0
    scene bg_house with fade
    show ethan_default_unif at right with dissolve
    Ethan "This was our usual routine."
    Ethan "Go to school, hang out with our band, play at the arcade or at the basketball court, then play some more at his house."
    hide ethan_default_unif
    scene black
    pause 0.5
    Ethan "I missed this" 
    show ethan_default_unif at center with dissolve
    pause 2.0
    hide ethan_default_unif
    show ethan_dismayed2 at center
    Ethan "..."
    Ethan "But..."
    hide ethan_dismayed2
    show ethan_dismayed
    pause 1.0
    hide ethan_dismayed
    show ethan_closeup with move
    Ethan "Am I allowed to have this much fun?"

    scene white with fade

    jump music_club_darkened

label music_club_darkened:

    show classroom1blurr with fade
    play sound "sfx_distant_echo.ogg" loop
    
    show ethan_confused_unif2 at center
    Ethan "Huh… did I just hear something…?"
    scene black 
    hide ethan_confused_unif2
    Noah "Huh? What's wrong? You look weird."
    show ethan_scaredlook2
    "inner thoughts ni Ethan"
    Ethan "(No, he can't hear this. Not here.)"
    hide ethan_scaredlook2
    show ethan_scaredlook
    Ethan "(It's… that place. That facility… it's calling me again.)"

    pause 1.0
    scene bg black with fade
    stop sound
    $ past_travel_done = True
    jump main_room2
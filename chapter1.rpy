label chapter1:
    scene black with fade
    play music ("her.mp3")
    show screen chapter_title_text("Chapter 1: Shadows Ahead")
    pause 3.0
    hide screen chapter_title_text

    call screen objective_text(chap0_objective_find_clues)
    show screen objective_text(chap0_objective_find_clues, 0.98, 0.1)

    jump f1_p1

label elevator1:
    scene black with fade
    if not key_card1_acquired:
        "Access Denied. F1 Key Card Required."
        Ethan "I need the Key Card."
    
    else:
        "Elevator door opening..."
        jump chapter2

label f1_p1:
    scene bg f1p1 with fade
    
    while True:
        if pieces_count == 9 and not all_pieces_obtained:
            $ all_pieces_obtained = True
            call screen objective_text(chap1_objective_go_puzzle_room)
            show screen objective_text(chap1_objective_go_puzzle_room, 0.98, 0.1)

        call set_back_btn_clicked(False)
        call set_puzzle_missing_pieces_clicked(False)

        show screen f1_p1_buttons
        pause

    return

label f1_p2:
    if not from_locked_room:
        scene bg f1p2 with fade
        
    $ from_locked_room = False
    while True:
        if pieces_count == 9 and not all_pieces_obtained:
            $ all_pieces_obtained = True
            call screen objective_text(chap1_objective_go_puzzle_room)
            show screen objective_text(chap1_objective_go_puzzle_room, 0.98, 0.1)

        call set_back_btn_clicked(False)
        call set_puzzle_missing_pieces_clicked(False)

        show screen f1_p2_buttons
        pause

    return

label f1_p3:
    scene bg f1p3 with fade
    
    while True:
        if pieces_count == 9 and not all_pieces_obtained:
            $ all_pieces_obtained = True
            call screen objective_text(chap1_objective_go_puzzle_room)
            show screen objective_text(chap1_objective_go_puzzle_room, 0.98, 0.1)

        call set_back_btn_clicked(False)
        call set_puzzle_missing_pieces_clicked(False)

        show screen f1_p3_buttons
        pause

    return

label f1_p4:
    scene bg f1p4 with fade
    
    while True:
        if pieces_count == 9 and not all_pieces_obtained:
            $ all_pieces_obtained = True
            call screen objective_text(chap1_objective_go_puzzle_room)
            show screen objective_text(chap1_objective_go_puzzle_room, 0.98, 0.1)

        call set_back_btn_clicked(False)
        call set_puzzle_missing_pieces_clicked(False)

        show screen f1_p4_buttons
        pause

    return

label room101:
    scene bg darkroom with fade

    Ethan "This is where I woke up."
    Ethan "Nothing's here—just a bed and a table with a bunch of random junk on top of it."

    while not back_btn_clicked:
        show screen back_btn
        if not room101_pieces_taken:
            show screen puzzle_missing_pieces("101")

            if puzzle_missing_pieces_clicked: # piece-2, 4, 9
                hide screen puzzle_missing_pieces
                show screen puzzle_missing_pieces_zoomed("101")
                if puzzle_evt_flag:
                    Ethan "Found the pieces."

                elif pieces_count <= 0:
                    Ethan "Are these puzzle pieces?"

                else:
                    Ethan "Again? What are these pieces for?"

                menu: 
                    "Take the pieces?"
                    "Yes":
                        Ethan "I'll take them."
                        $ pieces_count += 3
                        $ room101_pieces_taken = True
    
                        if puzzle_evt_flag:
                            Ethan "I got [pieces_count] of these pieces now."
                            show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
                    "No":
                        Ethan "I'll leave them here."
                        hide screen puzzle_missing_pieces_zoomed

        pause
    
    hide back_btn
    hide screen puzzle_missing_pieces
    hide screen puzzle_missing_pieces_zoomed
    
    jump f1_p1

label room102:
    if all_pieces_obtained:
        jump puzzle_mini_game

    scene bg darkroom with fade

    if puzzle_evt_flag:
        show haru default at left with dissolve
        Ethan "I have to look for the puzzle pieces."
        Ethan "...the other rooms, maybe?"
    
    else:
        show haru default at left with dissolve
        Ethan "This place is packed."
        Ethan "...it's like someone dumped an entire storage unit in here."
        Ethan "Where do I even start looking?"
        Ethan "Wait... something's written on the wall."
        Ethan "\"Assemble the pieces\"?"

        call screen objective_text(chap1_objective_puzzle_evt)
        $ puzzle_evt_flag = True

        show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)

        Ethan "A jigsaw puzzle? Seriously?"
        Ethan "Ugh, but it's the only lead I've got."
        Ethan "...fine."
    
    while not back_btn_clicked:
        show screen back_btn
        pause
    
    jump f1_p1

label room103:
    scene bg darkroom with fade

    Ethan "This room looks like an office… maybe for some kind of company."
    Ethan "...It doesn't feel like anyone's worked here in years."
    
    while not back_btn_clicked:
        show screen back_btn
        if not room103_pieces_taken: 
            show screen puzzle_missing_pieces("103")

            if puzzle_missing_pieces_clicked: # piece 6, 8
                Ethan "...Wait, what's that under the chair?"
                hide screen puzzle_missing_pieces
                show screen puzzle_missing_pieces_zoomed("103")
                if puzzle_evt_flag:
                    Ethan "Found them."

                elif pieces_count <= 0:
                    Ethan "Are these puzzle pieces?"

                else:
                    Ethan "Another set of pieces? What are these for?"

                menu: 
                    "Take the pieces?"
                    "Yes":
                        Ethan "Yeah, I better take these pieces."
                        $ pieces_count += 2
                        $ room103_pieces_taken = True
    
                        if puzzle_evt_flag:
                            Ethan "I got [pieces_count] of them now."
                            show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
                    "No":
                        Ethan "I'll leave them here."
                        hide screen puzzle_missing_pieces_zoomed

        pause
    
    hide back_btn
    hide screen puzzle_missing_pieces
    hide screen puzzle_missing_pieces_zoomed
    
    jump f1_p3

label room104:
    scene bg darkroom with fade

    Ethan "Ugh, what's that smell?"
    Ethan "It's like a mix of dust, dirty laundry, and… rotten food left out for weeks."
    Ethan "This whole place feels like a garbage dump, not a bedroom."

    while not back_btn_clicked:
        show screen back_btn
        if not room104_pieces_taken:
            show screen puzzle_missing_pieces("104")

            if puzzle_missing_pieces_clicked: # piece-1, 3, 5, 7
                Ethan "...Wait, is that—on the bed?"
                hide screen puzzle_missing_pieces
                show screen puzzle_missing_pieces_zoomed("104")

                if puzzle_evt_flag:
                    Ethan "Oh, the pieces! There they are."

                elif pieces_count <= 0:
                    Ethan "Are these puzzle pieces?"

                else:
                    Ethan "What's with all these puzzle pieces?"

                menu: 
                    "Take the pieces?"
                    "Yes":
                        Ethan "I'll take them."
                        $ pieces_count += 4
                        $ room104_pieces_taken = True
                        if puzzle_evt_flag:
                            Ethan "I got [pieces_count] of these pieces now."
                            show screen objective_text(chap1_objective_puzzle_evt, 0.98, 0.1)
                    "No":
                        Ethan "I'll leave them here."
                        hide screen puzzle_missing_pieces_zoomed
        
        pause

    hide back_btn
    hide screen puzzle_missing_pieces
    hide screen puzzle_missing_pieces_zoomed
    jump f1_p4

label puzzle_mini_game:
    scene bg darkroom with fade

    if main_key1_acquired:
        Ethan "I already got the Main Key."
        jump f1_p1

    else:
        Ethan "Okay I got all the pieces"
        Ethan "Let's give it a try."

        # Start the drag-and-drop puzzle
        call screen drag_puzzle

        # When solved, returns here after puzzle_win
        "Main Key acquired."
       
        jump f1_p1

label main_room1:
    if not main_key1_acquired:
        $ from_locked_room = True
        "door locked sfx"
        if puzzle_evt_flag:
            if all_pieces_obtained:
                Ethan "It's locked. But, I have all the pieces now. Solving the puzzle might give me a clue."
            else:
                Ethan "It's locked. Maybe I should solve the puzzle first."
        else:
            Ethan "It's locked. I have to find the key."
        window hide
        jump f1_p2

    if not future_travel_done:
        scene bg darkroom with fade
        Ethan "A bunch of alcohol, corporate attire, and… a coffin?"
        Ethan "This is creepy."
        Ethan "Wait… is that the key card for the elevator?"
        show screen f1_keycard
        while not keycard_clicked:
            "Take the Key Card"

        Ethan "Wha-What's happening? I-I feel... "
        hide screen f1_keycard
        hide screen objective_text
        jump future_travel
        
    else: # future_travel is done
        if key_card1_acquired:
            scene bg darkroom with fade
            "I already have the Key Card for the elevator. I better get out of here."
            jump f1_p2
    
        scene bg darkroom with Fade(1.0, 1.0, 1.0, color="#fff")
        Ethan "Haaa... haaa..."
        Ethan "Thi-this is the room before."
        Ethan "I'm... back?"
        Ethan "Haa.. haa…"
        Ethan "Wh-what just happened to me?"
        Ethan "That was.. the worst."
        Ethan "Was that... really my future?"
        Ethan "No, no… I don't want that…"
        Ethan "I... I-I have to get out of this place."
        
        "Key Card Acquired"
        $ key_card1_acquired = True
        call screen objective_text(chap1_objective_go_elevator)
        show screen objective_text(chap1_objective_go_elevator, 0.98, 0.1)

        show screen back_btn
        call set_back_btn_clicked(False)

        while not back_btn_clicked:
            pause

        jump f1_p2

label future_travel:
    scene black with Fade(1.0, 1.0, 1.0, color="#fff")

    "Time Travel Future"
    "DRINKING ALCOHOL"
    "NECKTIE STRANGLE"
    "COFFIN FUNERAL"
    "END"

    $ future_travel_done = True

    jump main_room1
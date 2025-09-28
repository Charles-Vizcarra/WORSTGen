init python:
    # Set default volume for all main channels
    renpy.music.set_volume(0.7, channel="music")
    renpy.music.set_volume(0.7, channel="sound")
    renpy.music.set_volume(0.7, channel="voice")
    renpy.music.set_volume(0.7, channel="movie")


#  <===== Chapter 1 Functions =====

label set_puzzle_missing_pieces_clicked(state):
    $ puzzle_missing_pieces_clicked = state
    return

label set_back_btn_clicked(state):
    $ back_btn_clicked = state
    return    

label set_keycard_clicked(state):
    $ keycard_clicked = state
    return

# ===== Chapter 1 Functions =====>


#  <===== Chapter 2 Functions =====

label set_ladder_clicked(state):
    $ ladder_clicked = state
    return

# ===== Chapter 2 Functions =====>
init python:
    # Keep track of which pieces are placed correctly
    placed = {
        "piece_1": False,
        "piece_2": False,
        "piece_3": False,
        "piece_4": False,
        "piece_5": False,
        "piece_6": False,
        "piece_7": False,
        "piece_8": False,
        "piece_9": False
    }

    # Callback when a piece is dropped
    def drag_placed(drags, drop):
        if not drop:
            return

        piece = drags[0].drag_name
        spot = drop.drag_name

        # Example rule: match piece name to a spot
        # piece_2 → Left Circle, piece_3 → Right Circle, piece_4 → Middle Circle
        if piece == "piece_1" and spot == "1":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_2" and spot == "2":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_3" and spot == "3":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_4" and spot == "A":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_5" and spot == "B":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_6" and spot == "C":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_7" and spot == "D":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_8" and spot == "E":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        elif piece == "piece_9" and spot == "F":
            drags[0].snap(drop.x, drop.y)
            placed[piece] = True
        else:
            # Wrong spot → send back where it was
            drags[0].snap(drags[0].x, drags[0].y)

        # Check win condition
        if all(placed.values()):
            renpy.call_in_new_context("puzzle_win")


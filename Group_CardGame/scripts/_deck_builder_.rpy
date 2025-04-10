label deck_builder:
    python:
        for card in playerdeck:
            card.playercard = True
    label deck_builder_jump:
    show screen deck_builder_screen
    $ renpy.block_rollback()
    $ _choice = ui.interact()

    if _choice in unlocked_cards:
        $ selectcard = unlocked_cards.index(_choice)
        jump deck_builder_jump
    elif _choice == "gallery":
        hide screen deck_builder_screen
        show screen deck_builder_gallery
    elif _choice == "back":
        hide screen deck_builder_gallery
        show screen deck_builder_screen
    elif _choice == "Close":
        $ selectcard = -1
        hide screen deck_builder_screen
        jump main_room_menu
    elif _choice == "guide":
        $ selectcard = -1
        hide screen deck_builder_screen
        jump deck_builder_guide
    elif _choice == "inc":
        $ currentpage += 1
        $ selectcard = -1
        jump deck_builder_jump
    elif _choice == "dec":
        $ currentpage -= 1
        $ selectcard = -1
        jump deck_builder_jump
    elif _choice == "unselect":
        $ selectcard = -1
        jump deck_builder_jump
    else:
        if not selectcard == -1:
            python:
                if unlocked_cards[selectcard].copies > -1:
                    unlocked_cards[selectcard].copies -= 1
                    add_card_to_deck(playerdeck[int(_choice)].title)
                    playerdeck[int(_choice)] = unlocked_cards[selectcard]
                    selectcard = -1
                    pass
            jump deck_builder_jump

        else:
            jump deck_builder_jump

screen deck_builder_screen():
    zorder 8
    $ card_shown=5
    imagebutton idle "images/cardgame/deck_builder.webp" action Return("unselect")

    for i in range(0, clamp(card_shown, 0, (len(unlocked_cards))-(card_shown*currentpage))):
        use cardrender(unlocked_cards[clamp(i+(currentpage*card_shown), 0, len(unlocked_cards))], 18,17+80*i, True)

    if not selectcard == -1:
        use cardrender(unlocked_cards[selectcard], 885, 316)
        #add im.Scale(unlocked_cards[selectcard].imagepath, card_width*0.5, card_height*0.5) xpos 885 ypos 316

        vbox:
            xpos 560
            ypos 320
            xsize 340
            ysize 33
            text "{size=-3}"+unlocked_cards[selectcard].get_title()+"{/size}" xalign 0 yalign 0.5 size 22

        vbox:
            xpos 760
            ypos 520
            xsize 112
            ysize 33
            text unlocked_cards[selectcard].get_amount() xalign 1 yalign 0.5

        vbox:
            xpos 560
            ypos 520
            xsize 112
            ysize 33
            text "{color=#ffffff}Value:{/color}"+unlocked_cards[selectcard].get_totalvalue() xalign 0 yalign 0.5

        vbox:
            xpos 560
            ypos 350
            xsize 300
            ysize 500
            text "{size=-5}"+unlocked_cards[selectcard].get_description()+"{/size}"

    for i in range(0,5):
        use cardrender(playerdeck[i], 223+165*i, 17, True, return_value=i, color=True)

    imagebutton:
        xpos 200
        ypos 380
        idle "images/cardgame/scrollup.webp"
        if not currentpage <= 0:
            hover "images/cardgame/scrollup_hover.webp"
            action Return("dec")

    imagebutton:
        xpos 200
        ypos 430
        idle "images/cardgame/scrolldown.webp"
        if currentpage < math.ceil((len(unlocked_cards)-1)/card_shown):
            hover "images/cardgame/scrolldown_hover.webp"
            action Return("inc")

    #Page info
    $ str_currentpage = currentpage+1
    $ str_currentpage_max = int(math.ceil((len(unlocked_cards)-1)/card_shown)+1.0)
    text "{color=#FFFFFF}{size=-5}Page [str_currentpage]/[str_currentpage_max]{/size}{/color}" xpos 215 ypos 360 text_align 0.5 xalign 0.5

    #Gallery button
    imagebutton:
        xpos 274
        ypos 310
        idle "images/cardgame/gallery.webp"
        hover "images/cardgame/gallery_hover.webp"
        action [Show("deck_builder_gallery"), Hide("deck_builder_screen")]

    #Guide button
    imagebutton:
        xpos 274
        ypos 400
        idle "images/cardgame/guide.webp"
        hover "images/cardgame/guide_hover.webp"
        action Return("guide")

    #Exit button
    imagebutton:
        xpos 274
        ypos 502
        idle "images/cardgame/exit.webp"
        hover "images/cardgame/exit_hover.webp"
        action Return("Close")
        keysym "game_menu"

    #Easter egg
    # hbox:
    #     xpos 1020
    #     ypos 296
    #     xsize 40
    #     ysize 40
    #     button action Jump("color_change") background "#ffffff00"
    #     #add Solid(get_hex_string(playercolor_rgb))

screen deck_builder_gallery():
    zorder 8
    imagebutton idle "interface/desk/_bg_.webp" action NullAction()

    text "{size=+15}Gallery{/size}" ypos 15 xalign 0.5

    for i, card in enumerate(cards_all):

        $ col = (i // 4) % 13
        $ row = i % 4

        use cardrender(card, 18+80*col, 67+125*row, False, cardzoom=0.25, color=card_exist(unlocked_cards, card))

    imagebutton:
        anchor (1.0, 0.0)
        ypos 18
        xalign 0.98

        idle "images/cardgame/back.webp"
        hover "images/cardgame/back_hover.webp"
        action [Show("deck_builder_screen"), Hide("deck_builder_gallery")]
        keysym "game_menu"

label color_change:
    python:
        playercolor_rgb = tuple(color_picker(playercolor_rgb), False, "Player border")
        enemycolor_rgb = tuple(color_picker(enemycolor_rgb), False, "Enemy border")

    jump deck_builder

### NOT WORKING ADD LATER ###
#label deck_builder_guide:
#    $ deck_guide_page = 0
#    $ deck_guide_zone = ""
#    $ deck_guide_helper = ""
#    show screen deck_builder_tutorial
#    with dissolve
#
#    nar "The goal of Triple Triad is to own the most cards on the playing field until all 9 slots are filled."
#    nar "To win the game you have to pay attention to your deck but also the enemy deck."
#
#    # Sides guide
#    $ deck_guide_zone = "player_zone"
#    nar "This is your deck."
#    nar "You can have a maximum of five cards in your active deck."
#    $ deck_guide_zone = "enemy_zone"
#    nar "This is your opponent's deck."
#    nar "Your opponent's deck is also limited to five cards."
#
#    # Inspection guide
#    $ deck_guide_zone = ""
#    $ deck_guide_page = 1
#    nar "You can inspect cards by clicking on them."
#    $ deck_guide_page = 2
#    nar "In the current version of the game you can also inspect enemy cards."
#    nar "This might change later on if we feel like the game is not difficult enough."
#
#    # Card guide
#    $ deck_guide_page = 1
#    nar "To place down a card, simply select it and click on any of the empty fields."
#    $ deck_guide_page = 3
#    nar "You can place only one card per turn."
#    $ deck_guide_zone = "card_zone"
#    $ deck_guide_helper = "border_guide"
#    nar "Every card you place down is displayed with a Blue border and signifies that you own the card."
#    nar "Your opponent's cards are displayed in red."
#
#    $ deck_guide_helper = "numbers_guide"
#    nar "Numbers on the sides, top, and bottom indicate the power of the card in a specific direction."
#    $ deck_guide_helper = "tier_guide"
#    nar "This is what we call a card tier."
#    nar "The shape and colour of it indicates the rarity of the card, while the number tells you the overall power of it."
#    $ deck_guide_helper = ""
#    nar "The card currently displayed is a special card."
#    nar "Special cards are unique and cannot be obtained more than once."
#    $ deck_guide_page = 33
#    nar "They also cannot be obtained more than once, but the picture changes depending on how many challenges you have won."
#    nar "Cool, right?"
#
#    $ deck_guide_helper = ""
#    $ deck_guide_page = 3
#    nar "Moving on."
#    nar "..." ("base", xpos="far_left", ypos="head")
#    #
#    $ deck_guide_zone = "fight_zone"
#    $ deck_guide_helper = "fight_guide"
#    $ deck_guide_page = 4
#    nar "Once a card is played, it can be taken by the opponent when they place a card with a number higher than the side of the card facing that number."
#    $ deck_guide_helper = "border_guide"
#    nar "When a card is taken, its border changes colour."
#    $ deck_guide_zone = ""
#    $ deck_guide_helper = ""
#    $ deck_guide_page = 5
#    nar "The player with the most cards of their colour by the end wins the game."

#    if not states.sna.ev.cardgame.known:
#        nar "(Seems simple enough....)" ("base", xpos="far_left", ypos="head")

    #$ _choice = ui.interact()

    #if _choice == "back":

    hide screen deck_builder_tutorial
    jump deck_builder

    ### NOT WORKING ADD LATER ###

##### screen deck_builder_tutorial():
#####     zorder 18
#####     #imagebutton idle "interface/desk/_bg_.webp" action None
##### 
#####     add "images/cardgame/guide/[deck_guide_page].webp"
##### 
#####     if not deck_guide_zone == "":
#####         add "images/cardgame/guide/[deck_guide_zone].webp"
##### 
#####     if deck_guide_helper == "border_guide":
#####         add "images/cardgame/guide/[deck_guide_helper].webp" xpos 600 ypos 250
##### 
#####     if deck_guide_helper == "numbers_guide":
#####         add "images/cardgame/guide/[deck_guide_helper].webp" xpos 540 ypos 300 xalign 0.5 yalign 0.5
##### 
#####     if deck_guide_helper == "tier_guide":
#####         add "images/cardgame/guide/[deck_guide_helper].webp" xpos 500 ypos 200 xanchor 0.5
##### 
#####     if deck_guide_helper == "fight_guide":
#####         add "images/cardgame/guide/[deck_guide_helper].webp" xpos 540 ypos 360 xalign 0.5

    ##Back button
    #imagebutton:
    #    xpos 930
    #    ypos 480
    #    idle "images/cardgame/back.webp"
    #    hover "images/cardgame/back_hover.webp"
    #    action Return("back")
    #    keysym "game_menu"

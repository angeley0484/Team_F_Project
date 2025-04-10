default selectcard = -1
default selectenemycard = -1
default currentpage = 0
#Shown Cards is a integer for how many cards should be hidden
#
#Sudden Death is where when there is draw then a new round will begin
#Where you take all card of you color up in you hand
#
#Reverse is where the take over is reverse so instead of > it is <
#
#Dobelt_number
# Rules(Shown Cards, Sudden Death, Reverse, Dobelt_number)
default standard_rules = [0, False, False, False]

default playercolor_rgb = Color((51, 92, 147, 255))
default enemycolor_rgb = Color((116, 0, 0, 255))


default table_cards = [[None for x in range(0,3)] for y in range(0,3)]

#Special Cards

default card_bird = Card( imagepath="images/cards/087001_hr1.webp",
                            topvalue = 4,
                            bottomvalue = 2,
                            rightvalue = 2,
                            leftvalue = 1,
                            title="Bird",
                            description = "Its a bird.")

default card_fireball = Card( imagepath="images/cards/087006_hr1.webp",
                            topvalue = 2,
                            bottomvalue = 1,
                            rightvalue = 3,
                            leftvalue = 3,
                            title="Fireball",
                            description = "Its a Fireball.")

default card_snail = Card( imagepath="images/cards/087008_hr1.webp",
                            topvalue = 7,
                            bottomvalue = 1,
                            rightvalue = 4,
                            leftvalue = 4,
                            title="Spike Snail",
                            description = "Its a snail with spikes.")

default card_chicken = Card( imagepath="images/cards/087085_hr1.webp",
                            topvalue = 1,
                            bottomvalue = 2,
                            rightvalue = 3,
                            leftvalue = 3,
                            title="Giant Chicken",
                            description = "Its an oversized chicken.")

default card_monster = Card( imagepath="images/cards/087012_hr1.webp",
                            topvalue = 2,
                            bottomvalue = 2,
                            rightvalue = 5,
                            leftvalue = 5,
                            title="Monster",
                            description = "Its a Monster.")



default enemy_deck = []

default unlocked_cards = [card_monster, card_chicken, card_snail, card_fireball, card_bird]

default playerdeck = [card_monster, card_chicken, card_snail, card_fireball, card_bird]


####### Rulesets for later

#####    default card_rule_reverse = CardGameRule(name="Reverse", description="Instead of a higher number, you need to have the lowest number to take over a card.", icon="images/cardgame/rule_reverse.webp")
#####    default card_rule_hidden = CardGameRule(name="Hidden", description="The hidden rule means that a certain amount of cards in your enemies deck will be hidden.", icon="images/cardgame/rule_hidden.webp")
#####    default card_rule_death = CardGameRule(name="Death", description="If your game ends in a draw you pick up the cards that are shown in your colour and play again.", icon="images/cardgame/rule_death.webp")
#####    default card_rule_double = CardGameRule(name="Double", description="If the card you put down has the same number facing at least 2 other cards (Rather than higher/lower) you'll take over those cards.", icon="images/cardgame/rule_double.webp")
#####    default card_rule_random = CardGameRule(name="Random", description="Your deck is selected randomly from the available cards.", icon="images/cardgame/rule_random.webp")

default cards_basic = [card_monster, card_chicken, card_snail, card_fireball, card_bird]



default cards_all = list(cards_realm) + # list(instert card array here) 

default opponent_first_deck = [card_monster.clone(), card_chicken.clone(), card_snail.clone(), card_fireball.clone(), card_bird.clone()]



init python:

    def card_exist(unlockedlist, cardobj):
        for elm in unlockedlist:
                if cardobj.title == elm.title:
                    return True
        return False
    replace_index = 0
    new_deck = []
    def create_random_deck(min, max, card_pool):
        new_deck = []
        smalles_func = lambda elm1, elm2 : elm1.get_total_value() > elm2.get_total_value()
        gretest_func = lambda elm1, elm2 : elm1.get_total_value() < elm2.get_total_value()
        temp_pool = []
        temp_pool.extend(card_pool)
        for card in range(0,5):
            random_choice = renpy.random.choice(temp_pool)

            new_deck.append(random_choice)
            del temp_pool[temp_pool.index(random_choice)]

        while min > get_deck_score(new_deck) or max < get_deck_score(new_deck):
            replace_index = 0
            if get_deck_score(new_deck) < min:
                replace_index = find_index_func(temp_pool, smalles_func)
            else:
                replace_index = find_index_func(temp_pool, gretest_func)


            replace_index = clamp(replace_index,0,4)
            random_choice = renpy.random.choice(temp_pool)

            temp_pool.append(new_deck[replace_index])
            new_deck[replace_index] = (random_choice)
            del temp_pool[temp_pool.index(random_choice)]

        return new_deck
    def find_index_func(seq, func):
        func_index = 0
        for i in range(0, len(seq)):
            if func(seq[func_index], seq[i]):
                func_index = i
        return func_index

    def get_deck_score(deck):
        score = 0
        for card in deck:
            score += card.get_total_value()
        return score

    def get_image_size(image):
        myDisplayable = im.Image(image)
        myRender = renpy.render(myDisplayable, 800, 600, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]

        return (x,y)

    def get_hex_string(red, green, blue, alpha=1.0):
        red = str(hex( int( math.ceil( red*255))))[2:]
        if not len(red) == 2:
            red = "0"+red
        green = str(hex(int(math.ceil( green * 255))))[2:]
        if not len(green) == 2:
            green = "0"+green
        blue = str(hex(int(math.ceil( blue * 255))))[2:]
        if not len(blue) == 2:
            blue = "0"+blue
        alpha = str(hex(int(math.ceil( alpha * 255))))[2:]
        if not len(alpha) == 2:
            alpha = "0"+alpha

        return "#" + red + green + blue + alpha

    def get_hex_string_tuple(color):
        return get_hex_string(color[0], color[1], color[2], color[3])

    def get_rgb_tuple(hex):
        rgb = get_rgb_list(hex)
        return tuple(rgb)

    def get_rgb_list(hex):
        hex = hex.lstrip('#')
        hex_len = len(hex)
        rgb = list(int(hex[i:i + hex_len // 3], 16) for i in range(0, hex_len, hex_len // 3))
        if len(rgb) < 4:
            rgb.append(255) # Add alpha
        return rgb

    def get_width(image):
        return get_image_size(image)[0]

    def get_height(image):
        return get_image_size(image)[1]

    def reset_table_cards():
        global table_cards

        for y in range(0,3):
            for x in range(0,3):
                table_cards[x][y] = None
        return

    def check_winner(player_deck):
        global table_cards
        playerpoints = len(player_deck)

        for y in range(0,3):
            for x in range(0,3):
                if table_cards[x][y] and table_cards[x][y].playercard:
                    playerpoints += 1
        if playerpoints > 5:
            return "win"
        elif playerpoints == 5:
            return "draw"
        else:
            return "loss"

    def update_table(x, y, reverse, dobelt_number):
        global table_cards
        if reverse:
            take_over = lambda a, b : a < b
        else:
            take_over = lambda a, b : a > b


        if not y == 0 and not table_cards[x][y-1] == None and take_over(table_cards[x][y].topvalue, table_cards[x][y-1].bottomvalue):
            table_cards[x][y-1].playercard = table_cards[x][y].playercard

        if not y == 2 and not table_cards[x][y+1] == None and take_over(table_cards[x][y].bottomvalue, table_cards[x][y+1].topvalue):
            table_cards[x][y+1].playercard = table_cards[x][y].playercard

        if not x == 0 and not table_cards[x-1][y] == None and take_over(table_cards[x][y].leftvalue, table_cards[x-1][y].rightvalue):
            table_cards[x-1][y].playercard = table_cards[x][y].playercard

        if not x == 2 and not table_cards[x+1][y] == None and take_over(table_cards[x][y].rightvalue, table_cards[x+1][y].leftvalue):
            table_cards[x+1][y].playercard = table_cards[x][y].playercard

        if dobelt_number:
            dobelt_found = []
            if not y == 0 and not table_cards[x][y-1] == None:
                if table_cards[x][y].topvalue == table_cards[x][y-1].bottomvalue:
                    dobelt_found.append([x,y-1])

            if not y == 2 and not table_cards[x][y+1] == None:
                if table_cards[x][y].bottomvalue == table_cards[x][y+1].topvalue:
                    dobelt_found.append([x,y+1])

            if not x == 0 and not table_cards[x-1][y] == None:
                if table_cards[x][y].leftvalue == table_cards[x-1][y].rightvalue:
                    dobelt_found.append([x-1,y])


            if not x == 2 and not table_cards[x+1][y] == None:
                if table_cards[x][y].rightvalue == table_cards[x+1][y].leftvalue:
                    dobelt_found.append([x+1,y])

            if len(dobelt_found) > 1:
                for card in dobelt_found:
                    table_cards[card[0]][card[1]].playercard = table_cards[x][y].playercard

    def add_card_to_deck(title):
            for card in unlocked_cards:
                if title == card.title:
                    card.copies += 1

    class CardGameRule(object):
        def __init__(self, **kwargs):
            self.name = None
            self.description = None
            self.icon = None
            self.__dict__.update(**kwargs)

    class Card(object):
        sizes = (320, 480)

        def __init__(self, **kwargs):
            self.playercard = True
            self.textcolor = "{color=#ffffff}"
            self.copies = 0
            self.description = "Description"
            self.title = "Title"
            self.imagepath = "images/cards/card.webp"
            self.backside = "images/cards/087000_hr1.webp"

            self.topvalue = 0
            self.bottomvalue = 1
            self.rightvalue = 2
            self.leftvalue = 3
            self.__dict__.update(**kwargs)

        def get_image(self, backside=False):
            return self.backside if backside else self.imagepath

        ############ FIX THIS BORDER ISSUE



        def get_border(self):
            if self.playercard:
                return Transform("images/cards/border.webp", matrixcolor=TintMatrix(playercolor_rgb))
            return Transform("images/cards/border.webp", matrixcolor=TintMatrix(enemycolor_rgb))

        def get_title(self):
            return self.textcolor+self.title+"{/color}"
        def get_amount(self):
            return self.textcolor+"amount: " + str(self.copies+1)+"{/color}"
        def get_totalvalue(self):
            return self.textcolor+str(self.topvalue+self.bottomvalue+self.leftvalue+self.rightvalue)+"{/color}"
        def get_total_value(self):
            return self.topvalue+self.bottomvalue+self.leftvalue+self.rightvalue

        def get_description(self):
            return self.textcolor+self.description+"{/color}"

        def clone(self):
            return Card(title = self.title,imagepath=self.imagepath, topvalue=self.topvalue, bottomvalue=self.bottomvalue, rightvalue=self.rightvalue, leftvalue=self.leftvalue, playercard = self.playercard)

        def get_ai_score(self, table_of_cards, reverse, dobelt_number):
            high_score = -1000
            position = (0,0)
            wallscore = 3
            getcardscore = 12
            if reverse:
                score_func = lambda a : 10 - a
                take_over = lambda a, b : a < b
            else:
                score_func = lambda a : a
                take_over = lambda a, b : a > b

            for y in range(0,3):
                for x in range(0,3):
                    score = 0
                    if table_cards[x][y] == None:
                        if not y == 0 and not table_cards[x][y-1] == None and table_cards[x][y-1].playercard:
                            if take_over(self.topvalue, table_cards[x][y-1].bottomvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.topvalue)
                        else:
                            score += wallscore

                        if not y == 2 and not table_cards[x][y+1] == None and table_cards[x][y+1].playercard:
                            if take_over(self.bottomvalue, table_cards[x][y+1].topvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.bottomvalue)
                        else:
                            score += wallscore

                        if not x == 0 and not table_cards[x-1][y] == None and table_cards[x-1][y].playercard:
                            if take_over(self.leftvalue, table_cards[x-1][y].rightvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.leftvalue)
                        else:
                            score += wallscore

                        if not x == 2 and not table_cards[x+1][y] == None and table_cards[x+1][y].playercard:
                            if take_over(self.rightvalue, table_cards[x+1][y].leftvalue):
                                score += getcardscore
                            else:
                                score += score_func(self.rightvalue)
                        else:
                            score += wallscore

                        if dobelt_number:
                            dobelt_found = []
                            if not y == 0 and not table_cards[x][y-1] == None:
                                if self.topvalue == table_cards[x][y-1].bottomvalue:
                                    dobelt_found.append(table_cards[x][y-1])

                            if not y == 2 and not table_cards[x][y+1] == None:
                                if self.bottomvalue == table_cards[x][y+1].topvalue:
                                    dobelt_found.append(table_cards[x][y+1])

                            if not x == 0 and not table_cards[x-1][y] == None:
                                if self.leftvalue == table_cards[x-1][y].rightvalue:
                                    dobelt_found.append(table_cards[x-1][y])


                            if not x == 2 and not table_cards[x+1][y] == None:
                                if self.rightvalue == table_cards[x+1][y].leftvalue:
                                    dobelt_found.append(table_cards[x+1][y])

                            if len(dobelt_found) > 1:
                                for card in dobelt_found:
                                    if card.playercard:
                                        high_score += getcardscore

                        if score > high_score:
                            high_score = score
                            position = (x, y)


            return [high_score, position]

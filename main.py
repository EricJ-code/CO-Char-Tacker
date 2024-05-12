import curses

def draw_menu(stdscr, selected_idx, roles, specialties, current_specialty, points):
    stdscr.clear()
    stdscr.addstr("Select your role:\n", curses.color_pair(4))  # Main text color for header

    # Display roles
    for idx, role in enumerate(roles):
        if idx == selected_idx:
            stdscr.addstr("  ")
            stdscr.attron(curses.color_pair(1))  # Selected role color
            stdscr.addstr(f"{role}\n")
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(f"  {role}\n", curses.color_pair(4))  # Main text color for unselected roles

    # Divider
    stdscr.addstr("_" * 40 + "\n", curses.color_pair(4))

    # Display selected role details
    role = roles[selected_idx]
    specialty = specialties[role][current_specialty]['name']
    stdscr.addstr("You have [", curses.color_pair(4))
    stdscr.attron(curses.color_pair(1))  # Role name in highlighted color
    stdscr.addstr(f"{role}")
    stdscr.attroff(curses.color_pair(1))
    stdscr.addstr("] highlighted\n", curses.color_pair(4))
    stdscr.addstr("You are viewing [", curses.color_pair(4))
    stdscr.attron(curses.color_pair(5))  # Specialty name in another color
    stdscr.addstr(f"{specialty}")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr("]\n", curses.color_pair(4))
    stdscr.addstr("Stats:\n", curses.color_pair(4))
    for stat_category, stats in points[role][current_specialty].items():
        stdscr.addstr(f"  {stat_category}:\n", curses.color_pair(4))
        for stat, (value, special) in stats.items():
            if special:
                if len(stat) >= 6:
                    stdscr.addstr(f"\t{stat}", curses.color_pair(4))
                    stdscr.attron(curses.color_pair(2))  # Special stat asterisk color
                    stdscr.addstr("*")
                    stdscr.attroff(curses.color_pair(2))
                    stdscr.addstr(f":\t{value} Points\n", curses.color_pair(4))
                else:
                    stdscr.addstr(f"\t{stat}", curses.color_pair(4))
                    stdscr.attron(curses.color_pair(2))  # Special stat asterisk color
                    stdscr.addstr("*")
                    stdscr.attroff(curses.color_pair(2))
                    stdscr.addstr(f":\t\t{value} Points\n", curses.color_pair(4))
            else:
                if len(stat) >= 7:
                    stdscr.addstr(f"\t{stat}:\t{value} Points\n", curses.color_pair(4))
                else:
                    stdscr.addstr(f"\t{stat}:\t\t{value} Points\n", curses.color_pair(4))
    
    stdscr.addstr("\n[Use arrow keys to see other pages] <->\n", curses.color_pair(4))
    stdscr.addstr("_" * 40 + "\n", curses.color_pair(4))
    stdscr.addstr("[ENTER] to select\n", curses.color_pair(4))
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Selected role color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Special stat asterisk color
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Main text color
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Specialty color

    roles = ["Face", "Muscle", "Scholar", "Slink", "Weird"]
    specialties = {
        "Face": [{"name": "Journalist"}, {"name": "Magician"}],
        "Muscle": [{"name": "Explorer"}, {"name": "Soldier"}],
        "Scholar": [{"name": "Doctor"}, {"name": "Professor"}],
        "Slink": [{"name": "Criminal"}, {"name": "Detective"}],
        "Weird": [{"name": "Medium"}, {"name": "Occultist"}]
    }
    # Initialize points with special flag
    points = {
        "Face": [
            #Journalist
            {"Nerve": 
                {"Move": (0, False) 
                ,"Strike": (0, False)
                ,"Control": (0, False)}
            ,"Cunning": 
                {"Sway": (0, False)
                ,"Read": (1, False)
                ,"Hide": (0, False)}
            ,"Intuition": 
                {"Survey": (2, True)
                ,"Focus": (1, False)
                ,"Sense": (1, False)}},

            #Magician
            {"Nerve": 
                {"Move": (0, False)
                ,"Strike": (0, False)
                ,"Control": (0, False)}
            ,"Cunning": 
                {"Sway": (2, True)
                ,"Read": (1, False)
                ,"Hide": (1, False)}
            ,"Intuition": 
                {"Survey": (0, False)
                ,"Focus": (1, False)
                ,"Sense": (0, False)}}
        ],
        "Muscle": [
            #Explorer
            {"Nerve": 
                {"Move": (1, True) 
                ,"Strike": (2, False)
                ,"Control": (0, False)}
            ,"Cunning": 
                {"Sway": (0, False)
                ,"Read": (0, False)
                ,"Hide": (0, False)}
            ,"Intuition": 
                {"Survey": (1, False)
                ,"Focus": (1, False)
                ,"Sense": (0, False)}},

            #Soldier
            {"Nerve": 
                {"Move": (2, False)
                ,"Strike": (2, True)
                ,"Control": (1, False)}
            ,"Cunning": 
                {"Sway": (0, False)
                ,"Read": (0, False)
                ,"Hide": (0, False)}
            ,"Intuition": 
                {"Survey": (0, False)
                ,"Focus": (0, False)
                ,"Sense": (0, False)}}
        ],

        "Scholar": [
            #Doctor
            {"Nerve": 
                {"Move": (0, False) 
                ,"Strike": (0, False)
                ,"Control": (1, False)}
            ,"Cunning": 
                {"Sway": (0, False)
                ,"Read": (1, True)
                ,"Hide": (0, False)}
            ,"Intuition": 
                {"Survey": (1, False)
                ,"Focus": (2, False)
                ,"Sense": (0, False)}},

            #Professor
            {"Nerve": 
                {"Move": (0, False)
                ,"Strike": (0, False)
                ,"Control": (0, False)}
            ,"Cunning": 
                {"Sway": (1, False)
                ,"Read": (0, False)
                ,"Hide": (0, False)}
            ,"Intuition": 
                {"Survey": (2, False)
                ,"Focus": (2, True)
                ,"Sense": (0, False)}}
        ],
        "Slink": [
            #Criminal
            {"Nerve": 
                {"Move": (0, False) 
                ,"Strike": (0, False)
                ,"Control": (1, False)}
            ,"Cunning": 
                {"Sway": (0, False)
                ,"Read": (0, False)
                ,"Hide": (2, True)}
            ,"Intuition": 
                {"Survey": (1, False)
                ,"Focus": (1, False)
                ,"Sense": (0, False)}},

            #Detective
            {"Nerve": 
                {"Move": (0, False)
                ,"Strike": (0, False)
                ,"Control": (1, True)}
            ,"Cunning": 
                {"Sway": (0, False)
                ,"Read": (0, False)
                ,"Hide": (1, False)}
            ,"Intuition": 
                {"Survey": (2, False)
                ,"Focus": (1, False)
                ,"Sense": (0, False)}}
        ],
        "Weird": [
            #Medium
            {"Nerve": 
                {"Move": (0, False) 
                ,"Strike": (0, False)
                ,"Control": (0, False)}
            ,"Cunning": 
                {"Sway": (0, False)
                ,"Read": (2, True)
                ,"Hide": (0, False)}
            ,"Intuition": 
                {"Survey": (1, False)
                ,"Focus": (0, False)
                ,"Sense": (2, True)}},

            #Detective
            {"Nerve": 
                {"Move": (0, False)
                ,"Strike": (0, False)
                ,"Control": (1, False)}
            ,"Cunning": 
                {"Sway": (0, False)
                ,"Read": (1, False)
                ,"Hide": (0, False)}
            ,"Intuition": 
                {"Survey": (0, False)
                ,"Focus": (1, True)
                ,"Sense": (2, False)}}
        ],
    }
    
    current_row = 0
    current_specialty = 0  # 0 for first specialty, 1 for second

    draw_menu(stdscr, current_row, roles, specialties, current_specialty, points)

    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(roles) - 1:
            current_row += 1
        elif key == curses.KEY_LEFT:
            current_specialty = 0
        elif key == curses.KEY_RIGHT:
            current_specialty = 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break

        draw_menu(stdscr, current_row, roles, specialties, current_specialty, points)

    # Optionally you can add more functionality here for after selection
    stdscr.clear()
    stdscr.addstr(f"You have selected {roles[current_row]} with specialty in {specialties[roles[current_row]][current_specialty]['name']}.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)

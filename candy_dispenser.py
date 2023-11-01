import random
import tkinter as tk

ovals = []
springs = {}
dialog_content = None
candie_colors = []

max_ovals = 7

start_y = 20
spring_y1, spring_y2 = start_y + 6, start_y + 6
plate_y = start_y + 3
spring_height = 200
oval_width = 78
oval_height = 20
oval_spacing = 2
plate_width = 5
plate_x1, plate_x2 = 21, 99
spring_x1, spring_x2 = plate_x1, plate_x2


def add_oval(event):
    global dialog_content

    if dialog_content:
        dialog.delete(dialog_content)

    if len(ovals) < max_ovals:
        x1 = 21
        x2 = x1 + oval_width
        y1 = start_y
        y2 = y1 + oval_height

        fill_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255),
                                                  random.randint(0, 255))

        shift()
        move_spring("down")
        new_oval = canvas.create_oval(x1, y1, x2, y2, outline=fill_color, fill=fill_color)

        # Add the oval reference to the list
        ovals.insert(0, new_oval)
        candie_colors.insert(0, fill_color)

    else:
        dialog_content = dialog.create_text((dialog.winfo_reqwidth() // 2) + 5, dialog.winfo_reqheight() // 2,
                                            text='I am full',
                                            font=("Helvetica", 12),
                                            tags='dialog_content',
                                            fill="red", )


def shift(up=False):
    if len(ovals) > 0:
        if up:
            for oval in ovals:
                new_y = -1 * (oval_spacing + oval_height)
                canvas.move(oval, 0, new_y)

        else:
            for oval in ovals:
                new_y = (oval_spacing + oval_height)

                canvas.move(oval, 0, new_y)

    else:
        print("Not enough ovals to shift.")


def remove_clicked(event):
    global dialog_content
    if dialog_content:
        dialog.delete(dialog_content)

    if ovals:
        candy = ovals.pop(0)
        # print(canvas.itemcget(candy, option=)
        canvas.delete(candy)
        fill_color = candie_colors.pop(0)

        dialog_content = dialog.create_oval(48.5, 65, 126.5, 85, fill=fill_color, outline=fill_color)

        shift(up=True)
        move_spring("up")
    else:
        if dialog_content:
            dialog.delete(dialog_content)
            dialog.delete(dialog_content)

        dialog_content = dialog.create_text((dialog.winfo_reqwidth() // 2) + 5, dialog.winfo_reqheight() // 2,
                                            text='No candies left',
                                            font=("Helvetica", 12),
                                            tags='dialog_content',
                                            fill="red", )


def move_spring(direction, spring_speed=22):
    global plate_y
    occupied_height = ((oval_height + oval_spacing) * (len(ovals) + 1)) + 26
    remaining_height = 200 - occupied_height
    changes = [remaining_height * (4 / 20), remaining_height * (8 / 20), remaining_height * (3 / 20),
               remaining_height * (6 / 20), remaining_height * (2 / 20), remaining_height * (4 / 20),
               remaining_height * (1 / 20),
               remaining_height * (2 / 20)]

    keys_list = list(springs.keys())

    if direction == "up":
        for i in range(len(keys_list)):
            change = changes[i]

            if springs[keys_list[i]][0] == 'down' and springs[keys_list[i]][1] == '8':
                x1, y1, x2, y2 = canvas.coords(keys_list[i])
                y1 -= 22
                canvas.coords(keys_list[i], x1, y1, x2, y1 + change)

            else:
                if springs[keys_list[i]][0] == 'up' and springs[keys_list[i]][1] == '8':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i])
                    y1 -= 13.2
                    y2 -= 17.6
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'down' and springs[keys_list[i]][1] == '6':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i])
                    y1 -= 13.2
                    y2 -= 9.9
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'up' and springs[keys_list[i]][1] == '6':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i])
                    y1 -= 6.6
                    y2 -= 9.9
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'down' and springs[keys_list[i]][1] == '4':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i])
                    y1 -= 6.6
                    y2 -= 4.4
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'up' and springs[keys_list[i]][1] == '4':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i])
                    y1 -= 2.2
                    y2 -= 4.4
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'down' and springs[keys_list[i]][1] == '2':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i])
                    y1 -= 2.2
                    y2 -= 1.1
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'up' and springs[keys_list[i]][1] == '2':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i])
                    y1 -= 0.0
                    y2 -= 1.1
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

        plate_y -= spring_speed
    elif direction == "down":
        for i in range(len(keys_list)):
            change = changes[i]

            if springs[keys_list[i]][0] == 'down' and springs[keys_list[i]][1] == '8':
                x1, y1, x2, y2 = canvas.coords(keys_list[i])
                y1 += 22
                canvas.coords(keys_list[i], x1, y1, x2, y1 + change)

            else:
                if springs[keys_list[i]][0] == 'up' and springs[keys_list[i]][1] == '8':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i - 1])

                    y1 += change
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'down' and springs[keys_list[i]][1] == '6':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i - 1])
                    y2 = y1 + change
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'up' and springs[keys_list[i]][1] == '6':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i - 1])
                    y1 += change
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'down' and springs[keys_list[i]][1] == '4':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i - 1])
                    y2 = y1 + change
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'up' and springs[keys_list[i]][1] == '4':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i - 1])

                    y1 += change
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'down' and springs[keys_list[i]][1] == '2':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i - 1])
                    y2 = y1 + change
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

                if springs[keys_list[i]][0] == 'up' and springs[keys_list[i]][1] == '2':
                    x1, y1, x2, y2 = canvas.coords(keys_list[i - 1])
                    y1 += change
                    canvas.coords(keys_list[i], x1, y1, x2, y2)

        plate_y += spring_speed
    # canvas.coords(spring, 60, spring_y, 60, spring_height)
    canvas.coords(plate, plate_x1, plate_y, plate_x2, plate_y)
    # print("Spring Height: {}".format(spring_height - spring_y))


def peek_clicked(event):
    global dialog_content

    if dialog_content:
        dialog.delete(dialog_content)
    if ovals:
        dialog_content = dialog.create_oval(48.5, 65, 126.5, 85, fill=candie_colors[0], outline=candie_colors[0])

    elif not ovals:
        dialog_content = dialog.create_text((dialog.winfo_reqwidth() // 2) + 5, dialog.winfo_reqheight() // 2,
                                            text='Dispenser is \n empty!',
                                            font=("Helvetica", 12),
                                            tags='dialog_content',
                                            fill="red", )


def remaining_clicked(event):
    global dialog_content

    if dialog_content:
        dialog.delete(dialog_content)
    if len(ovals) >= 1:
        dialog_content = dialog.create_text(75, 75, text=f'{len(ovals)} candie{"" if len(ovals) == 1 else "s"} left',
                                            font=("Helvetica", 12),
                                            tags='dialog_content', fill="orange")
    else:
        dialog_content = dialog.create_text(75, 75, text='No candy left', font=("Helvetica", 12), tags='dialog_content',
                                            fill="orange", )


def check_empty_clicked(event):
    global dialog_content

    if dialog_content:
        dialog.delete(dialog_content)

    status = False
    if len(ovals) < 1:
        status = True

    dialog_content = dialog.create_text(75, 75, text=f'{"Yes" if status else "No"}', font=("Helvetica", 12),
                                        tags='dialog_content',
                                        fill="orange", )


def draw_rectangle(canva):
    x1, y1 = 20, 20
    x2, y2 = 100, 200

    canva.create_rectangle(x1, y1, x2, y2, outline="black", width=2, fill="white")


def create_spring():
    global spring_y1, spring_y2
    no_lines = 8
    changes = [(34.8, ['down', '8']), (69.6, ['up', '8']), (26.1, ['down', '6']), (52.2, ['up', '6']),
               (17.4, ['down', '4']), (34.8, ['up', '4']), (8.7, ['down', '2']), (17.0, ['up', '2'])]

    for i in range(no_lines):
        height_change, group = changes[i]
        if len(springs) == 0:
            spring_y1, spring_y2 = spring_y1, spring_y2 + height_change

        # last_key = list(springs.keys())[-1]
        else:
            x1, y1, x2, y2 = canvas.coords(list(springs.keys())[-1])
            spring_y1, spring_y2 = \
                y1 + height_change if group[0] == 'up' else y1, \
                    y1 + height_change if group[0] == 'down' else y2

        new_spring = canvas.create_line(spring_x1, spring_y1, spring_x2, spring_y2, fill='green', width=3)
        springs[new_spring] = [group[0], group[1]]


root = tk.Tk()
root.title("PEX candy dispenser")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

canvas = tk.Canvas(frame, width=120, height=220)
canvas.grid(row=0)

draw_rectangle(canvas)
plate = canvas.create_line(plate_x1, plate_y, plate_x2, plate_y, fill='green', width=5)

dialog = tk.Canvas(frame, width=150, height=150, )
dialog.create_rectangle(25, 25, 150, 125, outline="black", width=2, fill="white")
dialog.grid(row=0, column=2)
dialog_label = tk.Label(dialog, text="Display", justify='center')
dialog_label.place(x=25, y=20)
create_spring()

button1 = tk.Button(frame, text="Add", width=10)
button2 = tk.Button(frame, text="Remove", width=10)
button3 = tk.Button(frame, text="Peek", width=10)
button4 = tk.Button(frame, text="Remaining", width=10)
button5 = tk.Button(frame, text="Empty?", width=10)

button1.bind("<Button-1>", add_oval)
button2.bind("<Button-1>", remove_clicked)
button3.bind("<Button-1>", peek_clicked)
button4.bind("<Button-1>", remaining_clicked)
button5.bind("<Button-1>", check_empty_clicked)

button1.grid(row=1)
button2.grid(row=2)
button3.grid(row=3)
button4.grid(row=4)
button5.grid(row=5)

root.mainloop()

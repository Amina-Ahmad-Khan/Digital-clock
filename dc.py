from tkinter import *
import time
import math

def update_time():
    current_time = time.strftime('%I:%M:%S %p')
    clock_label.config(text=current_time)
    draw_clock_hands()  # Update clock hands before updating time label
    clock_label.after(1000, update_time)

def draw_clock_face():
    center_x = 150
    center_y = 150
    clock_radius = 140

    # Draw clock outline
    clock_canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                             center_x + clock_radius, center_y + clock_radius,
                             outline="white", width=4)

    # Draw hour markers
    for i in range(12):
        angle = math.radians(30 * i)
        marker_outer_x = center_x + clock_radius * math.sin(angle)
        marker_outer_y = center_y - clock_radius * math.cos(angle)
        marker_inner_x = center_x + (clock_radius - 10) * math.sin(angle)
        marker_inner_y = center_y - (clock_radius - 10) * math.cos(angle)
        clock_canvas.create_line(marker_outer_x, marker_outer_y,
                                 marker_inner_x, marker_inner_y,
                                 fill="white", width=4)

def draw_clock_hands():
    # Clear previously drawn hands
    clock_canvas.delete("clock_hand")

    current_time = time.localtime()
    hours, minutes, seconds = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

    # Calculate angles for hour, minute, and second hands
    hour_angle = math.radians(((hours % 12) + minutes / 60) * 30)
    minute_angle = math.radians((minutes + seconds / 60) * 6)
    second_angle = math.radians(seconds * 6)

    # Draw hour hand
    draw_hand(hour_angle, 50, "blue", 6)

    # Draw minute hand
    draw_hand(minute_angle, 70, "white", 4)

    # Draw second hand
    draw_hand(second_angle, 90, "red", 2)

def draw_hand(angle, length, color, width):
    center_x = 150
    center_y = 150
    hand_end_x = center_x + length * math.sin(angle)
    hand_end_y = center_y - length * math.cos(angle)
    clock_canvas.create_line(center_x, center_y, hand_end_x, hand_end_y, fill=color, width=width, tags="clock_hand")

root = Tk()
root.title("Analog Clock")
root.configure(bg='black')

clock_label = Label(root, font=('New Times Roman', 20, 'italic'), bg='black', fg='white')
clock_label.pack(padx=20, pady=10)

clock_canvas = Canvas(root, width=300, height=300, bg='black', highlightthickness=0)
clock_canvas.pack()

draw_clock_face()
update_time()
root.mainloop()

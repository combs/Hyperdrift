import csv, os, sys


# dimensions
dx, dy = (98, 98)


leds_x, leds_y = (8, 8)


all_paddings_x, all_paddings_y = leds_x+1, leds_y+1

# Keep out of this zone
margin_x, margin_y = (13, 13)


print("margin_x", margin_x, "padding alone", dx / all_paddings_x)

start_x = max(margin_x,  dx / all_paddings_x)
start_y = max(margin_y,  dy / all_paddings_y)
end_x = dx - start_x
end_y = dx - start_y

print("start_x", start_x, "end_x", end_x, "start_y", start_y, "end_y", end_y)

per_x = (end_x - start_x) / (leds_x - 1)
per_y = (end_y - start_y) / (leds_y - 1)

# kicad footprints are offset by this much per led
offset_x = -1.5
offset_y = 0

rows = []

for diode in range(leds_x * leds_y):

    ident = "D" + str(diode + 1)
    y = diode // 8
    x = diode % 8
    row = {"refdes": ident, "x": x * per_x + start_x + offset_x, "y": 0 - (y * per_y + start_y + offset_y)}
    # PartsPlacer Kicad for some reason expects inverted y axis
    rows.append(row)

with open("pixel-grid.csv", "w") as fh:
    writer = csv.DictWriter(fh, fieldnames=("refdes", "x", "y"))
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print("wrote pixel-grid.csv")



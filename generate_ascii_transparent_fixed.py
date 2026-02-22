from PIL import Image, ImageDraw, ImageFont, ImageChops

def generate_white_bg_banner():
    # --- Settings ---
    width = 1200
    temp_height = 300     
    # KEY FIX 1: Pure White background makes 'multiply' blend mode turn transparent!
    bg_color = "#FFFFFF"  
    text_color = "#333333"
    num_frames = 88
    
    raw_frames = []

    # Attempt to load a monospace font
    font = None
    font_options = ["UbuntuMono-R.ttf", "consola.ttf", "cour.ttf", "Courier", "Monaco"]
    for font_name in font_options:
        try:
            font = ImageFont.truetype(font_name, 36)
            break
        except IOError:
            continue
    if not font: font = ImageFont.load_default()

    # --- Generate Frames ---
    for i in range(num_frames):
        frame = Image.new("RGB", (width, temp_height), bg_color)
        draw = ImageDraw.Draw(frame)
        
        # --- Cat & Yarn Logic (Preserving your perfect geometry) ---
        if (i // 2) % 2 == 0:
            c1, c2, c3, c4 = r"       /\_/\   ", r"      ( o.o )  ", r"  ~~~~-----    ", r"____//____\\___"
        else:
            c1, c2, c3, c4 = r"       /\_/\   ", r"      ( >.< )  ", r"   ~~~-----    ", r"____\\____//___"

        state = i % 4
        if state == 0:   y3, y4 = r" /-\ ", r" \-  "
        elif state == 1: y3, y4 = r" /-\ ", r" \-  " # Adjusted for sync
        elif state == 2: y3, y4 = r" /-\ ", r"  -/ "
        else:            y3, y4 = r"  -\ ", r" \-/ "
        
        # Logic adjustment to match previous "perfect" loop states exactly
        if state == 0:   y3 = r" /-\ "
        elif state == 3: y3 = r"  -\ "
        else:            y3 = r" /-\ "
        
        if state == 1:   y4 = r" \-  "
        elif state == 2: y4 = r"  -/ "
        else:            y4 = r" \-/ "

        # String Construction
        gap_size = 8
        mid_space, mid_trail = " " * 8, "_" * 8
        end_space = " " * 60
        end_trail = (" " * gap_size) + ("_" * (60 - gap_size))
        
        base_l1 = c1 + mid_space + "     " + end_space
        base_l2 = c2 + mid_space + "     " + end_space
        base_l3 = c3 + mid_space + y3      + end_space
        base_l4 = c4 + mid_trail + y4      + end_trail
        
        # Wrap Logic
        if i > 0:
            l1, l2, l3, l4 = base_l1[-i:] + base_l1[:-i], base_l2[-i:] + base_l2[:-i], base_l3[-i:] + base_l3[:-i], base_l4[-i:] + base_l4[:-i]
        else:
            l1, l2, l3, l4 = base_l1, base_l2, base_l3, base_l4
            
        full_text = f"{l1*2}\n{l2*2}\n{l3*2}\n{l4*2}"
        
        # Draw text
        draw.text((-10, 50), full_text, font=font, fill=text_color, spacing=4)
        raw_frames.append(frame)

    # --- KEY FIX 2: Aggressive Auto-Crop ---
    bg_frame = Image.new("RGB", (width, temp_height), bg_color)
    min_y, max_y = temp_height, 0
    
    for frame in raw_frames:
        diff = ImageChops.difference(frame, bg_frame)
        bbox = diff.getbbox()
        if bbox:
            _, upper, _, lower = bbox
            min_y = min(min_y, upper)
            max_y = max(max_y, lower)
    
    # Crop tight (only 1 pixel padding)
    min_y = max(0, min_y - 1)
    max_y = min(temp_height, max_y + 1)
    
    final_frames = [f.crop((0, min_y, width, max_y)) for f in raw_frames]
    
    # Cinematic Start Offset
    start_idx = 60
    final_frames = final_frames[start_idx:] + final_frames[:start_idx]

    final_frames[0].save("ascii_transparent_fixed.gif", save_all=True, append_images=final_frames[1:], duration=100, loop=0)
    print(f"Generated clean white-bg GIF! Height is now tight: {max_y - min_y}px")

if __name__ == "__main__":
    generate_white_bg_banner()
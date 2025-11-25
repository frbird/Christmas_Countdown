# Christmas Countdown Clock

A festive web-based countdown timer that displays the time remaining until Christmas Day. Features a beautiful green background with Christmas lights and snowflakes, with countdown digits displayed in red boxes.

## Features

- **Real-time countdown** to Christmas Day (December 25th)
- **Beautiful festive design** with Christmas-themed background image
- **Digital clock font** for authentic countdown display
- **Responsive design** that works on various screen sizes
- **Smooth updates** using `requestAnimationFrame` for optimal performance
- **Accessibility features** with ARIA labels and live regions
- **Automatic year handling** - automatically counts down to next Christmas if current date has passed

## How to Use

1. Open `countdown_website.html` in a web browser
2. The countdown will automatically start displaying:
   - **Days** remaining (large display at top)
   - **Hours** remaining (bottom left)
   - **Minutes** remaining (bottom center)
   - **Seconds** remaining (bottom right)
3. On Christmas Day, the display will show "Merry Christmas!" message

## File Structure

```
Christmas_Countdown/
├── countdown_website.html    # Main HTML file with countdown functionality
├── countdown.py               # Python countdown script (separate utility)
├── fonts/
│   ├── digital-7/            # Digital clock font family
│   └── ds_digital/           # DS Digital font (used in the countdown)
└── images/
    └── IMG_0534.png          # Festive background image with Christmas lights
```

## Technical Details

### Technologies Used
- HTML5
- CSS3 (with custom fonts, responsive design, and animations)
- Vanilla JavaScript (no dependencies)

### Key Features
- **Custom Font**: Uses DS-DIGI.TTF digital clock font for authentic countdown appearance
- **Background Image**: Festive green background with Christmas lights and snowflakes
- **Color Scheme**: Dark green digits with black outline for visibility against red boxes
- **Performance**: Uses `requestAnimationFrame` for smooth, efficient updates
- **Responsive**: Uses `clamp()` and viewport units for responsive sizing

### Browser Compatibility
Works in all modern browsers that support:
- CSS `@font-face`
- `requestAnimationFrame` API
- CSS `clamp()` function

## Customization

### Adjusting Digit Colors
Edit the `.box` class in the CSS section to change the digit color:
```css
.box {
    color: #006600; /* Change this to your desired color */
}
```

### Adjusting Position
Modify the positioning values in the CSS for each time unit:
- `#days` - Top center position
- `#hours` - Bottom left position
- `#minutes` - Bottom center position
- `#seconds` - Bottom right position

### Font Size
Adjust the `font-size` values using `clamp()` for responsive sizing:
```css
#days .time-value {
    font-size: clamp(2.5rem, 35vw, 22rem);
}
```

## Notes

- The countdown automatically handles year transitions
- On Christmas Day, all countdown displays are hidden and replaced with a "Merry Christmas!" message
- The background image should be kept in the `images/` folder for proper display
- Font files must remain in the `fonts/` directory structure

## License

This project is provided as-is for personal use.



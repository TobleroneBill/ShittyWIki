from Website import Create_App

# Color palettes
colors = [
 0x002082,  # Darkest
 0x3057e1,
 0x4a6de5,
 0xced8f7   # Brightest
]

app = Create_App()
if __name__ == '__main__':
    app.run(debug=True)
    print('hi')

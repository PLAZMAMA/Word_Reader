from GUI import *


for i in range(29):
    img = Img(f"/Users/maor/Documents/src/Word_Reader/data/words/{i}.png")
    plt.imshow(img.image)
    plt.show()
    letters = img.preprocess()
    print(f"letters: {letters}")
    c = 0
    for letter in letters:
        im = Image.fromarray(letter)
        im.save(f"/Users/maor/Documents/src/Word_Reader/data/unlabeled_letters/{i}:{c}.png")
        c += 1
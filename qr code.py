import qrcode

img = qrcode.make("https://twitter.com/matindra")
img.save("twitter_matindra.jpg")
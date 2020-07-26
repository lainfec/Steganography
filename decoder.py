from PIL import Image


im = Image.open("new_img.png")
pixels = im.load()

bin_string=''

for x in range(0,im.width):
    for y in range(0,im.height):
        r,g,b=pixels[x,y]
        bin_string+=str(r%2)+str(g%2)+str(b%2)

n=len(bin_string)
true_string=''
itr=7

while itr<n:
    true_string+=chr(int(bin_string[itr-7:itr],2))
    itr+=7

print("Welcome to the Decoder! This decoder uses new_img.png as the source image.")

x=true_string.find("NUDIUSTERTIAN")
if x==-1:
    print("new_img.png is not encoded!")
else:
    print("Your encoded message is: ",true_string[:x])

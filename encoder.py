from PIL import Image

print("Welcome to this naive LSB Steganographic encoder! This program uses image.png as the source image")
im = Image.open("image.png")
org_pixels = im.load()

new_img=Image.new('RGB', (im.width, im.height), 'black')
pixels=new_img.load()

message=input("Enter the message you'd like to hide in the image: ")
message+="NUDIUSTERTIAN"
if len(message)%3!=0:
    while len(message)%3!=0:
        message+='a'

bin_string=''.join('{:0<7}'.format(format(ord(x),'b')) for x in message)
str_itr,n=0,len(bin_string)

for x in range(0,im.width):
    for y in range(0,im.height):
        fr,fg,fb,a=org_pixels[x,y]
        if str_itr<n:
            r,g,b,a=org_pixels[x,y]

            fr=int(f'{r:08b}'[:7]+bin_string[str_itr],2)
            str_itr+=1
            fg=int(f'{g:08b}'[:7]+bin_string[str_itr],2)
            str_itr+=1
            fb=int(f'{b:08b}'[:7]+bin_string[str_itr],2)
            str_itr+=1

        pixels[x,y]=(fr,fg,fb)


new_img.save("new_img.png")
print("Saved!")
            



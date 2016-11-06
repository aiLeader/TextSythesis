#synthesis text
import os
import Image, ImageFont, ImageDraw

f=open("atoms.txt")
atoms=[];
for lines in f:
    lines=lines.rstrip("\n")
    atoms.append(lines);
f.close();

#text="ABC"
fonts=['FreeMono.ttf','FreeSerifBold.ttf','FreeSerifBoldItalic.ttf','Ubuntu-B.ttf'];
cnt = 0;
#ff = open("position.txt","w")
for i in range(0,len(atoms)):
    for j in range(0,len(fonts)):
        im=Image.new("RGB",(300,100),(0,0,255));
        dr=ImageDraw.Draw(im);
        font=ImageFont.truetype(os.path.join("fonts",fonts[j]),50)
        dr.text((80,20),atoms[i],font=font);
        #im.show();
        cnt = cnt + 1;
        im.save("images/%d.png"%cnt);
        #ff.write("%d.png\n"%cnt);
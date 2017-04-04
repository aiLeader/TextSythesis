#synthesis text
import os
import Image, ImageFont, ImageDraw
import TextReader
import random
import numpy as np

#atoms=[unicode('使用在图片上添加中文文字','utf-8')];
reader = TextReader.TextReader();
reader.read("atoms.txt");
reader.read_background_image("back.txt");


#f=open("atoms.txt")

#for lines in f:
#    lines=lines.rstrip("\n")
#    atoms.append(lines);
#f.close();



#text="ABC"
fonts=['songti.TTF'];
cnt = 0;
#ff = open("position.txt","w")
height = 300;
width = 1000;
font_size = 40;

for i in range(0,len(reader.atoms)):
    for j in range(0,len(fonts)):
        label=Image.new("RGB",(width,height),(0,0,255));
        idx = random.randint(0,len(reader.image_path)-1);
        image=Image.open(reader.image_path[idx]);
        h = image.size[1];
        w = image.size[0];
        img = image.crop((0, 0, width, height));
        dr=ImageDraw.Draw(label);
        drr = ImageDraw.Draw(img);
        font=ImageFont.truetype(os.path.join("fonts",fonts[j]),font_size)
        l = len(reader.atoms[i])
        cx = width/2;
        cy = height/2;

        dr.text((cx - l/2*font_size,cy ),reader.atoms[i],font=font);
        drr.text((cx - l/2*font_size,cy ),reader.atoms[i],font=font);
        #im.show();
        cnt = cnt + 1;
        label.save("labels/%d.png"%cnt);
        img.save("images/%d.png"%cnt);

        reader.get_box(np.array(label));
        #ff.write("%d.png\n"%cnt);
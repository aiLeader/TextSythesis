#synthesis text
import os
import Image, ImageFont, ImageDraw
import TextReader
import random
import numpy as np
import cv2
reader = TextReader.TextReader();
reader.read("atoms.txt");
reader.read_background_image("back.txt");
fonts=['songti.TTF'];
cnt = 0;
height = 224;
width = 1000;
font_size = 40;

for i in range(0,len(reader.atoms)):
    for j in range(0,len(fonts)):
        label=Image.new("RGB",(width,height),(0,0,255));
        idx = random.randint(0,len(reader.image_path)-1);
        image=Image.open(reader.image_path[idx]);
        h = image.size[1];
        w = image.size[0];

        dx = random.randint(0,w-width);
        dy = random.randint(0,h-height);

        img = image.crop((dx, dy, dx+width, dy+height));
        dr=ImageDraw.Draw(label);
        drr = ImageDraw.Draw(img);
        font=ImageFont.truetype(os.path.join("fonts",fonts[j]),font_size)
        l = len(reader.atoms[i])
        cx = width/2;
        cy = height/2;

        dr.text((cx - l/2*font_size,cy ),reader.atoms[i],font=font);
        drr.text((cx - l/2*font_size,cy ),reader.atoms[i],font=font);
        #im.show();

        #label.save("pixels/%d.png"%cnt);


        reader.get_box(np.array(label), len(reader.atoms[i]));
        if len(reader.box) <=0:
            continue;
        
        im_show = np.array(img)
        for i in range(0,len(reader.box)):
            cv2.rectangle(im_show,(reader.box[i][0],reader.box[i][1]),(reader.box[i][2],reader.box[i][3]),(255,0,0), 2);
        #cv2.imshow("src",im_show);
        cv2.imwrite("pixels/%d.png"%cnt, im_show);
        img.save("images/%d.jpg"%cnt);
        f = open("labels/%d.txt"%cnt,"w");
        for i in range(0,len(reader.box)):
           xc = (float(reader.box[i][0]) + float(reader.box[i][2]))/(2.0*float(width));
           yc = (float(reader.box[i][1]) + float(reader.box[i][3]))/(2.0*float(height));
           w = (-float(reader.box[i][0]) + float(reader.box[i][2]))/float(width);
           h = (-float(reader.box[i][1]) + float(reader.box[i][3]))/float(height);
           x0 = reader.box[i][0];
           y0 = reader.box[i][1];
           x1 = reader.box[i][2];
           y1 = reader.box[i][3];
           f.write("%d %d %d %d\n"%(x0,y0,x1,y1));
        f.close();


        #f.write("%d %d\n"%(height,width));
        
        length = len(reader.box)-1;
        xc = (float(reader.box[0][0]) + float(reader.box[length][2]))/(2.0*float(width));
        yc = (float(reader.box[0][1]) + float(reader.box[length][3]))/(2.0*float(height));
        w = (-float(reader.box[0][0]) + float(reader.box[length][2]))/float(width);
        h = (-float(reader.box[0][1]) + float(reader.box[length][3]))/float(height);
        x0 = reader.box[0][0];
        x1 = reader.box[length][2];
        y0 = reader.box[0][1];
        y1 = reader.box[length][3];


        #f.write("%d %d %d %d\n"%(x0,y0,x1,y1));
        cnt = cnt + 1;
        if cnt %100 ==0:
            print cnt

        
        #cv2.waitKey(0);
        #ff.write("%d.png\n"%cnt);

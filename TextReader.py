
import cv2
import numpy as np 
class TextReader:
    def read(self, file):
        f = open(file,"r");
        self.atoms = [];
        for lines in f:
            lines = lines.strip("\n");
            content = lines.split(" ");
            for j in range(len(content)):
                content[j] = unicode(content[j],'utf-8')
                self.atoms.append(content[j]);
        f.close();
    def read_background_image(self, file):
        f= open(file,"r");
        self.image_path = [];
        for lines in f:
            lines = lines.strip("\n");
            self.image_path.append(lines);
        f.close();
    def get_box(self, img, leng):
        imggray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY);
        imgfloat = imggray.astype(np.float);
        colimg = np.sum(imgfloat,0);
        colimg = colimg - np.min(colimg);
        rowimg = np.sum(imgfloat,1);
        rowimg = rowimg - np.min(rowimg);
        self.rowstart = [];
        self.rowend = [];
        self.colstart = [];
        self.colend = [];
        th = 10;
        for i in range(0, rowimg.shape[0]-1):
            if rowimg[i] <= th and rowimg[i+1] >= th:
                self.rowstart.append(i);
            if rowimg[i] >= th and rowimg[i+1] <= th:
                self.rowend.append(i);
                
        for i in range(0, colimg.shape[0]-1):
            if colimg[i] <= th and colimg[i+1] >= th:
                self.colstart.append(i);
            if colimg[i] >= th and colimg[i+1] <= th:
                self.colend.append(i);
                


        self.box = [];

        if len(self.colstart) <=0 or len(self.rowstart) <=0:
            return;
        
        x0 = min(self.colstart);
        x1 = max(self.colend);
        per = float(x1-x0)/leng;
        for i in range(0,leng):
            self.box.append([self.colstart[0] + int(i*per), self.rowstart[0], self.colstart[0] + int((i+1)*per), self.rowend[0]]);
            
        #np.savetxt("row.txt",rowimg);
        #np.savetxt("col.txt",colimg);

        
        

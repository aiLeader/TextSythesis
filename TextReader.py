
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
    def get_box(self, img):
        imggray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY);
        imgfloat = imggray.astype(np.float);
        colimg = np.sum(imgfloat,0);
        colimg = colimg - np.min(colimg);
        rowimg = np.sum(imgfloat,1);
        rowimg = rowimg - np.min(rowimg);
        for i in range(0, rowimg.shape[0]):
            if rowimg[i,0] >= 10:
                
                

        cv2.imshow("src",imggray);
        #np.savetxt("row.txt",rowimg);
        #np.savetxt("col.txt",colimg);
        
        
        cv2.waitKey(0);
        
        

import cv2


class Test:
    img=0
    grayImage=0
    binaryImage=0
    def readImage(self):
        #self.img = cv2.imread("dandan.jpg",cv2.IMREAD_GRAYSCALE);
        self.img = cv2.imread("dandan.jpg");
    def do(self):
        self.readImage()
        cv2.namedWindow('Iridan',cv2.WINDOW_NORMAL);
        cv2.imshow('Iridan',self.img);
        #Gray
        self.grayImage = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        cv2.namedWindow('Iridan-Gray',cv2.WINDOW_NORMAL);
        cv2.imshow('Iridan-Gray',self.grayImage);
        #Binary
        ret,self.binaryImage = cv2.threshold(self.grayImage,50,255,cv2.THRESH_BINARY)
        cv2.namedWindow('Iridan-Binary',cv2.WINDOW_NORMAL);
        cv2.imwrite('dd.png',self.binaryImage)
        cv2.imshow('Iridan-Binary',self.binaryImage);
        #Show
        cv2.waitKey(0)
        cv2.destroyAllWindows();
def main():
    print ("start test ");
    myTest = Test();
    myTest.do();


main();

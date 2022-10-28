import cv2

img = cv2.imread("numpy_new.jpg")
img2 = cv2.imread("opencv_new.jpg")

bitwiseNot = cv2.bitwise_not(img2)
bitwiseXor = cv2.bitwise_xor(img,bitwiseNot)

cv2.imshow("extract_fapiao_Not инвертировать операцию:",bitwiseNot)
cv2.imshow("bitwiseXor XOR операция:",bitwiseXor)
# cv2.imwrite("./extract_fapiao_Not.png",bitwiseNot)
# cv2.imwrite("./fapiao_Not_Xor.png",bitwiseXor)
cv2.waitKey(0)
cv2.destroyAllWindows()
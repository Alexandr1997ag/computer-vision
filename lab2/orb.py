import cv2
import numpy as np


query_img = cv2.imread('/media/alex/One Touch/учеба/комп зрение/lab2/пример/1.jpg')
original_img = cv2.imread('/media/alex/One Touch/учеба/комп зрение/lab2/пример/12.jpg')
query_img_bw = cv2.cvtColor(query_img, cv2.IMREAD_GRAYSCALE)
original_img_bw = cv2.cvtColor(original_img, cv2.IMREAD_GRAYSCALE)


orb = cv2.ORB_create()
queryKP, queryDes = orb.detectAndCompute(query_img_bw,None)
trainKP, trainDes = orb.detectAndCompute(original_img_bw,None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = matcher.match(queryDes,trainDes)
matches = sorted(matches, key = lambda x:x.distance)

final_img = cv2.drawMatches(query_img, queryKP,
                            original_img, trainKP, matches[:20], None)

final_img = cv2.resize(final_img, (1000, 650))

cv2.imshow("Matches", final_img)
cv2.waitKey()
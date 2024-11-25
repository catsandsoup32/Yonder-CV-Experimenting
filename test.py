import cv2
import numpy as np

frame = np.zeros((480, 640, 3), dtype=np.uint8)  # Create a black frame
cv2.putText(frame, "Test Window", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow('Test', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
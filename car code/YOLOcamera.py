import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('best.pt')

# Open the video file
cap = cv2.VideoCapture(0)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    frame = cv2.flip(frame,0)

    if success:
        # Run YOLOv8 inference on the frame
        results = model.predict(source=frame,show=True,imgsz=224,conf=0.8,verbose=False)

        # Visualize the results on the frame
        #annotated_frame = results[0].plot()

        # Display the annotated frame
        #cv2.imshow("YOLOv8 Inference", annotated_frame)
        #print(results[0].boxes.cls.cpu().numpy())
        for r in results:
        	for c in r.boxes.cls:
        		obj = model.names[int(c)]
                        
                # Printing detected objects
        		print(obj)

    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()


import cv2
import time

def main():
    # Replace with your RTSP URL
    rtsp_url = "rtsp://username:password@ip_address:port/stream_path"
    output_file = "output.avi"  # Output file for recording
    timeout = 10  # Timeout in seconds

    # Create a VideoCapture object
    cap = cv2.VideoCapture(rtsp_url)
    start_time = time.time()

    # Check if the connection is successful
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Check for timeout
            if time.time() - start_time > timeout:
                print("Error: Timeout reached.")
                break

            if not ret:
                print("Error: Failed to capture image")
                break

            # Write the frame into the file
            out.write(frame)

            # Display the resulting frame
            cv2.imshow('RTSP Stream', frame)

            # Press 'q' to quit the video feed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # When everything done, release the capture and writer
        cap.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

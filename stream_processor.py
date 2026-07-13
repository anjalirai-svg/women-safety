"""
Stream Processor
Captures frames from a video source (webcam, RTSP feed, or file) and
yields them for downstream processing.
"""

import cv2


class StreamProcessor:
    def __init__(self, source=0, resize_width: int = 640):
        """
        source: 0 for default webcam, or an RTSP/HTTP URL, or a file path.
        """
        self.source = source
        self.resize_width = resize_width
        self.cap = cv2.VideoCapture(source)

        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open video source: {source}")

    def frames(self):
        """Generator yielding resized BGR frames one at a time."""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            h, w = frame.shape[:2]
            scale = self.resize_width / w
            frame = cv2.resize(frame, (self.resize_width, int(h * scale)))

            yield frame

    def release(self):
        self.cap.release()


if __name__ == "__main__":
    sp = StreamProcessor(source=0)
    for frame in sp.frames():
        cv2.imshow("Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    sp.release()
    cv2.destroyAllWindows()

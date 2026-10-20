"""Detect vehicles in a video using a pretrained YOLO model."""

import argparse
import cv2
from ultralytics import YOLO

# COCO class IDs: car=2, motorcycle=3, bus=5, truck=7
VEHICLE_CLASSES = {2, 3, 5, 7}


def process_video(source, confidence=0.30, model_path="yolov8n.pt"):
    """Display vehicle detections and counts for each video frame."""
    model = YOLO(model_path)
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        raise RuntimeError(f"Could not open video source: {source}")

    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            results = model.predict(
                frame,
                conf=confidence,
                classes=list(VEHICLE_CLASSES),
                verbose=False,
            )

            vehicle_count = 0

            for result in results:
                if result.boxes is not None:
                    vehicle_count = len(result.boxes)

                    for box in result.boxes:
                        x1, y1, x2, y2 = map(
                            int, box.xyxy[0].tolist()
                        )
                        class_id = int(box.cls[0].item())
                        label = model.names[class_id]

                        cv2.rectangle(
                            frame, (x1, y1), (x2, y2),
                            (0, 255, 0), 2
                        )
                        cv2.putText(
                            frame, label, (x1, max(20, y1 - 8)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0, 255, 0), 2
                        )

            cv2.putText(
                frame,
                f"Vehicles in frame: {vehicle_count}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2,
            )

            cv2.imshow("Smart Traffic - Vehicle Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(
        description="Detect vehicles in traffic video."
    )
    parser.add_argument(
        "--source",
        default="0",
        help="Video filename or camera index (default: 0).",
    )
    parser.add_argument(
        "--confidence",
        type=float,
        default=0.30,
        help="Detection confidence threshold.",
    )
    parser.add_argument(
        "--model",
        default="yolov8n.pt",
        help="Path to pretrained YOLO model weights.",
    )
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source

    process_video(
        source,
        confidence=args.confidence,
        model_path=args.model,
    )


if __name__ == "__main__":
    main()

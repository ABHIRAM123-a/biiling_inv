"""
Smart Traffic Management System - Configuration
"""

# ─── YOLO Settings ───────────────────────────────────────────────
YOLO_MODEL_PATH = "yolov8n.pt"          # nano for speed; swap to yolov8m.pt for accuracy
YOLO_CONFIDENCE_THRESHOLD = 0.5
YOLO_NMS_THRESHOLD = 0.45
YOLO_INPUT_SIZE = (640, 640)

# Vehicle class IDs (COCO dataset)
VEHICLE_CLASSES = {
    2:  "car",
    3:  "motorcycle",
    5:  "bus",
    7:  "truck",
    1:  "bicycle",
}

# ─── Kalman Filter Settings ───────────────────────────────────────
KALMAN_PROCESS_NOISE = 1e-2
KALMAN_MEASUREMENT_NOISE = 1e-1
KALMAN_MAX_MISSED_FRAMES = 10           # frames before a track is dropped
KALMAN_MIN_HITS = 3                     # min detections to confirm a track

# ─── Traffic Signal Settings ──────────────────────────────────────
# Phase durations in seconds
SIGNAL_MIN_GREEN = 10
SIGNAL_MAX_GREEN = 60
SIGNAL_YELLOW_DURATION = 3
SIGNAL_BASE_GREEN = 20

# Density → green time mapping
DENSITY_THRESHOLDS = {
    "low":    (0,  5),    # vehicles → (min, max) green
    "medium": (5,  15),
    "high":   (15, 999),
}
DENSITY_GREEN_TIMES = {
    "low":    15,
    "medium": 30,
    "high":   50,
}

# ─── ROI / Lane Settings ─────────────────────────────────────────
# Each lane is a polygon: [(x1,y1), (x2,y2), ...]
# These are placeholder ratios (0–1) relative to frame size.
LANE_ROIS_NORMALIZED = {
    "North": [(0.0, 0.0), (0.5, 0.0), (0.5, 0.5), (0.0, 0.5)],
    "South": [(0.5, 0.5), (1.0, 0.5), (1.0, 1.0), (0.5, 1.0)],
    "East":  [(0.5, 0.0), (1.0, 0.0), (1.0, 0.5), (0.5, 0.5)],
    "West":  [(0.0, 0.5), (0.5, 0.5), (0.5, 1.0), (0.0, 1.0)],
}

# ─── CNN Congestion Classifier ────────────────────────────────────
CNN_MODEL_PATH = "models/congestion_cnn.pth"
CNN_INPUT_SIZE = (224, 224)
CNN_CLASSES = ["free_flow", "moderate", "congested", "severe"]
CNN_CONFIDENCE_MIN = 0.6

# ─── Speed Estimation ────────────────────────────────────────────
PIXELS_PER_METER = 10.0                 # calibrate per camera
FPS = 30                                # assumed / actual capture FPS

# ─── Logging & Output ────────────────────────────────────────────
LOG_DIR = "logs"
OUTPUT_DIR = "outputs"
SAVE_ANNOTATED_FRAMES = True
DISPLAY_WINDOW = True

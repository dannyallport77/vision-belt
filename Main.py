"""
Vision Belt Prototype - Main Pipeline

Dependencies:
  - Python 3.8+
  - pyrealsense2
  - opencv-python
  - numpy
  - pyyaml
  - bleak  # for BLE communication (future integration)
  - pyttsx3 or gTTS  # for TTS (future integration)
  - websocket-client  # for data publishing (future integration)
  - argparse (built-in)
  - logging (built-in)

To install dependencies:
```bash
pip install pyrealsense2 opencv-python numpy pyyaml bleak pyttsx3 websocket-client
```
"""
import argparse
import logging
import yaml
import numpy as np
import cv2
import pyrealsense2 as rs

# =============================================
# Vision Belt Prototype - Main Pipeline
# TODO: Implement additional modules for:
#   - Object classification (signage, stairs, trip hazards)
#   - BLE communication layer for haptic motors
#   - TTS/audio library integration for mobile feedback
#   - Logging and session management
#   - Data publishing via WebSocket or REST
# =============================================

# Configure logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Placeholder functions for feedback
def send_haptic(direction: str, strength: float):
    """
    Send haptic feedback via BLE to vibration motors.
    TODO:
      - Integrate Bluetooth Low Energy library (e.g., bleak)
      - Map strength to PWM values for actuator control
    """
    # Debug print (comment out or replace with actual BLE call)
    # logger.debug(f"Haptic: {direction} (strength={strength:.2f})")


def send_audio(message: str):
    """
    Send audio feedback via mobile device.
    TODO:
      - Integrate TTS engine (e.g., pyttsx3, gTTS)
      - Stream audio over BLE or mobile speaker
    """
    # Debug print (comment out or replace with actual TTS call)
    # logger.debug(f"Audio: {message}")


def main(config_path: str):
    # Validate config file path and handle errors
    try:
        with open(config_path, 'r') as f:
            cfg = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        return

    # ===== Configure RealSense pipeline =====
    pipeline = rs.pipeline()
    config = rs.config()
    # TODO: Expose camera selection in config (multiple devices)
    config.enable_stream(rs.stream.depth,
                         cfg['depth']['width'],
                         cfg['depth']['height'],
                         rs.format.z16,
                         cfg['depth']['fps'])
    config.enable_stream(rs.stream.color,
                         cfg['color']['width'],
                         cfg['color']['height'],
                         rs.format.bgr8,
                         cfg['color']['fps'])
    profile = pipeline.start(config)

    # Align depth frames to color frames
    align_to = rs.stream.color
    align = rs.align(align_to)

    logger.info("Vision Belt pipeline started.")
    try:
        while True:
            frames = pipeline.wait_for_frames()
            aligned = align.process(frames)
            depth_frame = aligned.get_depth_frame()
            color_frame = aligned.get_color_frame()
            if not depth_frame or not color_frame:
                continue

            # Convert frames to numpy arrays
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())

            # TODO: Implement advanced obstacle detection and classification
            # Simple proximity detection: find nearest non-zero depth
            valid_depths = depth_image[np.nonzero(depth_image)]
            if valid_depths.size == 0:
                continue
            min_dist = np.min(valid_depths) * cfg['depth']['scale']
            h, w = depth_image.shape
            cy, cx = np.unravel_index(np.argmin(depth_image), depth_image.shape)
            if cx < w/3:
                direction = 'left'
            elif cx > 2*w/3:
                direction = 'right'
            else:
                direction = 'center'

            # Provide feedback if within threshold
            if min_dist < cfg['feedback']['distance_threshold']:
                strength = (cfg['feedback']['distance_threshold'] - min_dist) / cfg['feedback']['distance_threshold']
                send_haptic(direction, strength)
                send_audio(f"Obstacle {direction}, {min_dist:.2f} meters away")

            # TODO: Publish raw data over WebSocket or REST for mobile app

            # Display for debugging
            depth_colormap = cv2.applyColorMap(
                cv2.convertScaleAbs(depth_image, alpha=0.03),
                cv2.COLORMAP_JET)
            images = np.hstack((color_image, depth_colormap))
            cv2.imshow('Vision Belt Debug', images)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        pipeline.stop()
        cv2.destroyAllWindows()
        logger.info("Vision Belt pipeline stopped.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Vision Belt object detection prototype')
    parser.add_argument('--config', type=str,
                        default='config/settings.yaml',
                        help='Path to YAML settings file')
    args = parser.parse_args()
    # TODO: Add argument for test mode / unit tests
    main(args.config)

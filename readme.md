# Vision Belt

An open-source wearable system designed to provide real-time environmental feedback to visually impaired individuals through auditory and tactile cues.

## Vision Statement

> To empower visually impaired individuals with intuitive, real-time environmental awareness through accessible, open-source wearable technology.

## Features

* **3D Object Detection**: Uses depth-sensing cameras to detect obstacles, signage, and terrain changes in the user’s surroundings.
* **Haptic Feedback**: Belt-mounted vibration motors convey directional and proximity information through distinct patterns.
* **Auditory Cues**: Bluetooth-connected bone-conduction headphones provide verbal alerts and descriptions.
* **Mobile App Integration**: A companion mobile application handles processing, configuration, and logging of environmental data.
* **Open-Source**: Fully open-source under the MIT license, encouraging community contributions and enhancements.

## Hardware Requirements

* Intel RealSense D415 (or equivalent) depth-sensing cameras (minimum 2 units).
* Microcontroller or smartphone supporting USB-C/USB-A video input for camera streams.
* Vibration motors (coin or linear resonant actuators) and driver circuitry.
* Rechargeable battery pack (5V output) with at least 10,000mAh capacity.
* Belt or harness to mount cameras and vibration modules securely and comfortably.
* Bluetooth-enabled bone-conduction headphones or speaker.

## Software Requirements

* **Mobile Device**: Android 9.0+ or iOS 14.0+ with USB-C/Lightning video input support.
* **Development Environment**:

  * Python 3.8+ for prototyping vision algorithms.
  * OpenCV and Intel RealSense SDK (if using RealSense cameras).
  * Node.js 14+ and React Native (or Flutter) for mobile app development.
* **Libraries**:

  * TensorFlow Lite or PyTorch Mobile for on-device ML inference.
  * Bluetooth Low Energy (BLE) library for mobile platforms.

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/dannyallport77/vision-belt.git
   cd vision-belt
   ```
2. **Install Dependencies**:

   * Backend (Python vision prototype):

     ```bash
     pip install -r requirements.txt
     ```
   * Mobile App:

     ```bash
     cd mobile-app
     npm install
     ```
3. **Configure Cameras**:

   * Connect depth cameras to the processing device and verify streams:

     ```bash
     python src/vision/stream_test.py
     ```
4. **Run Vision Prototype**:

   ```bash
   python src/vision/main.py --config config/settings.yaml
   ```
5. **Launch Mobile App**:

   ```bash
   cd mobile-app
   npm run android   # or npm run ios
   ```

## Usage

1. Wear the belt and secure the cameras at hip level facing forward and backward.
2. Power on the system and pair your Bluetooth headphones with the mobile device.
3. Open the Vision Belt mobile app and select **Start Session**.
4. Begin walking; obstacles and hazards will trigger haptic and auditory feedback.

## Contribution Guidelines

We welcome contributions from developers, researchers, and users:

1. Fork the repository and create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and add tests where applicable.
3. Commit your changes:

   ```bash
   git commit -m "Add feature: describe your feature"
   ```
4. Push to your fork and submit a Pull Request.

Please read our [CODE\_OF\_CONDUCT.md](CODE_OF_CONDUCT.md) for community guidelines.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please open an issue or reach out to the maintainers at [vision-belt@example.com](mailto:vision-belt@example.com).

# Smart Traffic Management System — Test Plan

## 1. Purpose

This test plan describes how to evaluate the vehicle-detection software, traffic-demand logic, and Arduino LED prototype.

## 2. Software Tests

| Test | Procedure | Expected result |
|---|---|---|
| Video input | Open a valid traffic video | Video frames are processed |
| Invalid input | Supply a nonexistent video path | A clear error is reported |
| Vehicle detection | Run the pretrained YOLO model on traffic footage | Vehicle detections are displayed when recognized |
| Traffic demand | Test with different vehicle counts | Green time stays within configured limits |
| Equal demand | Provide equal counts for both approaches | The configured tie-breaking rule is applied |

## 3. Arduino Tests

1. Inspect all LED connections and resistors before powering the board.
2. Upload the Arduino sketch.
3. Confirm both approaches start with red LEDs.
4. Confirm the North–South approach changes from green to yellow and then red.
5. Confirm the East–West approach then changes from red to green to yellow.
6. Confirm both approaches are red during the transition intervals.
7. Repeat the cycle and check for unexpected LED states.

## 4. Safety Checks

- Use only a low-voltage tabletop LED setup.
- Never connect this prototype to real traffic infrastructure.
- Disconnect power before changing circuit connections.

## 5. Results Record

Record the date, test setup, observed result, pass/fail status, and any errors for each test.

| Test | Observed result | Status | Notes |
|---|---|---|---|
| Video input | Not tested yet | Pending | |
| Vehicle detection | Not tested yet | Pending | |
| Traffic-demand logic | Not tested yet | Pending | |
| Arduino LED sequence | Not tested yet | Pending | |

## 6. Limitations

Results must be recorded only after running each test. Expected results in this document are not proof that the system has passed testing.

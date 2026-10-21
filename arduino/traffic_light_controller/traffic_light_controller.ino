/*
  Smart Traffic Management System
  Low-voltage LED prototype for two traffic approaches.
  For educational use only; not for real road signals.
*/

const int NS_RED = 3;
const int NS_YELLOW = 4;
const int NS_GREEN = 5;

const int EW_RED = 6;
const int EW_YELLOW = 7;
const int EW_GREEN = 8;

const unsigned long GREEN_TIME = 5000;
const unsigned long YELLOW_TIME = 2000;
const unsigned long ALL_RED_TIME = 1000;

void setLights(
  bool nsRed, bool nsYellow, bool nsGreen,
  bool ewRed, bool ewYellow, bool ewGreen
) {
  digitalWrite(NS_RED, nsRed);
  digitalWrite(NS_YELLOW, nsYellow);
  digitalWrite(NS_GREEN, nsGreen);

  digitalWrite(EW_RED, ewRed);
  digitalWrite(EW_YELLOW, ewYellow);
  digitalWrite(EW_GREEN, ewGreen);
}

void setup() {
  pinMode(NS_RED, OUTPUT);
  pinMode(NS_YELLOW, OUTPUT);
  pinMode(NS_GREEN, OUTPUT);

  pinMode(EW_RED, OUTPUT);
  pinMode(EW_YELLOW, OUTPUT);
  pinMode(EW_GREEN, OUTPUT);

  // Start safely with both approaches red.
  setLights(HIGH, LOW, LOW, HIGH, LOW, LOW);
  delay(ALL_RED_TIME);
}

void loop() {
  // North-South green; East-West red.
  setLights(LOW, LOW, HIGH, HIGH, LOW, LOW);
  delay(GREEN_TIME);

  // North-South yellow; East-West remains red.
  setLights(LOW, HIGH, LOW, HIGH, LOW, LOW);
  delay(YELLOW_TIME);

  // Both approaches red before switching.
  setLights(HIGH, LOW, LOW, HIGH, LOW, LOW);
  delay(ALL_RED_TIME);

  // East-West green; North-South red.
  setLights(HIGH, LOW, LOW, LOW, LOW, HIGH);
  delay(GREEN_TIME);

  // East-West yellow; North-South remains red.
  setLights(HIGH, LOW, LOW, LOW, HIGH, LOW);
  delay(YELLOW_TIME);

  // Both approaches red before repeating.
  setLights(HIGH, LOW, LOW, HIGH, LOW, LOW);
  delay(ALL_RED_TIME);
}

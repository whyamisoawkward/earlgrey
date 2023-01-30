//control code for stepper motors in 3d Scanner
//full project and instructions can be found on
//http://whyamisoawkward.com/
#include <Stepper.h>

String     inputString = "help\n"; // a string to hold incoming data
boolean stringComplete = true;     // whether the string is completet
boolean        ComData = false;    // whether com data is on when motors are moving will slow them down

// Define stepper motor connections and steps per revolution:
#define yaxisdirPin 2
#define yaxisstepPin 3
#define platteraxisdirPin 4
#define platteraxisstepPin 5
#define zaxisdirPin 6
#define zaxisstepPin 7
#define tiltaxisdirPin 8
#define tiltaxisstepPin 9
#define stepsetting1 400
#define stepsetting2 800
#define stepsetting3 1600
#define stepsetting4 2400
#define STEPS 50

Stepper stepper(STEPS, 10, 12, 11, 13);

void setup() {
  // Declare pins as output:
  pinMode(yaxisstepPin, OUTPUT);
  pinMode(yaxisdirPin, OUTPUT);
  pinMode(platteraxisstepPin, OUTPUT);
  pinMode(platteraxisdirPin, OUTPUT);
  pinMode(zaxisstepPin, OUTPUT);
  pinMode(zaxisdirPin, OUTPUT);
  pinMode(tiltaxisstepPin, OUTPUT);
  pinMode(tiltaxisdirPin, OUTPUT);
  
  
  // initialize the serial port:
  Serial.begin(115200);
}

void serialEvent()// ********************************************************      Serial in
{ while (Serial.available()) 
  {
    char inChar = (char)Serial.read();            // get the new byte:
    if (inChar > 0)     {inputString += inChar;}  // add it to the inputString:
    if (inChar == '\n') { stringComplete = true;} // if the incoming character is a newline, set a flag so the main loop can do something about it: 
  }
}

void zaxisstepup1() {

  // Set the spinning direction clockwise:
  digitalWrite(zaxisdirPin, HIGH);

  // Spin the zaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting1; i++) {
    // These four lines result in 1 zaxisstep:
    digitalWrite(zaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(zaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void zaxisstepdown1() {

  // Set the spinning direction clockwise:
  digitalWrite(zaxisdirPin, LOW);

  // Spin the zaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting1; i++) {
    // These four lines result in 1 zaxisstep:
    digitalWrite(zaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(zaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void zaxisstepup2() {

  // Set the spinning direction clockwise:
  digitalWrite(zaxisdirPin, HIGH);

  // Spin the zaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting2; i++) {
    // These four lines result in 1 zaxisstep:
    digitalWrite(zaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(zaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void zaxisstepdown2() {

  // Set the spinning direction clockwise:
  digitalWrite(zaxisdirPin, LOW);

  // Spin the zaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting2; i++) {
    // These four lines result in 1 zaxisstep:
    digitalWrite(zaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(zaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void zaxisstepup3() {

  // Set the spinning direction clockwise:
  digitalWrite(zaxisdirPin, HIGH);

  // Spin the zaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting3; i++) {
    // These four lines result in 1 zaxisstep:
    digitalWrite(zaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(zaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void zaxisstepdown3() {

  // Set the spinning direction clockwise:
  digitalWrite(zaxisdirPin, LOW);

  // Spin the zaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting3; i++) {
    // These four lines result in 1 zaxisstep:
    digitalWrite(zaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(zaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void zaxisstepup4() {

  // Set the spinning direction clockwise:
  digitalWrite(zaxisdirPin, HIGH);

  // Spin the zaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting4; i++) {
    // These four lines result in 1 zaxisstep:
    digitalWrite(zaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(zaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void zaxisstepdown4() {

 // Set the spinning direction clockwise:
  digitalWrite(zaxisdirPin, LOW);

  // Spin the zaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting4; i++) {
    // These four lines result in 1 zaxisstep:
    digitalWrite(zaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(zaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }
    

void yaxisstepup1() {

  // Set the spinning direction clockwise:
  digitalWrite(yaxisdirPin, HIGH);

  // Spin the yaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting1; i++) {
    // These four lines result in 1 yaxisstep:
    digitalWrite(yaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(yaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void yaxisstepdown1() {

  // Set the spinning direction clockwise:
  digitalWrite(yaxisdirPin, LOW);

  // Spin the yaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting1; i++) {
    // These four lines result in 1 yaxisstep:
    digitalWrite(yaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(yaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void yaxisstepup2() {

  // Set the spinning direction clockwise:
  digitalWrite(yaxisdirPin, HIGH);

  // Spin the yaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting2; i++) {
    // These four lines result in 1 yaxisstep:
    digitalWrite(yaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(yaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void yaxisstepdown2() {

  // Set the spinning direction clockwise:
  digitalWrite(yaxisdirPin, LOW);

  // Spin the yaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting2; i++) {
    // These four lines result in 1 yaxisstep:
    digitalWrite(yaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(yaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void yaxisstepup3() {

  // Set the spinning direction clockwise:
  digitalWrite(yaxisdirPin, HIGH);

  // Spin the yaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting3; i++) {
    // These four lines result in 1 yaxisstep:
    digitalWrite(yaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(yaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void yaxisstepdown3() {

  // Set the spinning direction clockwise:
  digitalWrite(yaxisdirPin, LOW);

  // Spin the yaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting3; i++) {
    // These four lines result in 1 yaxisstep:
    digitalWrite(yaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(yaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void yaxisstepup4() {

  // Set the spinning direction clockwise:
  digitalWrite(yaxisdirPin, HIGH);

  // Spin the yaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting4; i++) {
    // These four lines result in 1 yaxisstep:
    digitalWrite(yaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(yaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void yaxisstepdown4() {

 // Set the spinning direction clockwise:
  digitalWrite(yaxisdirPin, LOW);

  // Spin the yaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting4; i++) {
    // These four lines result in 1 yaxisstep:
    digitalWrite(yaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(yaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void platteraxisstepup1() {

  // Set the spinning direction clockwise:
  digitalWrite(platteraxisdirPin, HIGH);

  // Spin the platteraxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting1; i++) {
    // These four lines result in 1 platteraxisstep:
    digitalWrite(platteraxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(platteraxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void platteraxisstepdown1() {

  // Set the spinning direction clockwise:
  digitalWrite(platteraxisdirPin, LOW);

  // Spin the platteraxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting1; i++) {
    // These four lines result in 1 platteraxisstep:
    digitalWrite(platteraxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(platteraxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void platteraxisstepup2() {

  // Set the spinning direction clockwise:
  digitalWrite(platteraxisdirPin, HIGH);

  // Spin the platteraxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting2; i++) {
    // These four lines result in 1 platteraxisstep:
    digitalWrite(platteraxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(platteraxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void platteraxisstepdown2() {

  // Set the spinning direction clockwise:
  digitalWrite(platteraxisdirPin, LOW);

  // Spin the platteraxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting2; i++) {
    // These four lines result in 1 platteraxisstep:
    digitalWrite(platteraxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(platteraxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void platteraxisstepup3() {

  // Set the spinning direction clockwise:
  digitalWrite(platteraxisdirPin, HIGH);

  // Spin the platteraxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting3; i++) {
    // These four lines result in 1 platteraxisstep:
    digitalWrite(platteraxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(platteraxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void platteraxisstepdown3() {

  // Set the spinning direction clockwise:
  digitalWrite(platteraxisdirPin, LOW);

  // Spin the platteraxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting3; i++) {
    // These four lines result in 1 platteraxisstep:
    digitalWrite(platteraxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(platteraxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void platteraxisstepup4() {

  // Set the spinning direction clockwise:
  digitalWrite(platteraxisdirPin, HIGH);

  // Spin the platteraxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting4; i++) {
    // These four lines result in 1 platteraxisstep:
    digitalWrite(platteraxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(platteraxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void platteraxisstepdown4() {

 // Set the spinning direction clockwise:
  digitalWrite(platteraxisdirPin, LOW);

  // Spin the platteraxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting4; i++) {
    // These four lines result in 1 platteraxisstep:
    digitalWrite(platteraxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(platteraxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }
    
  void idplatteraxisstepper() {
    Serial.print("1");



  
  delay(0);
  inputString="";
    }



void tiltaxisstepup1() {

  // Set the spinning direction clockwise:
  digitalWrite(tiltaxisdirPin, HIGH);

  // Spin the tiltaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting1; i++) {
    // These four lines result in 1 tiltaxisstep:
    digitalWrite(tiltaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(tiltaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void tiltaxisstepdown1() {

  // Set the spinning direction clockwise:
  digitalWrite(tiltaxisdirPin, LOW);

  // Spin the tiltaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting1; i++) {
    // These four lines result in 1 tiltaxisstep:
    digitalWrite(tiltaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(tiltaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void tiltaxisstepup2() {

  // Set the spinning direction clockwise:
  digitalWrite(tiltaxisdirPin, HIGH);

  // Spin the tiltaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting2; i++) {
    // These four lines result in 1 tiltaxisstep:
    digitalWrite(tiltaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(tiltaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void tiltaxisstepdown2() {

  // Set the spinning direction clockwise:
  digitalWrite(tiltaxisdirPin, LOW);

  // Spin the tiltaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting2; i++) {
    // These four lines result in 1 tiltaxisstep:
    digitalWrite(tiltaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(tiltaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void tiltaxisstepup3() {

  // Set the spinning direction clockwise:
  digitalWrite(tiltaxisdirPin, HIGH);

  // Spin the tiltaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting3; i++) {
    // These four lines result in 1 tiltaxisstep:
    digitalWrite(tiltaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(tiltaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void tiltaxisstepdown3() {

  // Set the spinning direction clockwise:
  digitalWrite(tiltaxisdirPin, LOW);

  // Spin the tiltaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting3; i++) {
    // These four lines result in 1 tiltaxisstep:
    digitalWrite(tiltaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(tiltaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }

void tiltaxisstepup4() {

  // Set the spinning direction clockwise:
  digitalWrite(tiltaxisdirPin, HIGH);

  // Spin the tiltaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting4; i++) {
    // These four lines result in 1 tiltaxisstep:
    digitalWrite(tiltaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(tiltaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
}

    void tiltaxisstepdown4() {

 // Set the spinning direction clockwise:
  digitalWrite(tiltaxisdirPin, LOW);

  // Spin the tiltaxisstepper motor 1 revolution quickly:
  for (int i = 0; i < stepsetting4; i++) {
    // These four lines result in 1 tiltaxisstep:
    digitalWrite(tiltaxisstepPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(tiltaxisstepPin, LOW);
    delayMicroseconds(100);
  }

  delay(0);
  inputString="";
    }
    
void panleft1() {

  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  delay(0);
  inputString="";
}

void panright1() {
  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  delay(0);
  inputString="";
    }

void panleft2() {

  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  delay(0);
  inputString="";
}

void panright2() {

  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  delay(0);
  inputString="";
    }

void panleft3() {

  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  delay(0);
  inputString="";
}

void panright3() {

  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  delay(0);
  inputString="";
    }

void panleft4() {

  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(50); // do 50 steps – corresponds to one revolution in one minute
  delay(0);
  inputString="";
}

void panright4() {

  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  stepper.setSpeed(100); // 10 rpm
  stepper.step(-50); // do 50 steps – corresponds to one revolution in one minute
  delay(0);
  inputString="";
    }

    
//commands to send to stepper motor u for a step up and d for a step down
   void loop()  // **************************************************************     loop
{
 serialEvent(); 
 if (stringComplete) 
 {
  if (inputString=="u1\n")      {zaxisstepup1();}
  if (inputString=="d1\n")     {zaxisstepdown1();}
  if (inputString=="u2\n")      {zaxisstepup2();}
  if (inputString=="d2\n")     {zaxisstepdown2();}
  if (inputString=="u3\n")      {zaxisstepup3();}
  if (inputString=="d3\n")     {zaxisstepdown3();}
  if (inputString=="u4\n")      {zaxisstepup4();}
  if (inputString=="d4\n")     {zaxisstepdown4();} 
  if (inputString=="f1\n")      {yaxisstepup1();}
  if (inputString=="b1\n")     {yaxisstepdown1();}
  if (inputString=="f2\n")      {yaxisstepup2();}
  if (inputString=="b2\n")     {yaxisstepdown2();}
  if (inputString=="f3\n")      {yaxisstepup3();}
  if (inputString=="b3\n")     {yaxisstepdown3();}
  if (inputString=="f4\n")      {yaxisstepup4();}
  if (inputString=="b4\n")     {yaxisstepdown4();}
  if (inputString=="r1\n")      {tiltaxisstepup1();}
  if (inputString=="s1\n")     {tiltaxisstepdown1();}
  if (inputString=="r2\n")      {tiltaxisstepup2();}
  if (inputString=="s2\n")     {tiltaxisstepdown2();}
  if (inputString=="r3\n")      {tiltaxisstepup3();}
  if (inputString=="s3\n")     {tiltaxisstepdown3();}
  if (inputString=="r4\n")      {tiltaxisstepup4();}
  if (inputString=="s4\n")     {tiltaxisstepdown4();}
  if (inputString=="q1\n")      {platteraxisstepup1();}
  if (inputString=="t1\n")     {platteraxisstepdown1();}
  if (inputString=="q2\n")      {platteraxisstepup2();}
  if (inputString=="t2\n")     {platteraxisstepdown2();}
  if (inputString=="q3\n")      {platteraxisstepup3();}
  if (inputString=="t3\n")     {platteraxisstepdown3();}
  if (inputString=="q4\n")      {platteraxisstepup4();}
  if (inputString=="t4\n")     {platteraxisstepdown4();}
  if (inputString=="y1\n")      {panleft1();}
  if (inputString=="x1\n")     {panright1();}
  if (inputString=="y2\n")      {panleft2();}
  if (inputString=="x2\n")     {panright2();}
  if (inputString=="y3\n")      {panleft3();}
  if (inputString=="x3\n")     {panright3();}
  if (inputString=="y4\n")      {panleft4();}
  if (inputString=="x4\n")     {panright4();} 
  
  inputString = ""; stringComplete = false; // clear the string:
 }

}


//arduino piano



int gPin = A0; // FSR is connected to analog 0
int fPin = A1; 
int ePin = A2; 
int dPin = A3; 
int cPin = A4; 
int speakerPin = 8;      // connect Red LED to pin 11 (PWM pin)
int fsrReading;      // the analog reading from the FSR resistor divider

char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };
 
void setup(void) {
  Serial.begin(9600);   // We'll send debugging information via the Serial monitor
}
 
void loop(void) {
   fsrReading=-1;
/*
  if(analogRead(gPin)>10)
        fsrReading = 4;
  if(analogRead(fPin)>10)
        fsrReading = 3;
if(analogRead(ePin)>10)
        fsrReading = 2;
 if(analogRead(dPin)>10)
        fsrReading = 1;
if(analogRead(cPin)>10)
        fsrReading = 0;
*/
        
  Serial.print("Analog reading = ");
  Serial.println(fsrReading);

 if( fsrReading>-1)
  tone(speakerPin, tones[fsrReading],1000);
 
  delay(100);
}


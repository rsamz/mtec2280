
int counter = 0;

long pMillis = 0;

int interval = 10;

const int ledPin[] = {10,8,6,2};
int x = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(ledPin[x],OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (millis() - pMillis >= interval) {
    pMillis = millis();
    counter++;
    //Serial.println(counter);
  }

  analogWrite(ledPin[x], counter);

      Serial.println(x);
  //}
  if(counter >= 225){
    counter = 0;
    if(x<4){
  x++;
    }
  }

}

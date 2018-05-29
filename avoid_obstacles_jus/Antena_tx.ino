#include <VirtualWire.h>

const int Boton1 = 7;
const int Boton2 = 4;
const int Antena = 2;

enum TypeState {
  voz,
  manual,
  avanzar,
  parar
};

bool statewaschanged(TypeState actual_state, TypeState next_state)
{
  return actual_state != next_state;
}

void changestate1(TypeState actual, TypeState &next)
{
  if(actual == voz){
    next = manual;
  }else{
    next = voz;
  }
}

void changestate2(TypeState actual, TypeState &next)
{
  if(actual == manual){
    next = avanzar;
  }else if(actual == avanzar){
    next = parar;
  }else if(actual == parar){
    next = avanzar;
  }
}

TypeState actual_state = voz;
TypeState next_state = manual;
int btn1 = 0;
int btn2 = 0;
char dato[1];



void setup() {
  pinMode(Boton1, INPUT);
  pinMode(Boton2, INPUT);
  Serial.begin(9600);
  
  vw_setup(2000); // velocidad: Bits per segundo
  vw_set_tx_pin(Antena); //Pin 2 como salida para el RF 
}

void loop() {
 
  btn1 = digitalRead(Boton1);
  btn2 = digitalRead(Boton2);
  
  if(btn1 == HIGH){
    changestate1(actual_state, next_state);
  }else if(btn2 == HIGH){
    changestate2(actual_state, next_state);
  }
  
  if(statewaschanged(actual_state, next_state)){
    if(next_state == voz){
      dato[0] = 'v';
    }else if(next_state == manual){
      dato[0] = 'm';
    }else if(next_state == avanzar){
      dato[0] = 'a';
    }else{
      dato[0] = 'p';
    }
    vw_send((uint8_t*)dato,sizeof(dato));
    vw_wait_tx();
  }
  actual_state = next_state;
  delay(200);

}


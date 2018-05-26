#include <Servo.h>

Servo servomotor;  // crea un objeto tipo servo para controlar el servomotor 

const int VinFrenteDcho = 23;
const int GndFrenteDcho = 25;
const int VinRearDcho = 22;                                                                    
const int GndRearDcho = 24;

const int VinFrenteIzq = 33;
const int GndFrenteIzq = 35;
const int VinRearIzq = 32;
const int GndRearIzq = 34;

const int ServoM = 2;

const int Salida = 9;
const int Entrada = 8;

int pos;
long dist;
long tiempo;

void leerdist()
{
  digitalWrite(Salida,LOW);
  delayMicroseconds(5);
  digitalWrite(Salida, HIGH); 
  delayMicroseconds(10);
  tiempo=pulseIn(Entrada, HIGH); 
  dist= int(0.017*tiempo);
  Serial.println(dist);
}

 void initservofrente()
 {
   
   for(pos = 0; pos < 91; pos += 1){
    
     servomotor.write(pos);
   
    delay(15);
  }
   
 }
 
 void moveservoizq()
 {
   
   for(pos = pos; pos < 180; pos += 1){
    
     servomotor.write(pos);
   
     delay(15);
   }
   
 }
 
 void moveservodcha()
 {
   for(pos = pos; pos > 0; pos -= 1){
    
     servomotor.write(pos);
   
     delay(15);
   }
 }
 
 //AVANZAR AL FRENTE
 
 void avanzarfrente()
 {
   
    digitalWrite(VinFrenteDcho, HIGH);
    digitalWrite(GndFrenteDcho, HIGH);
 
    digitalWrite(VinFrenteIzq, HIGH);
    digitalWrite(GndFrenteIzq, HIGH);
    
    delay(140);
    
    digitalWrite(VinFrenteIzq, LOW);
    digitalWrite(GndFrenteIzq, LOW);
    
    delay(25);
    
    digitalWrite(VinFrenteIzq, HIGH);
    digitalWrite(GndFrenteIzq, HIGH);
 }
 
 //GIRAR A LA IZQUIERDA
 
 void girarizq()
 {
    //oruga izquierda hacia atras:
    
    digitalWrite(VinRearIzq, HIGH);
    digitalWrite(GndRearIzq, HIGH);
    
    //oruga dcha hacia delante:
    digitalWrite(VinFrenteDcho, HIGH);
    digitalWrite(GndFrenteDcho, HIGH);
    
    delay(1100);
 }
 
 //GIRAR A LA DERECHA  
 
 void girardcha()
 {
   //oruga derecha hacia atras:
   
   digitalWrite(VinRearDcho, HIGH);
   digitalWrite(GndRearDcho, HIGH);
   
   //oruga izquierda hacia delante
   
   digitalWrite(VinFrenteIzq, HIGH);
   digitalWrite(GndFrenteIzq, HIGH);
   
   delay(1100);
 }
 
 //AVANZAR HACIA ATRAS
 
 void avanzaratras()
 {
   //Los dos motores hacia atras:
   
   digitalWrite(GndRearDcho, HIGH);
   digitalWrite(VinRearDcho, HIGH);
  
   digitalWrite(GndRearIzq, HIGH);
   digitalWrite(VinRearIzq, HIGH);
   delay(2200);
   
   //giro de escape del callejon:
   
   stopmotors();
   delay(1000);
   
   //oruga izquierda hacia atras:
    
    digitalWrite(VinRearIzq, HIGH);
    digitalWrite(GndRearIzq, HIGH);
    
    //oruga dcha hacia delante:
    digitalWrite(VinFrenteDcho, HIGH);
    digitalWrite(GndFrenteDcho, HIGH);
    
    delay(2000);
 }
 
 void stopmotors()
 {
   digitalWrite(VinFrenteDcho, LOW);
   digitalWrite(GndFrenteDcho, LOW);
  
   digitalWrite(VinFrenteIzq, LOW);
   digitalWrite(GndFrenteIzq, LOW);
  
   digitalWrite(GndRearDcho, LOW);
   digitalWrite(VinRearDcho, LOW);
  
   digitalWrite(GndRearIzq, LOW);
   digitalWrite(VinRearIzq, LOW);
  
 }

void setup(){
 
 pinMode(VinFrenteDcho, OUTPUT);
 pinMode(GndFrenteDcho, OUTPUT);
 pinMode(VinRearDcho, OUTPUT);
 pinMode(GndRearDcho, OUTPUT);
 
 pinMode(VinFrenteIzq, OUTPUT);
 pinMode(GndFrenteIzq, OUTPUT);
 pinMode(VinRearIzq, OUTPUT);
 pinMode(GndRearIzq, OUTPUT);
 
  pinMode(Salida, OUTPUT);
  pinMode(Entrada, INPUT);
 
 servomotor.attach(ServoM);
 
 Serial.begin(9600);
 
 
 initservofrente();   //Colocar el servo mirando hacia el frente
  
}

void loop(){
  
  leerdist();
  
  delay(10);
  
  while(dist > 20){
    
   avanzarfrente(); 
   delay(100);
   stopmotors();
   delay(10);
   leerdist();
   delay(10);
   
  }
  //Estoy en el caso de que he detectado un obstaculo delante:
  
  stopmotors();
  
  //Leer a la izquierda
  moveservoizq();
  leerdist();
  delay(10);
  if(dist > 25){
    initservofrente();
    girarizq(); 
  }else{
    
    moveservodcha();
    leerdist();
    delay(10);
    
    if(dist > 25){
       initservofrente();
       girardcha(); 
    }else{
       initservofrente();
       avanzaratras(); 
    
    }
  }
   stopmotors();
   delay(300);                                                                                                                                                                                  
}

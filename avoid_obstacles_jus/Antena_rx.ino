#include <VirtualWire.h>

char data_received = 'p';

void setup()
{
    Serial.begin(9600);
    Serial.println("setup");

    //Se inicializa el RF
    vw_setup(2000);  //velocidad: Bits per segundo
    vw_set_rx_pin(2);
    vw_rx_start();
    
    pinMode(13, OUTPUT);
    pinMode(7, OUTPUT);
    digitalWrite(13, false);
    digitalWrite(7, false);
}

void loop()
{
    uint8_t dato;
    uint8_t datoleng=1;
    //verifico si hay un dato valido en el RF
    if (vw_get_message(&dato,&datoleng))
    {
        if((char)dato=='v')
        {
            digitalWrite(13, true);
            digitalWrite(7, false);
            data_received = 'v';

        }
        else if((char)dato=='m')
        {
            digitalWrite(13, false);
            data_received = 'm';

        }
        else if((char)dato=='a')
        {
            digitalWrite(7, true);
            digitalWrite(13, false);
            data_received = 'a';

        } 
        else if((char)dato=='p')
        {
            digitalWrite(7, false);
            digitalWrite(13, false);
            data_received = 'p';

        }           
    }
    Serial.print(data_received);
    delay(20);
}

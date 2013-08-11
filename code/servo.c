#include <wiringPi.h>
#include <stdlib.h>
main (int argc,char *argv[])
{
  int pin=1;
  int min=500,max=2400,wait;
  int deg;
  int i;
  
  if(argc<3)
    return 1;
  else{
    deg=atoi(argv[2]);
    pin=atoi(argv[1]);
  }
  
  deg=deg<0?0:(deg>180?180:deg);
  wait=min+deg*(max-min)/180;

  wiringPiSetup () ;
  pinMode (pin, OUTPUT) ;

  for (i=0;i<18;i++)
  {
    digitalWrite (pin, LOW) ; 
    delayMicroseconds (wait) ;
    digitalWrite (pin, HIGH) ; 
    delayMicroseconds (20000-wait) ;
  }
  digitalWrite (pin, LOW) ; 
}

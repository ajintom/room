void setup() {
 
Serial.begin(9600);
pinMode(3,OUTPUT);
pinMode(4,OUTPUT);
pinMode(12,OUTPUT);

}

String strbuff="";

//String str;
char rec;

int pin1=12,pin2=12,status1=0,status2=0,gotonoff=0,gotpin=0,blinkstate=0,both=0,dimpin=0,max1=0,max2=0;


void func(String str)
  { Serial.flush();
    
    
    if ((str=="blue")&&(gotpin==0))
      {pin1=3;
      gotpin=1;}
      
      
     if ((str=="blue")&&(gotpin==1))
      pin2=3;
      
      if ((str=="rgb")&&(gotpin==0))
      {pin1=4;
      gotpin=1;}
      
     if ((str=="rgb")&&(gotpin==1))
      pin2=4;
      
      
   
      
    if (str=="both")
     { pin1=3;
      pin2=4;
      both=1;
      status1=status2;
      blinkstate=3;
      dimpin=3;
      }
    
    if ((str=="on")&&(gotonoff==0))
     { gotonoff=1;
     dimpin=1;
      status1=1;
      if (both==1) status2=1;
      max1=255;
  }
    if ((str=="on")&&(gotonoff==1))
      {
        
       status2=1;
       max2=255;
      }
      
      if ((str=="off")&&(gotonoff==0))
     { gotonoff=1;
     if (both==1) status2=0;
     dimpin=1;
      status1=0;}
    if ((str=="off")&&(gotonoff==1))
      status2=0;
      
      if ((str=="blink")&&(gotonoff==0))
        {blinkstate=1;
        gotonoff=1;
        }
        
        if ((str=="blink")&&(gotonoff==1))
        {blinkstate=2;
        gotonoff=1;
        }
        
        if ((str=="dim")&&(gotonoff==0))
        {blinkstate=1;
        gotonoff=1;
        dimpin=1;
        
        }
        
        if ((str=="dim")&&(gotonoff==1))
        {blinkstate=2;
        gotonoff=1;
        dimpin=2;
        }
        
        
        
        
      
      if (str=="execute")
      { 
             if (both==1)
       {
       digitalWrite(pin1,status1);
       digitalWrite(pin2,status1);
       return;
       }
    
       
        if (status1==0)
        for (int i=254;i>1;--i) { analogWrite(pin1,i); delay(5);}
        else if (status1==1)
        for (int i=1;i<254;++i) { analogWrite(pin1,i); delay(5);}
        
         if (status2==0)
        for (int i=254;i>1;--i) { analogWrite(pin2,i); delay(5);}
        else if (status2==1)
        for (int i=1;i<254;++i) { analogWrite(pin2,i); delay(5);}
        
      
       
        if (blinkstate==1)
          {
              while (1)
                 {if (Serial.read()=='\n') break;
                   digitalWrite(pin1,HIGH);
                   delay(300);
                   digitalWrite(pin1,LOW);
                   delay(300);
                   
                 }
              } 
            if (blinkstate==2)
            {while(1)
            { if (Serial.read()=='\n') break;
              digitalWrite(pin2,HIGH);
                   delay(300);
                   digitalWrite(pin2,LOW);
                   delay(300);
            }      
            }
             if (blinkstate==3)
            {while(1)
            { if (Serial.read()=='\n') break;
              digitalWrite(pin2,HIGH);
              digitalWrite(pin1,LOW);
                   delay(300);
                   digitalWrite(pin2,LOW);
                   digitalWrite(pin1,HIGH);
                   delay(300);
            }      
            }
                
          
        
        
        
        pin1=12,pin2=12,status1=0,status2=0,gotonoff=0,gotpin=0,blinkstate=0,both=0,dimpin=0,max1=0,max2=0;
        
        return;
      }
      
     
      
      
     
      
    
    
 
 
  
    
   Serial.flush();
  delay(10);
  
}


void loop()
{
  
  char str = ' ';
  while(Serial.available()>0)
  {
   
    
  rec=Serial.read();
  if (rec=='\n')
    {func(strbuff);
     strbuff="";
     
    }
   else
  { 
  strbuff+=rec ;
  }
  
    
  }

}
 
 

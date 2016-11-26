void setup() {
 
Serial.begin(9600);
pinMode(11,OUTPUT);
//pinMode(4,OUTPUT);
}
String flag1="";
String flag;
char rec;

void func( String flag)

  {
  if (flag=="blue")
    {digitalWrite(11,HIGH);
    digitalWrite(4,LOW);
    }
    if (flag=="rgb")
    {digitalWrite(4,HIGH);
    digitalWrite(3,LOW);
    } 
     if (flag=="blue123")
    { digitalWrite(3,HIGH);
      digitalWrite(4,HIGH);
    
    } 
     if (flag=="off")
    {digitalWrite(11,LOW);
    digitalWrite(3,LOW);
    } 
  
    
   Serial.flush();
  delay(100);
  
}


void loop()
{
 
  char str = ' ';
  while(Serial.available()>0)
  {
   
    
  rec=Serial.read();
  if (rec=='\n')
    {func(flag1);
     flag1="";
     
    }
   else
  { 
  flag1+=rec ;
  }
  
    
  }
  //Serial.println(flag);
}
  //Serial.println(str);
 

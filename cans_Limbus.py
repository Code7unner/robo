import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793

  def execMain(self):
    counter = 0

    brick.motor("M3").setPower(100)
    brick.motor("M4").setPower(100)
    
    script.wait(1000)
    
    while True:
      if counter == 8:
        brick.motor("M4").setPower(50)
        
        brick.motor("M3").setPower(-(50))
        script.wait(450)
        
        brick.motor("M3").setPower(100)
        brick.motor("M4").setPower(100)
        script.wait(4200)
        
        brick.motor("M3").powerOff()
        brick.motor("M4").powerOff()
        script.wait(5000)
        return
        
      if (brick.sensor("A1").read() > 45 or brick.sensor("A2").read() > 45):
        brick.motor("M3").setPower(100)
        
        brick.motor("M4").powerOff()
        
      else:
        brick.motor("M4").setPower(100)
        
        brick.motor("M3").powerOff()
        
      script.wait(11)
      
      if not (brick.sensor("D1").read() > 22):
        brick.motor("M3").setPower(100)
        brick.motor("M4").setPower(100)
        
        script.wait(325)
        
        brick.motor("M3").setPower(50)
        
        brick.motor("M4").setPower(-(50))
        
        script.wait(1000)
        
        brick.motor("M3").setPower(100)
        brick.motor("M4").setPower(100)
        
        script.wait(2800)
        
        counter = counter + 1
        
        while True:
          brick.motor("M3").setPower(-(100))
          
          brick.motor("M4").setPower(-(90))
          
          script.wait(1)
          
          if brick.sensor("A1").read() > 50 or brick.sensor("A2").read() > 50:
            break

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()

import RPi.GPIO as GPIO
import time
import argparse


class stepper:
    def __init__(self,IN1=11,IN2=12,IN3=13,IN4=15,mode=GPIO.BOARD,sleep_time = 0.01):
        '''
        IN1:        pin connected with IN1 pin of driver
        IN2:        pin connected with IN2 pin of driver
        IN3:        pin connected with IN3 pin of driver
        IN4:        pin connected with IN4 pin of driver
        mode:       mode of pi for pins
        sleep_time: Set according require RPM increace for less RPM and wise versa (min: 0.001 give approx 140 RPM)
        
        
        '''
        
        
        self.IN1 = IN1
        self.IN2 = IN2
        self.IN3 = IN3
        self.IN4 = IN4
        self.mode = mode
        self.slp_time = sleep_time 
        
        GPIO.setmode(self.mode)
        GPIO.setup(self.IN1,GPIO.OUT)
        GPIO.setup(self.IN2,GPIO.OUT)
        GPIO.setup(self.IN3,GPIO.OUT)
        GPIO.setup(self.IN4,GPIO.OUT)    
        

    def step_position(self,inp=[0,0,0,0]):
        
        GPIO.output(self.IN1,inp[1])
        GPIO.output(self.IN2,inp[3])
        GPIO.output(self.IN3,inp[0])
        GPIO.output(self.IN4,inp[2])
        time.sleep(self.slp_time)

    def drive(self,rotation=1):
        '''
        rotation: Number of rotation any number like 1, 2, 3, -1, 0.5, 0.2, -3.5
        '''
        
        
        print('Setting up....')
        
        self.step_position() #set initialy all pin LOW
        if rotation >= 0:
            step_index = [0,1,2,3,4,5,6,7] #position of step for clockwise direction
        else:
            step_index = [7,6,5,4,3,2,1,0] #reversing position of step
            rotation = -rotation
            
        print('motor running...')
        
        try:
            step_taken = 0
            tik = time.time()
            while step_taken < rotation * 400: #measure the steps
                
                if step_taken % 8 == step_index[0]:
                    self.step_position([1,0,0,0])
                    
                elif step_taken % 8 == step_index[1]:
                    self.step_position([1,1,0,0])
                    
                elif step_taken % 8 == step_index[2]:
                    self.step_position([0,1,0,0])
                    
                elif step_taken % 8 == step_index[3]:
                    self.step_position([0,1,1,0])
                    
                elif step_taken % 8 == step_index[4]:
                    self.step_position([0,0,1,0])
                
                elif step_taken % 8 == step_index[5]:
                    self.step_position([0,0,1,1])
                
                elif step_taken % 8 == step_index[6]:
                    self.step_position([0,0,0,1])
                    
                elif step_taken % 8 == step_index[7]:
                    self.step_position([1,0,0,1])
                
                step_taken += 1
            
            tok = time.time()
            print('Time taken {:.2f} sec'.format(tok -tik))
            print('cleaning....')
            GPIO.cleanup()
        
        except:
            print('cleaning....')
            GPIO.cleanup()
                
    


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-r", "--rotation", help="Number of rotation you want to turn motor",type = float, default = 1)
    parser.add_argument("--IN1",help='pin number connected with IN1 with stepper motor driver',type= int, default = 11)
    parser.add_argument("--IN2",help='pin number connected with IN2 with stepper motor driver',type= int, default = 12)
    parser.add_argument("--IN3",help='pin number connected with IN3 with stepper motor driver',type= int, default = 13)
    parser.add_argument("--IN4",help='pin number connected with IN4 with stepper motor driver',type= int, default = 15)
    args = parser.parse_args()
    
    
    drive = stepper(IN1=args.IN1 , IN2=args.IN2 , IN3=args.IN3 , IN4=args.IN4 , mode=GPIO.BOARD , sleep_time = 0.01)
    drive.drive(rotation=args.rotation) #for anticlockwise use "-" ex: -2
    

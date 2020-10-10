# stepper_motor_connection_with_pi_and_jetson_nano
How to connect and drive stepper motor with raspberry pi and jetson nano.  


 
# setup

1. Connect all jumper as shown in below image  

    <img src='https://www.electronicshub.org/wp-content/uploads/2018/02/Raspberry-Pi-Stepper-Motor-Control-using-L298N-Circuit-Diagram.jpg'>

2. 
    clone the repo

    ```
    git clone https://github.com/ravirajsinh45/stepper_motor_connection_with_pi_and_jetson_nano.git
    ```
    ```
    cd stepper_motor_connection_with_pi_and_jetson_nano 
    ```
3. Installing RPi.GPIO in Pi or nano. In jetson nano we also can install jetson.GPIO but RPi.GPIO also work in jetson.  

    ```
    pip3 install -r requirements.txt
    ```
4. Drive stepper motor from command line itself. 

    ```
    python3 stepper.py -r 1 --IN1 11 --IN2 12 --IN3 13 --IN4 15 
    ```

    -r : number of rotation (ex 0.25, 0.5, 1, 2, -1.5 etc)  
    --IN1: pin connected in pi with stepper motor driver's IN1  
    --IN2: pin connected in pi with stepper motor driver's IN2  
    --IN3: pin connected in pi with stepper motor driver's IN3  
    --IN4: pin connected in pi with stepper motor driver's IN4  
  
    
    

# Thank you